import os
import sys
import csv
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pluga_beit_hr import dataset


def setup_temp(monkeypatch):
    tmp = TemporaryDirectory()
    tmp_path = Path(tmp.name)
    monkeypatch.setattr(dataset, "DATA_DIR", tmp_path)
    monkeypatch.setattr(dataset, "DEFAULT_FILE", tmp_path / "sample.csv")
    monkeypatch.setattr(dataset, "PEOPLE_FILE", tmp_path / "people.csv")
    return tmp


def test_load_and_append_dataset(monkeypatch):
    tmp = setup_temp(monkeypatch)
    try:
        # prepare initial CSV for dataset
        dataset.DATA_DIR.mkdir(parents=True, exist_ok=True)
        with dataset.DEFAULT_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "department"])
            writer.writeheader()
            writer.writerow({"id": "1", "name": "Alice", "department": "Engineering"})

        data = dataset.load_dataset(path=dataset.DEFAULT_FILE)
        assert data == [{"id": "1", "name": "Alice", "department": "Engineering"}]

        dataset.append_entry({"id": "2", "name": "Bob", "department": "Sales"}, path=dataset.DEFAULT_FILE)
        data = dataset.load_dataset(path=dataset.DEFAULT_FILE)
        assert len(data) == 2
        assert data[1]["name"] == "Bob"
    finally:
        tmp.cleanup()


def test_load_and_append_people(monkeypatch):
    tmp = setup_temp(monkeypatch)
    try:
        # initially file does not exist; load_people should create it with header
        people = dataset.load_people()
        assert people == []

        dataset.append_person({
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "123",
        })
        dataset.append_person({
            "first_name": "Jane",
            "last_name": "Smith",
            "phone_number": "456",
        })
        people = dataset.load_people()
        assert len(people) == 2
        assert people[0]["first_name"] == "John"
        assert people[1]["first_name"] == "Jane"
    finally:
        tmp.cleanup()

