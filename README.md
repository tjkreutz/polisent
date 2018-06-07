## Polisent

Work done in adapting general purpose sentiment lexicons for domain specific use. We specifically used word embeddings from the political domain to automatically learn new polarity values using [SentProp](https://nlp.stanford.edu/projects/socialsent/).

### Authors: Tim Kreutz and Walter Daelemans
### Paper: Not yet available

### Overview

The methods used are available in this repository, but they rely heavily on the [socialsent](https://github.com/williamleif/socialsent) package which needs:

- python (2.7)
- theano (0.8.0)
- keras (0.3.3)
- sklearn (0.19)
- numpy
- scipy

The lexicon, embeddings, tweet data are all available and can be downloaded and tested by running example.sh.
