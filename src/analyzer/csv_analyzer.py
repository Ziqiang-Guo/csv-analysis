# filepath: /csv-analysis/csv-analysis/src/analyzer/csv_analyzer.py

import pandas as pd
import numpy as np

class CsvAnalyzer:
    def __init__(self):
        self.data = None

    def load_csv(self, file_path):
        """Load a CSV file into a DataFrame."""
        self.data = pd.read_csv(file_path)

    def analyze_data(self, data):
        """
        Analyze the CSV data
        Args:
            data: pandas.DataFrame containing the CSV data
        Returns:
            dict: Analysis results
        """
        try:
            analysis = {
                'summary': {
                    'rows': len(data),
                    'columns': len(data.columns),
                    'column_names': list(data.columns)
                },
                'statistics': {}
            }
            
            numeric_data = data.select_dtypes(include=[np.number])
            for column in numeric_data.columns:
                stats = data[column].describe()
                analysis['statistics'][column] = {
                    'mean': float(stats['mean']),
                    'std': float(stats['std']),
                    'min': float(stats['min']),
                    'max': float(stats['max']),
                    'median': float(data[column].median()),  # Adding median calculation
                    'min_high_difference': float(stats['max']) - float(stats['min'])
                }
            
            return analysis
        except Exception as e:
            return {'error': str(e)}

    def generate_report(self, analysis_results):
        """Generate a report based on the analysis results."""
        report = "Analysis Report:\n"
        for key, value in analysis_results.items():
            report += f"{key}: {value}\n"
        return report