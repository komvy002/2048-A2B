from tokenizer_module import DefaultTokenizationStrategy, Tokenizer

# Testing for the tokenizer_module

def test_default_tokenization_strategy_with_letters():
    strategy = DefaultTokenizationStrategy()
    result = strategy.tokenize("a a a a a")
    assert result == ["a", "a", "a", "a", "a"]

def test_default_tokenization_strategy_with_words():
    strategy = DefaultTokenizationStrategy()
    result = strategy.tokenize("dog cat dog cat dog dog dog duck")
    assert result == ["dog", "cat", "dog", "cat", "dog", "dog", "dog", "duck"]

def test_default_tokenization_strategy_with_numbers():
    strategy = DefaultTokenizationStrategy()
    result = strategy.tokenize("1 2 3 4 5")
    assert result == ["1", "2", "3", "4", "5"]
    
def test_default_tokenization_strategy_with_mix_letters_numbers_words():
    strategy = DefaultTokenizationStrategy()
    result = strategy.tokenize("1 f dog 4 cat")
    assert result == ["1", "f", "dog", "4", "cat"]
    
def test_tokenizer_with_default_strategy():
    tokenizer = Tokenizer()
    result = tokenizer.tokenize("dog cat dog cat dog dog dog duck")
    assert result == ["dog", "cat", "dog", "cat", "dog", "dog", "dog", "duck"]