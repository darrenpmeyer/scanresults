#!/usr/bin/env python3 -u
"""
This is a very quick-and-dirty solution to grab comments from C-style source code.
Don't use it for anything important.
"""

import re
import sys


def get_comments(inf, outf):
    intext = inf.read()
    for match in re.finditer("/\*((?:[^*]|[\r\n]|(?:\*+([^*/]|[\r\n])))*)\*+/|//+(.+[\r\n])", intext, re.MULTILINE):
        for group in match.groups():
            if group is not None:
                print(group.strip(), file=outf)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        get_comments(sys.stdin, sys.stdout)
    else:
        for infile in sys.argv[1:]:
            print("=> {}".format(infile), file=sys.stderr)
            with open(infile, mode='r') as inf:
                get_comments(inf, sys.stdout)

