import numpy as np
from socialsent.util import lines


def get_vocab(fname, limit=None):
    """Load vocabulary file and return as list with a given length limit"""
    vocab = [line.split()[0] for line in lines(fname)]
    return vocab[:limit]


def load_data(fname):
    """Load documents and labels"""
    X, Y = [], []
    filehandle = open(fname, 'r')
    for line in filehandle.readlines():
        x, y = line.split('\t')
        y = int(y.strip())
        X.append(x)
        Y.append(y)
    return X, Y


def pred_function(X, lexicon):
    """Predict the polarity label using lexicon lookup and averaging over document"""
    Y_pred = []
    for x in X:
        pol_vals = [lexicon[word] for word in x.split() if word in lexicon]
        pol_mean = np.mean(pol_vals) if pol_vals else 0
        label = 1 if pol_mean > 0 else 0
        Y_pred.append(label)
    return Y_pred
