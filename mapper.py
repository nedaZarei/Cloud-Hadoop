#!/usr/bin/env python
import sys
import re

pattern = r'(\w+),(.+)'

for line in sys.stdin:
    line = line.strip()
    match = re.search(pattern, line)
    if match:
        key = match.group(1)  #document id 
        value = match.group(2)  #content 
        words = value.split()
        for word in words:
            print("{}\t{}".format(word.lower(), key))
