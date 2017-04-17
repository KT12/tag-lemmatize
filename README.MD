## Summary

`tag-lemmatize` is a small bolt-on utility function to be used in concert with the `nltk` package.  The function accepts un-tokenized strings.  The original intent was to write a small function which would ease the use of the [VADER](http://www.nltk.org/_modules/nltk/sentiment/vader.html) sentiment analysis tool.

The function uses `nltk.tokenize.word_tokenize`to tokenize the string.  It then tags parts-of-speech (POS) taking into account context using `nltk.pos_tag`, which assigns a  [Penn Treebank](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) POS tag.  The function then converts the Penn Treebank tag into the appropriate [WordNet](https://wordnet.princeton.edu/wordnet/frequently-asked-questions/database/)  POS tag.  Finally, it lemmatizes each word using `nltk.stem.WordNetLemmatizer`.

## Installation

Clone and add to `path`.

`import` to the Python interpreter.

`tag_and_lem` is the primary function.

## Motivation

The `nltk` pre-trained part-of-speech tagger uses Penn Treebank tags which must be converted to Wordnet tags in order to use `nltk`'s lemmatizer.  This small utility should make it easier to test of Natural Language Processing techniques without training a tagger which uses Wordnet tags.

## Requirements

Python 2.6+
nltk

## Contributors

@KT12

If this small function was useful, **please** star/follow [me](https://github.com/KT12)!
