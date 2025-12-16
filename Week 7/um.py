import re
import sys

def main():
    print(count(input("Text: ")))
    if not count:
        sys.exit(1)

# Checks for "um" in a sentence, case-insensitively and counts as 1 only when it appears as a word onto itself
# Hello, um, how are you?  --> 1
# Yummy food! --> 0
# Find all "um" as words and return the count as an integer
def count(s):
    matches = re.findall(r"\b(um)\b", s, re.IGNORECASE)

    # return the number of matches found
    return len(matches)


if __name__ == "__main__":
    main()