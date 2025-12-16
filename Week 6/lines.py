import sys
import os

def main():
    # Must have exactly one argument command line
    if len(sys.argv) != 2:
        sys.exit("Too few/many command-line arguments")

    filename = sys.argv[1]

    # Must be a .py file
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Process the file
    print(count_lines(filename))

def count_lines(filename):
    count = 0

    with open(filename) as f:
        for line in f:
            # Ignore blank lines and comments
            stripped = line.strip()

            # Skip blank lines and comments
            if stripped == "" or stripped.startswith("#"):
                continue

            # Otherwise it's code is to be counted
            count += 1

    return count

if __name__ == "__main__":
    main()






