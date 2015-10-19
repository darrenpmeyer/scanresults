#!/usr/bin/env python3 -u
from __future__ import print_function

import re
from os import path
import sys


def clean(inf, outf):
    # if not (path.exists(inputfile) and path.isfile(inputfile)):
    #     raise ValueError("{} does not exist or is not a file".format(inputfile))

    undesirable = re.compile("^(\s|----|r(\d+)\s)")
    # outf = open(outputfile, mode='w')
    # with open(inputfile, mode='r') as inf:
    for line in inf.readlines():
        if len(line) < 3 or undesirable.search(line):
            pass
        else:
            print(line, file=outf, end="")


if __name__ == "__main__":
    clean(sys.stdin, sys.stdout)