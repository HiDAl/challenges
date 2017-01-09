from data import DICTIONARY, LETTER_SCORES
import re

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
      return f.read().splitlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    scores = map((lambda c: LETTER_SCORES.get(c, 0)), list(word.upper()))

    return sum(scores)

def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
