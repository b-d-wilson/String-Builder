from time import perf_counter as timer
from typing import List

def join_words(words: List[str]) -> str:
    """Joins words using string concatenation"""
    sentence = ""
    for word in words:
        sentence += word
    return sentence


test_words = ['hehe', 'haha', 'hoho', 'hawhaw', 'ehehe', 'muahahahahhaha'] * 100000
start = timer()
joined = join_words(test_words)
stop = timer()
print(f'Runtime of join_words was {stop - start:0.4f} seconds')
