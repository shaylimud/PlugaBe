import csv
from pathlib import Path
from typing import List, Dict

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
DEFAULT_FILE = DATA_DIR / 'sample.csv'


def load_dataset(path: Path = DEFAULT_FILE) -> List[Dict[str, str]]:
    """Load data from a CSV file."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset file {path} does not exist")
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def append_entry(entry: Dict[str, str], path: Path = DEFAULT_FILE) -> None:
    """Append a new entry to the dataset."""
    file_exists = path.exists()
    with path.open('a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'department'])
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)
