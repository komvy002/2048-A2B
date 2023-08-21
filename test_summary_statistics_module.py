import pytest
from summary_statistics_module import WordCount, WordFrequency, WordStat

# Use fixtures to provide objects for tests
@pytest.fixture
def word_list() -> list:
    return ["dog", "dog", "cat", "duck"]

@pytest.fixture
def letter_list() -> list:
    return ["a", "a", "b", "c"]

@pytest.fixture
def number_list() -> list:
    return ["1", "1", "2", "3"]

@pytest.fixture
def mixed_list() -> list:
    return ["dog", "a", "1", "dog"]

# ========== Tests for WordCount ==========
def test_word_count_empty_list():
    word_count = WordCount()
    result = word_count.compute([])
    
    assert result == 0, f"Expected 0 but got {result}"

def test_word_count_word_list(word_list):
    word_count = WordCount()
    result = word_count.compute(word_list)
    
    assert result == 4, f"Expected 4 but got {result}"
    
def test_word_count_letter_list(letter_list):
    word_count = WordCount()
    result = word_count.compute(letter_list)
    
    assert result == 4, f"Expected 4 but got {result}"
    
def test_word_count_number_list(number_list):
    word_count = WordCount()
    result = word_count.compute(number_list)
    
    assert result == 4, f"Expected 4 but got {result}"
    
def test_word_count_mixed_list(mixed_list):
    word_count = WordCount()
    result = word_count.compute(mixed_list)
    
    assert result == 4, f"Expected 4 but got {result}"
    
# ========== Tests for WordFrequency ==========
def test_word_frequency_empty_list():
    word_frequency = WordFrequency()
    result = word_frequency.compute([])
    
    assert result == [], f"Expected empty list but got {result}"
    
def test_word_frequency_word_list(word_list):
    word_frequency = WordFrequency()
    result = word_frequency.compute(word_list)
    expected = [WordStat("dog", 2), WordStat("cat", 1), WordStat("duck", 1)]
    
    assert result == expected, f"Expected {expected} but got {result}"
    
def test_word_frequency_letter_list(letter_list):
    word_frequency = WordFrequency()
    result = word_frequency.compute(letter_list)
    expected = [WordStat("a", 2), WordStat("b", 1), WordStat("c", 1)]
    
    assert result == expected, f"Expected {expected} but got {result}"
    
def test_word_frequency_number_list(number_list):
    word_frequency = WordFrequency()
    result = word_frequency.compute(number_list)
    expected = [WordStat("1", 2), WordStat("2", 1), WordStat("3", 1)]
    
    assert result == expected, f"Expected {expected} but got {result}"
    
def test_word_frequency_mixed_list(mixed_list):
    word_frequency = WordFrequency()
    result = word_frequency.compute(mixed_list)
    expected = [WordStat("dog", 2), WordStat("a", 1), WordStat("1", 1)]
    
    assert result == expected, f"Expected {expected} but got {result}"