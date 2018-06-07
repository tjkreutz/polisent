import json

from polisent import helpers
from polisent.seeds import get_poliseeds
from polisent.lexicon_adaptation import run_lexicon_adaptations

from sklearn.metrics import accuracy_score
from socialsent.polarity_induction_methods import random_walk
from socialsent.representations.representation_factory import create_representation

if __name__ == "__main__":

    # Load test data
    X_test, Y_test = helpers.load_data('data/test_politics.csv')

    # First predict polarity using the general purpose lexicon
    lexicon = json.load(open('data/lexicons/duoman.json', 'r'))
    Y_pred = helpers.pred_function(X_test, lexicon)
    accuracy = accuracy_score(Y_test, Y_pred)
    print('Accuracy for general lexicon: {}'.format(accuracy))

    # Use SentProp with 10 neighbors and beta=0.9
    print('Running SentProp..')
    pos_seeds, neg_seeds = get_poliseeds()
    vocab = helpers.get_vocab('data/vocab.txt')

    embedding_file = "data/example_embeddings/politics.txt"

    embeddings = create_representation("GIGA", embedding_file, vocab)

    polarities = random_walk(embeddings, pos_seeds, neg_seeds, nn=10, sym=True, arccos=True)

    # Adapt the general purpose lexicon for domain specific use (with optimal parameters)
    print('Running lexicon adaptation..')
    new_lexicon = run_lexicon_adaptations(lexicon, polarities, 0.06, 0.58, 0.25)
    Y_pred = helpers.pred_function(X_test, new_lexicon)
    accuracy = accuracy_score(Y_test, Y_pred)
    print('Accuracy for adapted lexicon: {}'.format(accuracy))
