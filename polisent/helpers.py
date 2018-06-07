import numpy as np
from socialsent.util import lines


def get_vocab(fname, limit=None):
    vocab = [line.split()[0] for line in lines(fname)]
    return vocab[:limit]


def load_data(fname):
    X, Y = [], []
    filehandle = open(fname, 'r')
    for line in filehandle.readlines():
        x, y = line.split('\t')
        y = int(y.strip())
        X.append(x)
        Y.append(y)
    return X, Y


def get_seeds_from_vocab(lexicon, vocabfile, limit):
    vocab = get_vocab(vocabfile)
    pos_seeds, neg_seeds = [], []
    min_score, max_score = min(lexicon.values()), max(lexicon.values())
    for word in vocab:
        if word not in lexicon:
            continue
        if lexicon[word] == max_score and len(pos_seeds) < limit:
            pos_seeds.append(word)
        if lexicon[word] == min_score and len(neg_seeds) < limit:
            neg_seeds.append(word)
    return pos_seeds, neg_seeds


def pred_function(X, lexicon):
    Y_pred = []
    for x in X:
        pol_vals = [lexicon[word] for word in x.split() if word in lexicon]
        pol_mean = np.mean(pol_vals) if pol_vals else 0
        label = 1 if pol_mean > 0 else 0
        Y_pred.append(label)
    return Y_pred
