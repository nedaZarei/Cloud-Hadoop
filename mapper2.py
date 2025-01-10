#!/usr/bin/env python3

import sys
import re

def custom_mapper():
    for line in sys.stdin:
        line = line.strip()
        if "," in line: 
            doc_id, text = line.split(",", 1)
            words = re.findall(r'\b\w+\b', text.lower())  
            for word in words:
                print(f"{doc_id}|{word}|1")

if __name__ == "__main__":
    custom_mapper()
