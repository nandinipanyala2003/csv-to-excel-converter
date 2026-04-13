import os

def validate_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")