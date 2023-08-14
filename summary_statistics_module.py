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
        pass

class WordFrequency(StatisticProtocol):
    def compute(self, words: list[str]) -> List[WordStat]:
        pass