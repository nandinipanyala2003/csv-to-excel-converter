import argparse

def get_args():
    parser = argparse.ArgumentParser(description="CSV to Excel Converter")

    parser.add_argument("--input", required=True, help="Input CSV file path")
    parser.add_argument("--output", required=True, help="Output Excel file path")

    return parser.parse_args()