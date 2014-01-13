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

def removeChar(s, c):
    if c in s:
        i = s.index(c)
        s = s[:i] + s[i+1:]
    return s

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1:
        s = unicode(argv[1])
    else:
        s = u"祝！新成人おめでとうございます"

    s = removeChar(s, u"で")
    s = removeChar(s, u"す")
    s = removeChar(s, u"お")

    s = shuffled(s)
    print s + u"ですお"

