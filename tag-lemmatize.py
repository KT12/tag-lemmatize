#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:12:07 2016

@author: ktt

https://github.com/KT12

"""

from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# WordNet only cares about 5 parts of speech.
# The other parts of speech will be tagged as nouns.

part = {
    'N' : 'n',
    'V' : 'v',
    'J' : 'a',
    'S' : 's',
    'R' : 'r'
}

wnl = WordNetLemmatizer()

def convert_tag(penn_tag):
    '''
    convert_tag() accepts the **first letter** of a Penn part-of-speech tag,
    then uses a dict lookup to convert it to the appropriate WordNet tag.
    '''
    if penn_tag in part.keys():
        return part[penn_tag]
    else:
        # other parts of speech will be tagged as nouns
        return 'n'


def tag_and_lem(element):
    '''
    tag_and_lem() accepts a string, tokenizes, tags, converts tags,
    lemmatizes, and returns a string
    '''
    # list of tuples [('token', 'tag'), ('token2', 'tag2')...]
    sent = pos_tag(word_tokenize(element)) # must tag in context
    return ' '.join([wnl.lemmatize(sent[k][0], convert_tag(sent[k][1][0]))
                    for k in range(len(sent))])