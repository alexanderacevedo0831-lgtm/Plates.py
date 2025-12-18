import sys
import re

def validate(ip):
    # Match exactly 4 dot-separated groups of digits
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if not match:
        return False

    for part in match.groups():
        # No leading zeros unless the number is exactly "0"
        if part != "0" and part.startswith("0"):
            return False

        num = int(part)
        if num < 0 or num > 255:
            return False

    return True


def main():
    ip = input().strip()
    result = validate(ip)
    print(result)
    sys.exit(1)


if __name__ == "__main__":
    main()