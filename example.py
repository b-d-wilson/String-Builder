from time import perf_counter as timer
from typing import List

from stringbuilder import StringBuilder

def join_words_cat(words: List[str]) -> str:
    """Joins words using string concatenation"""
    sentence = ""
    for word in words:
        sentence += word
    return sentence


def join_words_builder(words: List[str]) -> str:
    """Joins words using a StringBuilder"""
    builder = StringBuilder()
    for word in words:
        builder.append(word)
    return builder.to_string()


def join_words_join(words: List[str]) -> str:
    """Joins words using str.join"""
    return ''.join(words)

test_words = ['hehe', 'haha', 'hoho', 'hawhaw', 'ehehe', 'muahahahahhaha'] * 10000000

start = timer()
joined = join_words_cat(test_words)
stop = timer()
print(f'Runtime of join_words_cat was {stop - start:0.4f} seconds')

start = timer()
joined = join_words_builder(test_words)
stop = timer()
print(f'Runtime of join_words_builder was {stop - start:0.4f} seconds')

start = timer()
joined = join_words_join(test_words)
stop = timer()
print(f'Runtime of join_words_join was {stop - start:0.4f} seconds')
