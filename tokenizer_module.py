from typing import Protocol, List
import re

# ========== Tokeniser ==========

# Define the Tokenization Strategy Interface
class TokenizationStrategy(Protocol):
    def tokenize(self, text: str) -> List[str]:
        ...

# Implement Default Strategy
class DefaultTokenizationStrategy(TokenizationStrategy):
    def tokenize(self, text: str) -> List[str]:
        return re.findall(r'\b\w+\b', text)

# Tokenize using the DefaultTokenizationStrategy
class Tokenizer:
    def __init__(self, strategy: TokenizationStrategy = DefaultTokenizationStrategy()):
        self.strategy = strategy

    def tokenize(self, text: str) -> List[str]:
        return self.strategy.tokenize(text)
