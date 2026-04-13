from cli.parser import get_args
from utils.logger import setup_logger
from utils.file_handler import validate_file
from core.cleaner import clean_data
from core.converter import convert_to_excel

import pandas as pd
import logging

def main():
    setup_logger()

    args = get_args()

    try:
        validate_file(args.input)

        logging.info("Reading CSV file...")
        df = pd.read_csv(args.input)

        logging.info("Cleaning data...")
        df = clean_data(df)

        logging.info("Converting to Excel...")
        convert_to_excel(df, args.output)

        logging.info("Conversion completed successfully!")

    except Exception as e:
        logging.error(f" Error: {e}")

if __name__ == "__main__":
    main()