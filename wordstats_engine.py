from typing import Dict
from file_access_module import FileAccessorProtocol
from tokenizer_module import Tokenizer
from formatting_engine import FormatterProtocol
from summarizing_engine import SummarisingEngine

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