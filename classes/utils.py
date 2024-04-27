from random import sample
from copy import deepcopy


def generateSegments(segments):
    chart = [i for i in range(segments)]
    return chart


def shuffleAsCopy(chart):
    _chart = deepcopy(chart)
    _len = range(len(_chart))
    for _ in _len:
        i, j = sample(_len, k=2)
        _chart[i], _chart[j] = _chart[j], _chart[i]

    return _chart
