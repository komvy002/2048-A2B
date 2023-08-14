import os
import click
from typing import Protocol, List, Dict

# ========== File Access ==========

# Define the File Accessor Interface
class FileAccessorProtocol(Protocol):
    def read(self, path: str) -> str:
        ...

    def write(self, path: str, content: str, mode: str = 'w') -> None:
        ...
# Implement Default File Accessor
class DefaultFileAccessor:
    def read(self, path: str) -> str:
        with open(path, 'r') as file:
            return file.read()

    def write(self, path: str, content: str, mode: str = 'w') -> None:
        with open(path, mode) as file:
            file.write(content)

class OutputPathValidator:
    VALID_FORMATS = ['.csv', '.txt']

    @staticmethod
    def validate(_ctx, _param, paths) -> Dict[str, str]:
        def getPathFormat(path):
            _base, extension = os.path.splitext(path)
            return extension.lower()

        output_spec = {}
        for path in paths:
            format = getPathFormat(path)
            if format not in OutputPathValidator.VALID_FORMATS:
                raise click.BadParameter(f"Output file {path} has an invalid format {format}. Known formats are {', '.join(OutputPathValidator.VALID_FORMATS)}.")
            output_spec[path] = format

        return output_spec

# ========== Tokeniser ==========

# Define the Tokenization Strategy Interface
class TokenizationStrategy(Protocol):
    def tokenize(self, text: str) -> List[str]:
        ...

# Implement Default Strategy
class DefaultTokenizationStrategy(TokenizationStrategy):
    def tokenize(self, text: str) -> List[str]:
        pass

class Tokenizer:
    def __init__(self, strategy: TokenizationStrategy = DefaultTokenizationStrategy()):
        self.strategy = strategy

    def tokenize(self, text: str) -> List[str]:
        return self.strategy.tokenize(text)

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

# ========== Summarising Engine ==========

class SummarisingEngine:
    def __init__(self, stats: List[StatisticProtocol]):
        self.stats = stats
        self.tokenizer = Tokenizer()

    def compute_statistics(self, input_text) -> dict:
        pass

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

# ========== Word Stats Manager ==========

class WordStatsManager:
    def __init__(self, 
                 file_accessor: FileAccessorProtocol, 
                 tokenizer: Tokenizer, 
                 summarising_engine: SummarisingEngine, 
                 formatters: Dict[str, FormatterProtocol] = None):
        
        pass

    def register_formatter(self, format: str, formatter: FormatterProtocol):
        self.formatters[format] = formatter
    
    def get_formatter(self, format):
        return self.formatters.get(format, None)

    def process_file(self, input_path, number, output_spec):
        pass

# ========== Console App ==========

@click.command(no_args_is_help=True)
@click.option("--number", default=10, type=click.IntRange(min=1),
              help="Maximum number of frequent words to include")
@click.option("--output", "output_spec", required=True, multiple=True, type=click.Path(),
              callback=OutputPathValidator.validate,
              help="Path of an output file. The extension (.txt or .csv) determines the output format.")
@click.argument("input_paths", required=True, type=click.Path(exists=True), nargs=-1)
def main(number, output_spec, input_paths):
    file_accessor = DefaultFileAccessor()
    tokenizer = Tokenizer(strategy=DefaultTokenizationStrategy())
    summarising_engine = SummarisingEngine([WordCount(), WordFrequency()])
    formatters = {
        '.txt': TxtFormatter(),
        '.csv': CsvFormatter()
    }

    manager = WordStatsManager(file_accessor, tokenizer, summarising_engine, formatters)

    for input_path in input_paths:
        manager.process_file(input_path, number, output_spec)

if __name__ == '__main__':
    main()