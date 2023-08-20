import pytest
from file_access_module import DefaultFileAccessor, OutputPathValidator, click

# ================== Tests for DefaultFileAccessor ==================

def test_read_file(tmp_path):
    # Setup
    file_content = "Greetings Program!"
    test_file = tmp_path / "test.txt"
    test_file.write_text(file_content)
    accessor = DefaultFileAccessor()

    # Exercise
    read_content = accessor.read(test_file)

    # Verify
    assert read_content == file_content
