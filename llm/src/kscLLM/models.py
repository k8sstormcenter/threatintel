from typing import TypedDict


class KillChainPhase(TypedDict):
    kill_chain_name: str
    phase_name: str


class STIXIndicator(TypedDict):
    name: str
    pattern: str
    kill_chain_phases: list[KillChainPhase]
    description: str
    indicator_types: list[str]
