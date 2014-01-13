#! coding: utf-8
import random as R
import sys

def shuffled(origin_string):
    """デバッグ用関数"""
    clone = list(origin_string)
    shuffled_string = ""
    while len(clone) > 0:
        shuffled_string += clone.pop(R.randint(0, len(clone) - 1))
    return shuffled_string

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1:
        s = unicode(argv[1])
    else:
        s = u"祝！新成人めとうございま"
    s = shuffled(s)
    print s + u"ですお"

