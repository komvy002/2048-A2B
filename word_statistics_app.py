import click
from typing import Protocol, List, Dict
from file_access_module import FileAccessorProtocol, DefaultFileAccessor, OutputPathValidator
from summary_statistics_module import WordStat, StatisticProtocol, WordCount, WordFrequency
from tokenizer_module import TokenizationStrategy, DefaultTokenizationStrategy, Tokenizer
from formatting_engine import FileStats, FormatterProtocol, TxtFormatter, CsvFormatter
from summarizing_engine import SummarisingEngine
from wordstats_engine import WordStatsManager

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