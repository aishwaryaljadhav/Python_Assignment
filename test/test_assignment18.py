from src.assignment18.util import word_statistics

def test_basic_case():
    words = ["bcdef", "abcdefg", "bcde", "bcdef"]
    
    unique_count, frequencies = word_statistics(words)
    
    assert unique_count == 3
    assert frequencies == [2, 1, 1]


def test_all_unique():
    words = ["a", "b", "c"]
    
    unique_count, frequencies = word_statistics(words)
    
    assert unique_count == 3
    assert frequencies == [1, 1, 1]

