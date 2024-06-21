import json
import asyncio
from asyncio import Semaphore
import click
from neo4j import AsyncGraphDatabase, AsyncDriver
from aiokafka import AIOKafkaConsumer
import logging as log

from patternmatcher.parse import (
    transform_tetragon_to_stix,
    get_observable_id,
    sanitize_bundle,
)
from patternmatcher.match import matches
from patternmatcher.load import load_to_neo4j

log.basicConfig(level=log.INFO)


class StixPatterMatcher:
    """
    This class listens for Tetragon logs from Kafka/Redpanda and matches it with indicators in Neo4j.
    """

    def __init__(self, neo4j_driver: AsyncDriver):
        self.indicators: dict[str, str] = {}
        self.lock = Semaphore()
        self.neo4j = neo4j_driver

    async def run(self, kafka_uri: str, kafka_topic: str):
        """Run the matcher for given kafka topic."""
        log.info(
            f"Running STIX pattern matcher for topic {kafka_topic} on {kafka_uri}."
        )
        await asyncio.gather(
            self._sheduled_task(self.load_indicators, 10),
            self.consume_kafka_topics(kafka_uri, kafka_topic),
        )

    async def _sheduled_task(self, task, interval: int = None):
        """Schedule an async task to run every interval seconds."""
        while True:
            await task()
            await asyncio.sleep(interval)

    async def load_indicators(self):
        """Load indicators from Neo4j."""

        query = """MATCH (i:Indicator) RETURN i"""
        async with self.neo4j.session() as session:
            async with self.lock:
                self.indicators.clear()
                result = await session.run(query)
                async for record in result:
                    data = record.data()["i"]
                    self.indicators[data["id"]] = data["pattern"]

        log.info(f"Currently watching {len(self.indicators)} indicators.")

    async def consume_kafka_topics(self, server: str, topic: str):
        consumer = AIOKafkaConsumer(
            topic, bootstrap_servers=server, auto_offset_reset="latest"
        )
        await consumer.start()
        async for message in consumer:
            log.debug(f"Received new consumer msg.")
            try:
                data = json.loads(message.value)
                bundle = transform_tetragon_to_stix(data)
                await self.check_bundle(bundle)
            except Exception as e:
                log.warning(f"Error transforming message: {e}")
                continue

    async def check_bundle(self, bundle):
        """Check if the bundle matches any of the indicators."""
        async with self.lock:
            for id, pattern in self.indicators.items():
                # load observed data to neo4j
                async with self.neo4j.session() as session:
                    await session.execute_write(
                        load_to_neo4j, sanitize_bundle(bundle)
                    )

                if matches(pattern, bundle):
                    log.info(f"Pattern {pattern} matched.")

                    # Add relation to indicator
                    query = """MATCH (i:Indicator {id: $id}), (o:ObservedData {id: $obs_id})
                                MERGE (i)-[:MATCHED]->(o)"""

                    async with self.neo4j.session() as session:
                        await session.run(
                            query, id=id, obs_id=get_observable_id(bundle)
                        )


@click.command()
@click.option(
    "--neo_uri",
    "-n",
    default="bolt://neo4j-poc.neo4j.svc.cluster.local:7687",
    help="Neo4j URI",
)
@click.option("--neo_user", "-u", default="neo4j", help="Username for Neo4j")
@click.option("--neo_pass", "-p", default="password", help="Password for Neo4j")
@click.option(
    "--kafka_uri",
    "-k",
    default="redpanda-src.redpanda.svc.cluster.local:9093",
    help="Kafka/Redpanda URI",
)
@click.option("--kafka_topic", "-t", default="signal", help="Kafka/Redpanda topic")
def main(neo_uri, neo_user, neo_pass, kafka_uri, kafka_topic):
    """Run the STIX indicator pattern matcher."""



    log.info(f"Starting STIX pattern matcher.")
    neo4j_driver = AsyncGraphDatabase.driver(uri=neo_uri, auth=(neo_user, neo_pass))

    log.info(f"Neo4j driver connected.")
    asyncio.run(StixPatterMatcher(neo4j_driver).run(kafka_uri, kafka_topic))


if __name__ == "__main__":
    main()
