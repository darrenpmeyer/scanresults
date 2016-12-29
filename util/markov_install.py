#!/usr/bin/env python3

import sys
import re
import os
import subprocess
import tempfile
import shutil


def make_tempdir(root=os.path.expanduser("~")):
    return tempfile.mkdtemp(dir=root)


def checkout_markov(tempdir, url="https://github.com/barrucadu/markov.git"):
    cwd = os.getcwd()
    os.chdir(tempdir)

    try:
        subprocess.check_call(['git', 'clone', "https://github.com/barrucadu/markov.git"])
    except Exception as e:
        os.chdir(cwd)
        raise(e)

    os.chdir(cwd)


def install_markov(tempdir):
    pyver = re.search("^(\d+)\.(\d+)", sys.version)
    pyverstr = "python{major}.{minor}".format(major=pyver.group(1), minor=pyver.group(2))

    library = None
    libpath = os.path.join('lib', pyverstr)

    for path in sys.path:
        if path.endswith(libpath):
            library = path
            break

    if library is None:
        raise ValueError("Cannot find a path ending in {}".format(libpath))

    print("Installing markov module at {}".format(library))
    shutil.move(os.path.join(tempdir, 'markov', 'markov'), library)
    shutil.rmtree(os.path.join(tempdir, 'markov'))


def rm_tempdir(tempdir):
    shutil.rmtree(tempdir)


def run(*args):
    tempdir = ""
    try:
        tempdir = make_tempdir()
        checkout_markov(tempdir)
        install_markov(tempdir)
    except Exception as e:
        print("Unable to install markov, see below.\n\n{}".format(e), file=sys.stderr)
    
    if os.path.exists(tempdir):
        rm_tempdir(tempdir)


if __name__ == "__main__":
    run(*sys.argv[1:])



