import math
import operator


def get_lexicon_distribution(lexicon):
    distro_dict = {polarity: 0 for polarity in get_lexicon_classes(lexicon)}
    for polarity in lexicon.values():
        distro_dict[polarity] += 1
    return distro_dict


def get_lexicon_classes(lexicon):
    return set(lexicon.values())


def get_pos_neg(polarities, B, y):
    pos_limit = int((1 - y) * B * len(polarities))
    neg_limit = int(y * B * len(polarities))
    return pos_limit, neg_limit


def get_pos_neg_zero(polarities, B, y):
    pos_limit, neg_limit = get_pos_neg(polarities, B, y)
    zero_limit = len(polarities) - pos_limit - neg_limit
    return pos_limit, neg_limit, zero_limit


def get_even_distribution(limit, length):
    distribution = []
    pure_divide = float(limit) / length
    floor_divide = math.floor(pure_divide)
    for i in range(length):
        remainder = math.ceil(pure_divide*i - sum(distribution))
        distribution.append(int(floor_divide + remainder))
    return distribution


def get_distribution(polarities, classes, B, y):
    pos_limit, neg_limit, zero_limit = get_pos_neg_zero(polarities, B, y)
    pos_count, neg_count = len([p for p in classes if p > 0]), len([p for p in classes if p < 0])
    limits = get_even_distribution(neg_limit, neg_count)
    limits.append(zero_limit)
    limits.extend(get_even_distribution(pos_limit, pos_count))
    return zip(limits, sorted(classes))


def cluster_polarities(polarities, classes, B, y):
    clustered_polarities = {}
    sorted_polarities = sorted(polarities.iteritems(), key=operator.itemgetter(1))
    distribution = get_distribution(polarities, classes, B, y)
    for d, c in distribution:
        slice, sorted_polarities = sorted_polarities[:d], sorted_polarities[d:]
        for word, polarity in slice:
            clustered_polarities[word] = c
    return clustered_polarities


def extend_lexicon(lexicon, polarities):
    count = 0
    for w, p in polarities.iteritems():
        if not p == 0 and w not in lexicon:
            count += 1
            lexicon[w] = p
    print('{} words added to lexicon'.format(count))
    return lexicon


def enhance_lexicon(lexicon, polarities, c):
    count = 0
    classes = get_lexicon_classes(lexicon)
    min_range_dif = abs(min(classes) - max(classes)) * c
    for w, p in polarities.iteritems():
        if w in lexicon and 0 < abs(p - lexicon[w]) < min_range_dif:
            count += 1
            lexicon[w] = p
    print('{} known words changed polarity'.format(count))
    return lexicon


def run_lexicon_adaptations(lexicon, polarities, B, y, c):
    classes = get_lexicon_classes(lexicon)
    polarities = cluster_polarities(polarities, classes, B, y)
    lexicon = extend_lexicon(lexicon, polarities)
    lexicon = enhance_lexicon(lexicon, polarities, c)
    return lexicon
