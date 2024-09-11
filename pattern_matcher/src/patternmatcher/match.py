# https://github.com/oasis-open/cti-pattern-matcher/tree/master

from stix2matcher.matcher import match
from patternmatcher.constants import *
import logging as log


def matches(pattern, bundles: list[dict], stix_version=STIX_VERSION):
    try:
        return len(match(pattern, bundles, stix_version=stix_version)) > 0
    except Exception as e:
        log.error(f"Error matching pattern {pattern} to bundle {bundles}: {e}")
        return False


if __name__ == "__main__":
    result = matches(STIX_INDICATOR_PATTERN_EXAMPLE, OBSERVABLE_STIX_BUNDLE_EXAMPLE2)
    print(result)
