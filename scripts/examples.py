#!/usr/bin/env python
#
#  Print out training examples, disregarding vocabulary.

from common.file import myopen

import sys

import string

def get_example(f):
    import common.hyperparameters
    HYPERPARAMETERS = common.hyperparameters.read("language-model")
    for l in myopen(f):
        prevwords = []
        for w in string.split(l):
            w = string.strip(w)
            prevwords.append(w)
            if len(prevwords) >= HYPERPARAMETERS["WINDOW_SIZE"]:
                yield prevwords[-HYPERPARAMETERS["WINDOW_SIZE"]:]

if __name__ == "__main__":
    assert len(sys.argv) == 2
    f = sys.argv[1]

    for (cnt, e) in enumerate(get_example(f)):
        print string.join(e)