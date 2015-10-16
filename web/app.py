from flask import Flask, request, render_template, session
from scanresults import ScanResults

app = Flask(__name__)
app.secret_key = 'ChangeThisForYourInstance!'

ROOT = ''  # can be changed to e.g. /scan if you want to use that sub-path
CORPUS_GLOB = '../../codescan-markov-corpus-sources/persona/engine_allan_poe.txt'

TRAIN_N_DEFAULT = 2
TRAIN_PARA_DEFAULT = False
SENTENCES_DEFAULT = 25


@app.route(ROOT + '/', methods=['GET'])
@app.route(ROOT + '/<sentences>', methods=['GET'])
def generate(sentences=SENTENCES_DEFAULT):
    # print(repr(request.args['s']))
    sentences=int(sentences)

    chain = ScanResults()
    chain.add_files(CORPUS_GLOB)
    chain.train(n=TRAIN_N_DEFAULT, paragraphs=TRAIN_PARA_DEFAULT)
    if chain.errors:
        return render_template('error.html', errors=[repr(item) for item in chain.errors])

    return render_template('output.html', output=chain.sentences(n=sentences))


if __name__ == "__main__":
    app.run(debug=True)