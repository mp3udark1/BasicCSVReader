# BasicCSVReader - Main Script
# Reads CSV and shows stats/preview
# Run with: python reader.py

import csv
import sys
import os

def read_csv(filename):
    """Read CSV file and return data, headers, stats."""
    if not os.path.exists(filename):
        print("File not found.")
        return None, None, 0, 0
    
    data = []
    headers = None
    row_count = 0
    col_count = 0
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)  # First row as headers
            if headers:
                col_count = len(headers)
            
            for row in reader:
                data.append(row)
                row_count += 1
                if row:
                    col_count = max(col_count, len(row))
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, 0, 0
    
    return data, headers, row_count, col_count

def show_stats(row_count, col_count):
    """Display basic stats."""
    print(f"File has {row_count} data rows and {col_count} columns.")
    if row_count > 0:
        print("Preview of first 3 rows (excluding header):")
        print("-" * 40)
    else:
        print("No data rows found.")

def preview_data(data, limit=3):
    """Show preview of data."""
    for i in range(min(limit, len(data))):
        print(f"Row {i+1}: {data[i]}")

def main():
    """Main function."""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter CSV file path: ").strip()
    
    if not filename:
        print("No file provided.")
        return
    
    data, headers, rows, cols = read_csv(filename)
    
    if data is not None:
        if headers:
            print(f"Headers: {headers}")
        show_stats(rows, cols)
        preview_data(data)
    else:
        print("Could not read the file.")

if __name__ == "__main__":
    main()