#!/usr/bin/env python
import sys
import re

#extracting document id and content
pattern = r'(\w+),(.+)'

for line in sys.stdin:
    line = line.strip()
    match = re.search(pattern, line)
    if match:
        doc_id = match.group(1)  #extracting doc id
        content = match.group(2)  #extracting content of the document
        words = content.lower().split()  #converting to lowercase and split into words
        for word in words:
            print("{}\t{}".format("{},{}".format(word, doc_id), 1))

