from typing import Protocol, List
import re

class TokenizationStrategy(Protocol):
    def tokenize(self, text: str) -> List[str]:
        ...

class DefaultTokenizationStrategy(TokenizationStrategy):
    def tokenize(self, text: str) -> List[str]:
        return re.findall(r'\b\w+\b', text)

class Tokenizer:
    def __init__(self, strategy: TokenizationStrategy = DefaultTokenizationStrategy()):
        self.strategy = strategy

    def tokenize(self, text: str) -> List[str]:
        return self.strategy.tokenize(text)