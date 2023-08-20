from file_access_module import DefaultFileAccessor, OutputPathValidator, click

# ================== Tests for file_access_module ==================

# ========== Test for DefaultFileAccessor ==========

def test_reading_file(tmp_path):
    file_content = "Greetings Program!"
    test_file = tmp_path / "test.txt"
    test_file.write_text(file_content)
    accessor = DefaultFileAccessor()
    
    read_content = accessor.read(test_file)
    assert read_content == file_content

