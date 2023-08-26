from typing import List
from tokenizer_module import Tokenizer
from summary_statistics_module import StatisticProtocol

class SummarisingEngine:
    def __init__(self, stats: List[StatisticProtocol]):
        self.stats = stats
        self.tokenizer = Tokenizer()

    def compute_statistics(self, input_text) -> dict:
        words = self.tokenizer.tokenize(input_text)
        results = {}
        for stat in self.stats:
            key = type(stat).__name__
            results[key] = stat.compute(words)
        return results