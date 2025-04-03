# csv-analysis/csv-analysis/README.md

# CSV Analysis Tool

A simple web application that helps you analyze CSV (spreadsheet) files. Upload your CSV file and get instant statistical analysis!

## What Does It Do?

- Upload any CSV file through a web browser
- Get instant analysis of your data
- View statistics like averages, minimum/maximum values, and more
- No coding knowledge required!

## Getting Started

### Prerequisites
- Python 3.7 or higher (Download from [Python.org](https://www.python.org/downloads/))
- A web browser (Chrome, Firefox, Safari, etc.)

### Installation Steps

1. Download this project to your computer

2. Open Terminal (On Mac: press Cmd + Space, type "Terminal", press Enter)

3. Navigate to the project folder:
```bash
cd path/to/csv-analysis
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the application:
```bash
python src/main.py
```

2. Open your web browser and go to:
```
http://localhost:8080
```

3. You should see a simple webpage with a "Choose File" button

### How to Use

1. Click the "Choose File" button
2. Select any CSV file from your computer
3. Click "Analyze"
4. View your results!

### Example Results
You'll see information like:
- Number of rows and columns
- Average values
- Minimum and maximum values
- And more!

### Common Issues

**Problem**: "Address already in use" error  
**Solution**: Try these commands in Terminal:
```bash
lsof -i :8080
kill -9 <PID>  # Replace <PID> with the number you see from above command
```

**Problem**: Can't find your CSV file  
**Solution**: Make sure your file ends with `.csv`

## Need Help?

If you run into any problems:
1. Make sure Python is installed
2. Check that you're in the right folder
3. Ensure your CSV file is properly formatted

## For Developers

If you want to modify the code:
- Main application code is in `src/main.py`
- Analysis logic is in `src/analyzer/csv_analyzer.py`
- File handling is in `src/utils/file_handler.py`

## Adding New Analytics Features

### Quick Start for Developers

1. Open the analyzer file:
```bash
code src/analyzer/csv_analyzer.py
```

2. Add your new analysis method to the `CsvAnalyzer` class:
```python
def analyze_new_feature(self, data):
    """
    Add your new analysis function here
    Args:
        data: pandas DataFrame containing the CSV data
    Returns:
        dict: Analysis results
    """
    return {
        'your_metric': your_calculation
    }
```

3. Update the main analysis method:
```python
def analyze_data(self, data):
    try:
        # Existing analysis
        basic_stats = self.get_basic_stats(data)
        
        # Add your new analysis
        new_stats = self.analyze_new_feature(data)
        
        # Combine results
        return {
            **basic_stats,
            **new_stats
        }
    except Exception as e:
        return {'error': str(e)}
```

### Example: Adding Correlation Analysis

```python
def analyze_correlations(self, data):
    """Calculate correlations between numeric columns"""
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    correlations = numeric_data.corr().round(2).to_dict()
    return {
        'correlations': correlations
    }
```

### Testing Your Changes

1. Create a test file:
```bash
code src/tests/test_analyzer.py
```

2. Add test cases:
```python
def test_new_feature():
    analyzer = CsvAnalyzer()
    test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = analyzer.analyze_new_feature(test_data)
    assert 'your_metric' in result
```

3. Run tests:
```bash
python -m pytest src/tests/
```

For more information, check out the [pandas documentation](https://pandas.pydata.org/docs/user_guide/index.html) for data analysis functions.

## License

Free to use for everyone!