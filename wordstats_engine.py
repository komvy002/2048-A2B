from typing import Dict
from file_access_module import FileAccessorProtocol
from tokenizer_module import Tokenizer
from formatting_engine import FormatterProtocol, FileStats
from summarizing_engine import SummarisingEngine


# ========== Word Stats Manager ==========

class WordStatsManager:
    def __init__(self, 
                 file_accessor: FileAccessorProtocol, 
                 tokenizer: Tokenizer, 
                 summarising_engine: SummarisingEngine, 
                 formatters: Dict[str, FormatterProtocol] = None):
        
        self.file_accessor = file_accessor
        self.tokenizer = tokenizer
        self.summarising_engine = summarising_engine
        self.formatters = formatters or {}

    def register_formatter(self, format: str, formatter: FormatterProtocol):
        self.formatters[format] = formatter
    
    def get_formatter(self, format):
        return self.formatters.get(format, None)

    def process_file(self, input_path, number, output_spec):
        input_text = self.file_accessor.read(input_path)
        statistics = self.summarising_engine.compute_statistics(input_text)
        word_count = statistics["WordCount"]
        frequent_words = statistics["WordFrequency"][:number]
        file_stats = FileStats(input_path, word_count, frequent_words)
        
        for path, format in output_spec.items():
            formatter = self.get_formatter(format)
            if formatter:
                formatted_output = formatter.format_output(file_stats)
                self.file_accessor.write(path, formatted_output, mode='a')  
            else:
                print(f"Unsupported format: {format}")