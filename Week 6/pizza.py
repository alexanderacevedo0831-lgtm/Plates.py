import sys
import os
import csv
from tabulate import tabulate


def main():
    # Must have exactly one argument command line
    if len(sys.argv) != 2:
        sys.exit("Too few/many command-line arguments")

    filename = sys.argv[1]

    # Must be a .csv file
    if not filename.lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    # File must exist
    if not os.path.exists(filename):
        sys.exit("File does not exist")

    # Read CSV into headers and table rows
    with open(filename) as f:
        reader = csv.DictReader(f)
        table = list(reader)
        if not table:
            sys.exit("CSV file is empty")
        headers ="keys"

        # Process the file
        print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()