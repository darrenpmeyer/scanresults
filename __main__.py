from scanresults import ScanResults
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Generate markov text from a corpus')
parser.add_argument('-t','--train', default=2, type=int, metavar='train_n',
                    help="The size of the Markov state prefix to train the corpus on")
parser.add_argument('-s','--sentences', default=25, type=int, metavar='sentences',
                    help="The number of sentences to print")
parser.add_argument('corpus_path', nargs="+",
                    help="Paths to corpus files to train on. Globs are permitted")
args = parser.parse_args()

sr = ScanResults()
sr.add_files(*args.corpus_path)

sr.train(args.train)
out = sr.sentences(args.sentences)
if out is not None:
    print(out)
