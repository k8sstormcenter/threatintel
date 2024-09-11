
import json
from pathlib import Path
from stix2matcher.matcher import match

from patternmatcher.constants import STIX_VERSION
from patternmatcher.match import matches



def test_ssrf_matching():
    p = Path()
    with open('resource/stix/bundles/SSRF/oss-ssrf.json', 'r') as file:
        indicator_bundle = json.load(file)

    ssrf_indicator = indicator_bundle['objects'][0]
    pattern = ssrf_indicator["pattern"]
    pattern = "([artifact:message LIKE '%Fetching access token for service account%'] AND [artifact:message LIKE '%Loading new entry succeeded%'] AND [artifact:message LIKE '%/computeMetadata/v1/instance/service-accounts/default/token\" HTTP/200%'] AND [artifact:message LIKE '%GET /curl?url=http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token HTTP/2.0\" 200%']) WITHIN 60 SECONDS"

    # pattern = "[artifact:message LIKE '%I%']"

    with open('resource/stix/observed/oss/positives_token_theft.json') as file:
        observable_bundles = json.load(file)


    res = matches(pattern, observable_bundles)
    res = match(pattern, observable_bundles, stix_version=STIX_VERSION)

    print(res)

    pass
