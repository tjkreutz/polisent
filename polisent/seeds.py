POLI_POS = ["perfect", "leuk", "gelukkig", "effectief", "correct", "winnen", "top", "positief", "succes", "prachtig"]
POLI_NEG = ["probleem", "slecht", "onzin", "onmogelijk", "jammer", "dom", "spijtig", "hypocriet", "kwaad", "discriminatie"]


def get_poliseeds():
    """Return the positive and negative seed words for the political domain. """
    return POLI_POS, POLI_NEG