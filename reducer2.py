#!/usr/bin/env python3

import sys
from collections import Counter

def custom_reducer(k=3):  
    active_doc = None
    word_counter = Counter()

    for line in sys.stdin:
        line = line.strip()
        if "|" not in line: 
            continue

        doc_id, word, count = line.split("|")
        count = int(count)

        #for doc changes
        if active_doc and active_doc != doc_id:
            for top_word, top_count in word_counter.most_common(k):
                print(f"{active_doc},{top_word},{top_count}")
            word_counter = Counter()  #reset counter for new doc

        active_doc = doc_id
        word_counter[word] += count

    #for last doc
    if active_doc:
        for top_word, top_count in word_counter.most_common(k):
            print(f"{active_doc},{top_word},{top_count}")

if __name__ == "__main__":
    custom_reducer()
