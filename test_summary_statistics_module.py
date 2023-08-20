from summary_statistics_module import WordCount, WordFrequency, WordStat

# ========== Tests for WordCount ==========
def test_word_count_empty_list():
    words = WordCount()
    result = words.compute([])
    assert result == 0, f"Expected 0 but got {result}"
