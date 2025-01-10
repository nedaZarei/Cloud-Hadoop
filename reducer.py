#!/usr/bin/env python
import sys
from collections import defaultdict

#dict to store the documents where each word is
word_docs = defaultdict(set)

#from the mapper
for line in sys.stdin:
    line = line.strip()
    word, doc = line.split('\t', 1)
    word_docs[word].add(doc)

for word, docs in sorted(word_docs.items()):
    print("{} : {{{}}}".format(word, ', '.join(sorted(docs))))
