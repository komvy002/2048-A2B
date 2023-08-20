from typing import List
from tokenizer_module import Tokenizer
from summary_statistics_module import StatisticProtocol

# ========== Summarising Engine ==========

class SummarisingEngine:
    def __init__(self, stats: List[StatisticProtocol]):
        self.stats = stats
        self.tokenizer = Tokenizer()

    def compute_statistics(self, input_text) -> dict:
        pass
