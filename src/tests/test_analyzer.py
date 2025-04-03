import unittest
from analyzer.csv_analyzer import CsvAnalyzer

class TestCsvAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = CsvAnalyzer()

    def test_load_csv(self):
        # Test loading a CSV file
        data = self.analyzer.load_csv('test.csv')
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)

    def test_analyze_data(self):
        # Test analyzing data
        self.analyzer.load_csv('test.csv')
        result = self.analyzer.analyze_data()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    def test_generate_report(self):
        # Test generating a report
        self.analyzer.load_csv('test.csv')
        self.analyzer.analyze_data()
        report = self.analyzer.generate_report()
        self.assertIsNotNone(report)
        self.assertIn('summary', report)

if __name__ == '__main__':
    unittest.main()