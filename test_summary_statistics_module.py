from summary_statistics_module import WordCount, WordFrequency, WordStat

# ========== Tests for WordCount ==========
def test_word_count_empty_list():
    word_count = WordCount()
    result = word_count.compute([])
    
    assert result == 0, f"Expected 0 but got {result}"

def test_word_count_full_list():
    word_count = WordCount()
    word_list = ["dog", "dog", "cat", "duck"]
    result = word_count.compute(word_list)
    
    assert result == 4, f"Expected 4 but got {result}"