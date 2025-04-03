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
            # Basic statistics
            stats = data.describe(include='all')
            
            # Convert to JSON serializable format
            analysis = {
                'summary': {
                    'rows': len(data),
                    'columns': len(data.columns),
                    'column_names': list(data.columns)
                },
                'statistics': {
                    col: {
                        'count': int(stats[col]['count']) if not pd.isna(stats[col]['count']) else 0,
                        'mean': float(stats[col]['mean']) if 'mean' in stats[col] and not pd.isna(stats[col]['mean']) else None,
                        'std': float(stats[col]['std']) if 'std' in stats[col] and not pd.isna(stats[col]['std']) else None,
                        'min': float(stats[col]['min']) if 'min' in stats[col] and not pd.isna(stats[col]['min']) else None,
                        'max': float(stats[col]['max']) if 'max' in stats[col] and not pd.isna(stats[col]['max']) else None,
                        'median': float(data['Salary'].median()) if 'Salary' in data.columns else None,
                    }
                    for col in data.select_dtypes(include=np.number).columns
                }
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