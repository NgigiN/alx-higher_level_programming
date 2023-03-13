#!/usr/bin/python3

def multiple_returns(sentence):
    a = 0
    i = len(sentence)
    if i == 0:
        return (None, sentence[a])
    else:
        return ((i, sentence[a]))
