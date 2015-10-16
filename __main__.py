from scanresults import ScanResults
import sys

sr = ScanResults()
sr.add_files(*sys.argv[1:])

sr.train()
out = sr.sentences()
if out is not None:
    print(out)
