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
        return f"File {file_stats.input_path} contains {file_stats.word_count} words. Frequent words are: " + \
               ", ".join([f"{word_stat.word} ({word_stat.frequency})" for word_stat in file_stats.frequent_words]) + "\n"

class CsvFormatter(FormatterProtocol):
    def format_output(self, file_stats: FileStats) -> str:
        row = [file_stats.input_path, str(file_stats.word_count)]
        for word_stat in file_stats.frequent_words:
            row.extend([word_stat.word, str(word_stat.frequency)])
        return ','.join(row) + "\n"