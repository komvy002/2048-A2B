from file_access_module import DefaultFileAccessor, OutputPathValidator, click

# ================== Tests for file_access_module ==================

# ========== Test for DefaultFileAccessor ==========

def test_reading_file(tmp_path):
    # Check if the read function can successfully read a files contents
    file_content = "Greetings Program!"
    test_file = tmp_path / "test.txt"
    test_file.write_text(file_content)
    accessor = DefaultFileAccessor()
    
    read_content = accessor.read(test_file)
    assert read_content == file_content

def test_writing_file(tmp_path):
    # Check if the write function can successfully write content to a file
    content_to_write = "Welcome to the Grid!"
    test_file = tmp_path / "write_test.txt"
    accessor = DefaultFileAccessor()

    accessor.write(test_file, content_to_write)

    written_content = test_file.read_text()
    assert written_content == content_to_write
    
def test_append_file(tmp_path):
    # Test that you can successfully append file contents
    initial_content = "Greetings"
    appended_content = ", SuperUsers!"
    test_file = tmp_path / "append_test.txt"
    test_file.write_text(initial_content)
    accessor = DefaultFileAccessor()

    accessor.write(test_file, appended_content, mode='a')

    final_content = test_file.read_text()
    assert final_content == initial_content + appended_content