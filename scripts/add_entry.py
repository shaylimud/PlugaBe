#!/usr/bin/env python3
"""Command-line utility to append an entry to the dataset."""
import argparse
from pluga_beit_hr.dataset import append_entry


def main() -> None:
    parser = argparse.ArgumentParser(description="Add an entry to the dataset")
    parser.add_argument("id", help="Unique identifier")
    parser.add_argument("name", help="Employee name")
    parser.add_argument("department", help="Department name")
    args = parser.parse_args()
    append_entry({"id": args.id, "name": args.name, "department": args.department})
    print("Entry added.")


if __name__ == "__main__":
    main()
