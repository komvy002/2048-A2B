from collections import Counter
from typing import Protocol, List

class WordStat:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency
        
    # Used for testing by comparing objects equality based on their attributes not their references.
    def __eq__(self, other):
        if not isinstance(other, WordStat):
            return NotImplemented
        return self.word == other.word and self.frequency == other.frequency

class StatisticProtocol(Protocol):
    def compute(self, words: list[str]):
        ...

class WordCount(StatisticProtocol):
    def compute(self, words: list[str]) -> int:
        return len(words)

class WordFrequency(StatisticProtocol):
    def compute(self, words: list[str]) -> List[WordStat]:
        word_freq = Counter(words)
        return [WordStat(word, frequency) for word, frequency in word_freq.most_common()]