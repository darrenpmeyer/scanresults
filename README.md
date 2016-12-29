# scanresults

Support code and documentation for the @ScanResults and @EngineAPoe markov accounts

# About

The @ScanResults and @EngineAPoe accounts are curated from the results of Markov-chain text generators trained
on corpuses containing the [Veracode SAST][1] finding and remediation advice templates combined with one or more
well-known literary texts.

@EngineAPoe uses the complete works of Edgar Allan Poe (with literary commentary)

@ScanResults uses several combinations of the following:

* Hamlet
* Hitchhikers Guide to the Galaxy

[1]: https://www.veracode.com/products/binary-static-analysis-sast "Veracode SAST landing page"

# Disclaimer

This project was produced as part of a Veracode hackathon, but the twitter accounts and work product are not reviewed
or sanctioned by Veracode. All work done as part of this is a personal project, so direct complaints at me.

# Setup and Usage

## Summary

    python3 -u -m scanresults /path/to/corpus_file.txt

You may speficy more than one corpus, and each may be a file or a file glob.

## Initial setup

    mkdir ~/scanresults-install
    cd ~/scanresults-install
    git clone https://github.com/barrucadu/markov.git
    git clone https://github.com/darrenpmeyer/scanresults.git
    
You can instead use the `util/markov_install.py` script to add the `markov` library into your site library. **This is experimental, and you should proceed at your own risk**. If you do this, you will not need to alter your `PYTHONPATH` to include the `markov` library.

## Run environment

    export PYTHONPATH=~/scanresults-install/markov:~/scanresults-install

## Running

You **must** make sure the `scanresults` module and the `markov` module are in your `PYTHONPATH`. See _Run environment_ above.

	python3 -u -m scanresults [options] corpus_file [corpus_file ...]

    Options:
       -t <num> : size of chain to train. Default: 2. Larger values give
                  more comprehensibility, but less humor.
       -s <num> : number of sentences to generate. Default: 25.
       
       corpus_file : a plain text file or file glob specifying plain text
                     files to use as an input corpus

# Notes and Dependencies

* Python 3
* [barrucadu/markov](https://github.com/barrucadu/markov)
* docopt (`pip3 install docopt`) is required for some components of the markov; you may be able to get away with
  not using it, since it's really only needed for the REPL, which we don't use