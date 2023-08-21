from collections import Counter
from typing import Protocol, List

# ========== Summary Statistics Protocols and Implementations ==========

class WordStat:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

class StatisticProtocol(Protocol):
    def compute(self, words: list[str]):
        ...

class WordCount(StatisticProtocol):
    def compute(self, words: list[str]) -> int:
        return len(words)

class WordFrequency(StatisticProtocol):
    def compute(self, words: list[str]) -> List[WordStat]:
        word_freq = Counter(words)
        print(f"word_freq= " + {word_freq})