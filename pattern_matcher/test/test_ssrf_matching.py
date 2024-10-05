import json
import sys
from pathlib import Path
from stix2matcher.matcher import match

from patternmatcher.constants import STIX_VERSION
from patternmatcher.match import matches

ROOT_PATH = Path(__file__).parent.parent.resolve()


def test_ssrf_oss_matching():
    with open("resource/stix/bundles/SSRF/oss-ssrf.json", "r") as file:
        indicator_bundle = json.load(file)

    ssrf_indicator = indicator_bundle["objects"][0]
    pattern = ssrf_indicator["pattern"]
    pattern = "([artifact:message LIKE '%Fetching access token for service account%'] AND [artifact:message LIKE '%Loading new entry succeeded%'] AND [artifact:message LIKE '%/computeMetadata/v1/instance/service-accounts/default/token\" HTTP/200%'] AND [artifact:message LIKE '%GET /curl?url=http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token HTTP/2.0\" 200%']) WITHIN 60 SECONDS"

    with open("resource/stix/observed/oss/positives_token_theft.json") as file:
        observable_bundles = json.load(file)

    # res = matches(pattern, observable_bundles) # boolean from library
    res = match(pattern, observable_bundles, stix_version=STIX_VERSION)

    for bundle in res:
        print(bundle["id"])


def test_ssrf_kcdaut_matching():
    with open(ROOT_PATH / "resource/stix/bundles/SSRF/kcd_aut_ssrf.json", "r") as file:
        indicator_bundle = json.load(file)

    indicator = indicator_bundle["objects"][0]
    pattern = indicator["pattern"]
    print(pattern)

    with open(
        ROOT_PATH / "resource/stix/observed/KCD-AUT/credential_steal_gke_tobias.json",
        "r",
    ) as file:
        observable_bundles = json.load(file)

    res = match(pattern, observable_bundles, stix_version=STIX_VERSION, verbose=False)

    assert len(res) == 2
    for bundle in res:
        print(bundle["id"])

    assert (
        res[0]["objects"][1]["id"] == "artifact--10c4b3ee-a55a-58ce-a2a3-8c26ee398a04"
    )
    assert (
        res[1]["objects"][1]["id"] == "artifact--6c20f3ab-ffd0-5afa-8f89-9cd1371a8a22"
    )
