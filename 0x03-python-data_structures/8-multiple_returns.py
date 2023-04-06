#!/usr/bin/python3

""" def multiple_returns(sentence):
    senlen = len(sentence)
    if senlen == 0:
        return (0, None)
    return (senlen, sentence[0]) """

def multiple_returns(sentence):
    slen = len(sentence)
    return (slen, None if slen == 0 else sentence[0])