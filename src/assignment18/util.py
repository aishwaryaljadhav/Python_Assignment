from collections import Counter

def word_statistics(words):
    counter = Counter(words)
    return len(counter), list(counter.values())
