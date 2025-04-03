# Standard library imports for testing and data manipulation
import unittest
import pandas as pd
import sys
import os

# Configure Python path to import from parent directory
# This allows the test to find the analyzer module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer.csv_analyzer import CsvAnalyzer

class TestCsvAnalyzer(unittest.TestCase):
    """
    Test suite for CsvAnalyzer class.
    Tests the data analysis functionality with sample data.
    """

    def setUp(self):
        """
        Initializes test environment before each test method.
        Creates a test DataFrame with:
        - Numeric column 'value' for statistical testing
        - Categorical column 'category' for non-numeric testing
        """
        self.analyzer = CsvAnalyzer()
        self.test_data = pd.DataFrame({
            'value': [10.5, 20.3, 15.7, 25.1, 30.0],
            'category': ['A', 'B', 'A', 'B', 'C']
        })

    def test_analyze_data(self):
        """
        Tests the main analyze_data method functionality.
        Verifies:
        1. Correct result structure (summary and statistics)
        2. Accurate row and column counts
        3. Statistical calculations (mean, median, min, max)
        4. Proper rounding of numerical values to 2 decimal places
        """
        result = self.analyzer.analyze_data(self.test_data)
        
        # Test basic structure
        self.assertIn('summary', result, "Result should contain 'summary'")
        self.assertIn('statistics', result, "Result should contain 'statistics'")
        
        # Test summary
        summary = result['summary']
        self.assertEqual(summary['rows'], 5, "Should have 5 rows")
        self.assertEqual(summary['columns'], 2, "Should have 2 columns")
        
        # Test statistics for numeric column
        stats = result['statistics'].get('value', {})
        self.assertIsNotNone(stats, "Should have statistics for 'value' column")
        
        # Test statistical values with proper rounding
        expected_stats = {
            'mean': 20.32,
            'median': 20.30,
            'min': 10.5,
            'max': 30.0
        }
        
        for stat_name, expected_value in expected_stats.items():
            self.assertIn(stat_name, stats, f"Should contain {stat_name}")
            self.assertAlmostEqual(
                stats[stat_name], 
                expected_value, 
                places=2, 
                msg=f"{stat_name} should be approximately {expected_value}"
            )

    def test_non_numeric_column(self):
        """
        Tests proper handling of non-numeric columns.
        Ensures that:
        1. Categorical columns are excluded from statistical analysis
        2. No errors occur when processing mixed data types
        """
        result = self.analyzer.analyze_data(self.test_data)
        self.assertNotIn('category', result['statistics'], 
                        "Non-numeric column should not be in statistics")

if __name__ == '__main__':
    unittest.main()