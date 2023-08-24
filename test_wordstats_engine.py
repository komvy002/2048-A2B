import pytest
from unittest.mock import Mock, patch
from wordstats_engine import WordStatsManager
from file_access_module import FileAccessorProtocol
from tokenizer_module import Tokenizer
from formatting_engine import FormatterProtocol
from summarizing_engine import SummarisingEngine

class MockFileAccessor:
    def read(self, path):
        return "dog cat duck"
    
    def write(self, path, content, mode):
        pass

class MockTokenizer:
    pass

class MockSummarisingEngine:
    def compute_statistics(self, text):
        return {
            "WordCount": 2,
            "WordFrequency": [("dog", 1), ("cat", 1)]
        }

class MockFormatter:
    def format_output(self, stats):
        return str(stats)

def test_initialization():
    ws_manager = WordStatsManager(MockFileAccessor(), MockTokenizer(), MockSummarisingEngine())
    assert isinstance(ws_manager.file_accessor, MockFileAccessor)
    assert isinstance(ws_manager.tokenizer, MockTokenizer)
    assert isinstance(ws_manager.summarising_engine, MockSummarisingEngine)
    assert ws_manager.formatters == {}

def test_register_and_get_formatter():
    ws_manager = WordStatsManager(MockFileAccessor(), MockTokenizer(), MockSummarisingEngine())
    ws_manager.register_formatter("mock_format", MockFormatter())
    assert isinstance(ws_manager.get_formatter("mock_format"), MockFormatter)
    assert ws_manager.get_formatter("non_existent_format") is None
    
@patch("wordstats_engine.FileStats")
def test_process_file(mock_file_stats):
    ws_manager = WordStatsManager(MockFileAccessor(), MockTokenizer(), MockSummarisingEngine())
    ws_manager.register_formatter("mock_format", MockFormatter())
    output_spec = {
        "output.txt": "mock_format"
    }
    ws_manager.process_file("in.txt", 2, output_spec)
    mock_file_stats.assert_called_once_with("in.txt", 2, [("dog", 1), ("cat", 1)])
    
def test_process_file_with_unsupported_format():
    ws_manager = WordStatsManager(MockFileAccessor(), MockTokenizer(), MockSummarisingEngine())
    ws_manager.register_formatter("mock_format", MockFormatter())
    output_spec = {
        "output.doc": "unsupported_format"
    }
    with pytest.raises(Exception) as excinfo:
        ws_manager.process_file("input.txt", 2, output_spec)
    assert "Unsupported format: unsupported_format" in str(excinfo.value)