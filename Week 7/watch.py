import re
import sys


def main():
    print(parse(input("HTML: ")))

# Extracts any Youtube URL that's the value of a src attribute of an iframe element
def parse(s):
    pattern = re.compile(r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"')
    match = pattern.search(s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}" # Return shortened, shareable youtube.be URL as a string
    return None


if __name__ == "__main__":
    main()