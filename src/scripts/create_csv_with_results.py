#!/usr/bin/env python3
from src.db.db_interaction import handle_database_interaction
from src.db.querys import SELECT_RESULTS
import csv


def write_csv():
    rows = handle_database_interaction(SELECT_RESULTS)
    try:
        with open("results.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["URL", "Processing Time", "Links Count", "Path"])
            writer.writerows(rows)
    except TypeError:
        print("Table is emp")


def main():
    write_csv()


if __name__ == "__main__":
    main()
