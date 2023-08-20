from typing import Protocol, List
from summary_statistics_module import WordStat

# ========== Formatting Engine ==========

class FileStats:
    def __init__(self, input_path: str, word_count: int, frequent_words: List[WordStat]):
        self.input_path = input_path
        self.word_count = word_count
        self.frequent_words = frequent_words

class FormatterProtocol(Protocol):
    def format_output(self, file_stats: FileStats) -> str:
        pass

class TxtFormatter(FormatterProtocol):
    def format_output(self, file_stats: FileStats) -> str:
        pass

class CsvFormatter(FormatterProtocol):
    def format_output(self, file_stats: FileStats) -> str:
        pass