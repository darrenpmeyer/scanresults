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

# Usage

    python3 -u -m /path/to/scanresults /path/to/corpus_file.txt
    
You may speficy more than one corpus file, and each argument may be a fileglob.

# Notes and Dependencies

* Python 3

* [barrucadu/markov](https://github.com/barrucadu/markov) -- **NOTE**:
  This currently requires [the `modularize` branch of this fork][2]; I have submitted a pull request into the main
  barrucadu repo that should eventually remove this special dependency.
  
* docopt (`pip3 install docopt`) is required for some components of the markov; you may be able to get away with
  not using it, since it's really only needed for the REPL, which we don't use

[2]: https://github.com/darrenpmeyer/markov/tree/modularize