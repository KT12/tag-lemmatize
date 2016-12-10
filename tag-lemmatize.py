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

# WordNet only cares about 4 parts of speech.
# The other parts of speech will be encoded as nouns.
part = {
    'N' : 'n',
    'V' : 'v',
    'J' : 'a',
    'S' : 's',
    'R' : 'r'
}