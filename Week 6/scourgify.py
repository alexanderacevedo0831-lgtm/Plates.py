import sys
import os
import csv

def main():
    # Must have exactly two command line arguments
    if len(sys.argv) != 3: 
        sys.exit("Too few command-line arguments")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # Infile must be a .csv file
    if not infile.lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    # Infile must exist
    if not os.path.exists(infile):
        sys.exit("File does not exist")

    # Read CSV file as input, whose columns are in order, name and house
    with open(infile) as f:
        reader = csv.DictReader(f)
        table = list(reader)
        if not table:
            sys.exit()

    # Write CSV file as output, whose columns are in order, first, last, and house
    with open(outfile, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in table:
            name = row["name"].split(", ")
            writer.writerow({"first": name[1], "last": name[0], "house": row["house"]})

if __name__ == "__main__":
    main()
