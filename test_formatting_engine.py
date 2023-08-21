from formatting_engine import FileStats, TxtFormatter, CsvFormatter

class MockWordStat:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

class TestTxtFormatter:
    def test_txt_format_output(self):
        file_stats = FileStats("out1.txt", 22, [MockWordStat("a", 5), MockWordStat("b", 4), MockWordStat("c", 3), MockWordStat("d", 2), MockWordStat("kk", 2)])
        formatter = TxtFormatter()
        expected_output = "File out1.txt contains 22 words. Frequent words are: a (5), b (4), c (3), d (2), kk (2)\n"
        assert formatter.format_output(file_stats) == expected_output
        
    def test_txt_format_output_alt(self):
        file_stats = FileStats("out2.txt", 8, [MockWordStat("dog", 5), MockWordStat("cat", 2), MockWordStat("duck", 1)])
        formatter = TxtFormatter()
        expected_output = "File out2.txt contains 8 words. Frequent words are: dog (5), cat (2), duck (1)\n"
        assert formatter.format_output(file_stats) == expected_output

class TestCsvFormatter:
    def test_csv_format_output(self):
        file_stats = FileStats("out1.csv", 22, [MockWordStat("a", 5), MockWordStat("b", 4), MockWordStat("c", 3), MockWordStat("d", 2), MockWordStat("kk", 2)])
        formatter = CsvFormatter()
        expected_output = "out1.csv,22,a,5,b,4,c,3,d,2,kk,2\n"
        assert formatter.format_output(file_stats) == expected_output

    def test_csv_format_output_alt(self):
        file_stats = FileStats("out2.csv", 8, [MockWordStat("dog", 5), MockWordStat("cat", 2), MockWordStat("duck", 1)])
        formatter = CsvFormatter()
        expected_output = "out2.csv,8,dog,5,cat,2,duck,1\n"
        assert formatter.format_output(file_stats) == expected_output