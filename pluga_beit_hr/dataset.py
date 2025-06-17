import csv
from pathlib import Path
from typing import List, Dict

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
DEFAULT_FILE = DATA_DIR / 'sample.csv'
PEOPLE_FILE = DATA_DIR / 'people.csv'


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


def _ensure_people_file() -> None:
    """Create the people CSV file with headers if it does not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not PEOPLE_FILE.exists():
        with PEOPLE_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=["first_name", "last_name", "phone_number"]
            )
            writer.writeheader()


def load_people() -> List[Dict[str, str]]:
    """Return all people records from ``PEOPLE_FILE``."""
    _ensure_people_file()
    with PEOPLE_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def append_person(entry: Dict[str, str]) -> None:
    """Append a single person to ``PEOPLE_FILE``."""
    _ensure_people_file()
    file_exists = PEOPLE_FILE.exists()
    with PEOPLE_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["first_name", "last_name", "phone_number"]
        )
        if not file_exists or PEOPLE_FILE.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(entry)
