Docs

`tag-lemmatize` is a small bolt-on utility function to be used in concert with the `nltk` package.  The function accepts un-tokenized strings.

The function uses `nltk.tokenize.word_tokenize`to tokenize the string.  It then tags parts-of-speech (POS) in the context of the string using `nltk.pos_tag`, which assigns a  [Penn Treebank](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) POS tag.  The function then converts the Penn Treebank tag into the appropriate [WordNet](https://wordnet.princeton.edu/wordnet/frequently-asked-questions/database/)  POS tag.  Finally, it lemmatizes each word using `nltk.stem.WordNetLemmatizer` which only accepts WordNet tags.


If this small function was useful, **please** star/follow me!

