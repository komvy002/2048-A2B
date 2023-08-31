
import pytest
from click.testing import CliRunner
from word_statistics_app import main
import os

@pytest.fixture
def runner():
    return CliRunner()

def create_dummy_input_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def test_main_with_valid_words_input(runner):
    create_dummy_input_file('in.txt', 'dog, dog, cat, duck')
    output_filename = 'out.txt'

    result = runner.invoke(main, ['--number', '5', '--output', output_filename, 'in.txt'])
    
    assert result.exit_code == 0
    assert os.path.exists(output_filename)
    with open(output_filename, 'r') as f:
        output_content = f.read()
    assert 'dog' in output_content
    assert 'cat' in output_content
    assert 'duck' in output_content

    os.remove('in.txt')
    os.remove(output_filename)
    
def test_main_with_valid_letters_input(runner):
    create_dummy_input_file('in.txt', 'd, d, c, c')
    output_filename = 'out.txt'

    result = runner.invoke(main, ['--number', '5', '--output', output_filename, 'in.txt'])
    
    assert result.exit_code == 0
    assert os.path.exists(output_filename)
    with open(output_filename, 'r') as f:
        output_content = f.read()
    assert 'd' in output_content
    assert 'c' in output_content

    os.remove('in.txt')
    os.remove(output_filename)
    
def test_main_with_multiple_valid_output_files(runner):
    create_dummy_input_file('in.txt', 'dog, dog, cat, duck')
    output_files = ['out.txt', 'out.csv']

    result = runner.invoke(main, ['--number', '10', '--output', 'out.txt', '--output', 'out.csv', 'in.txt'])

    assert result.exit_code == 0
    for output_file in output_files:
        assert os.path.exists(output_file)
        with open(output_file, 'r') as f:
            output_content = f.read()
        assert 'dog' in output_content
        assert 'cat' in output_content
        assert 'duck' in output_content

    os.remove('in.txt')
    for output_file in output_files:
        os.remove(output_file)
        
def test_main_with_mixed_valid_and_invalid_output_files(runner):
    create_dummy_input_file('in.txt', 'dog, dog, cat, duck')

    result = runner.invoke(main, ['--number', '10', '--output', 'out.txt', '--output', 'out.doc', 'in.txt'])

    assert "Output file out.doc has an invalid format .doc" in result.output
    assert result.exit_code != 0
    assert not os.path.exists('out.txt')
    assert not os.path.exists('out.doc')

    os.remove('in.txt')
    if os.path.exists('out.txt'):
        os.remove('out.txt')
    if os.path.exists('out.doc'):
        os.remove('out.doc')

def test_main_with_invalid_number_value(runner):
    create_dummy_input_file('in.txt', 'dog, dog, cat, duck')
 
    result = runner.invoke(main, ['--number', '0', '--output', 'out.txt', 'in.txt'])

    assert "Invalid value for '--number'" in result.output
    assert result.exit_code != 0
    
    os.remove('in.txt')
    
def test_main_with_invalid_input_file(runner):
    invalid_input_file = 'in.doc'
    
    result = runner.invoke(main, ['--number', '5', '--output', 'out.txt', invalid_input_file])
    
    assert "Invalid value for 'INPUT_PATHS...'" in result.output
    assert result.exit_code != 0

def test_main_with_invalid_output_extension(runner):
    create_dummy_input_file('in.txt', 'dog, dog, cat, duck')
    
    result = runner.invoke(main, ['--number', '5', '--output', 'out.doc', 'in.txt'])

    assert "Output file out.doc has an invalid format" in result.output
    assert result.exit_code != 0

    os.remove('in.txt')