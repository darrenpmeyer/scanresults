#!/usr/bin/env python3 -u
"""
Pulls messages that have no subtype (except "Me" messages) and no attachements
from a Slack channel data dump in JSON format
"""
from __future__ import print_function

import json
import re
import sys


def parse_json(jsonfile):
    archive = None
    with open(jsonfile, mode='r') as j:
        archive = json.load(j)

    if archive is None:
        raise Exception("Couldn't get any info from {}".format(jsonfile))

    for entry in archive:
        if 'type' in entry and entry['type'] != 'message':
            continue
        if 'subtype' in entry and entry['subtype'] != "me_mesage":
            continue

        cleantext = re.sub("^<@.+>:\s+", "", entry['text'])
        print(cleantext)


if __name__ == "__main__":
    for f in sys.argv[1:]:
        print("-> {}".format(f), file=sys.stderr)
        parse_json(f)

