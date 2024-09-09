#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        fisrt = None
    else:
        first = sentence[:1]
    return (length, first)
