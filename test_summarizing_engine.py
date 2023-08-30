from summarizing_engine import SummarisingEngine
from tokenizer_module import Tokenizer
from summary_statistics_module import WordCount, WordFrequency
import pytest
    
@pytest.fixture
def real_tokenizer():
    return Tokenizer()

@pytest.fixture
def summarising_engine():
    return SummarisingEngine(stats=[WordCount(), WordFrequency()])

def test_compute_statistics(summarising_engine):
    result = summarising_engine.compute_statistics("dog dog cat duck")
    expected_word_count = 4
    expected_word_freq = [('dog', 2), ('cat', 1), ('duck', 1)]

    actual_word_freq = [(word_stat.word, word_stat.frequency) for word_stat in result['WordFrequency']]

    assert 'WordCount' in result
    assert 'WordFrequency' in result
    assert result['WordCount'] == expected_word_count
    assert sorted(actual_word_freq, key=lambda x: (-x[1], x[0])) == expected_word_freq