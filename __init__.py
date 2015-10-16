import os
import glob
import fileinput

from markov import markovstate


class ScanResults:
    def __init__(self, corpus=None):
        self.markovstate = markovstate.MarkovState()
        self.corpus = corpus
        self.errors = list()

    def _paths(self, *pathlist):
         return [path
                 for ps in pathlist
                 for path in glob.glob(os.path.expanduser(ps))]

    def add_text(self, text):
        if self.corpus is None:
            self.corpus = ""
        self.corpus += text

    def add_files(self, *pathlist):
        self.errors = list()
        paths = self._paths(*pathlist)

        if paths is None or paths == []:
            raise ValueError("No paths provided")

        for path in paths:
            text = ""
            try:
                with open(path, mode='r') as f:
                    text = f.read()

            except IOError as err:
                self.errors.append(err)
                continue

            if text[-1] != "\n":
                text += "\n"

            self.add_text(text)

        if len(self.errors):
            return None
        else:
            return True

    def train(self, n=2, paragraphs=False, altcorpus=None):
        def _charinput(text=None):
            if text is None:
                text = self.corpus
            for line in text.splitlines(keepends=True):
                for char in line:
                    yield char

        self.markovstate.train(n, _charinput(self.corpus), noparagraphs=not paragraphs)

    def paragraphs(self, n=3):
        output = ""
        self.errors = list()
        try:
            output = self.markovstate.generate(n, None, 0, 0,
                                      endchunkf=lambda t: t == '\n\n',
                                      kill=1, prefix=("\n\n",))
        except markovstate.MarkovStateError as e:
            self.errors.append(e)
            return None

        return output

    def sentences(self, n=45):
        output = ""
        self.errors = list()
        sentence_token = lambda t: t[-1] in ".!?"
        try:
            output = self.markovstate.generate(n, None, 0, 0,
                                      startf=sentence_token,
                                      endchunkf=sentence_token,
                                      prefix=())
        except markovstate.MarkovStateError as e:
            self.errors.append(e)
            return None

        return output
