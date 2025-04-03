# src/utils/file_handler.py

import os
import pandas as pd
import io

def save_file(file_path, data):
    """Saves the given data to a specified file path."""
    with open(file_path, 'w', newline='') as file:
        file.write(data)

def read_file(file):
    """
    Read a CSV file from a FileStorage object
    Args:
        file: FileStorage object from Flask request
    Returns:
        pandas.DataFrame: DataFrame containing the CSV data
    """
    try:
        content = file.read().decode('utf-8')
        string_io = io.StringIO(content)
        df = pd.read_csv(string_io)
        return df
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {str(e)}")