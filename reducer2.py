#!/usr/bin/env python
import sys
from collections import defaultdict

# dict to store word frequencies for each document
doc_word_counts = defaultdict(lambda: defaultdict(int))

# from mapper
for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t')
    word, doc_id = key.split(',')
    doc_word_counts[doc_id][word] += int(count)

# top k words per document
K = 3
for doc_id, word_counts in doc_word_counts.items():
    # sorting words by frequency in desc, then alphabetically
    top_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))[:K]
    for word, count in top_words:
        print("{},{},{}".format(doc_id, word, count))
