from pyfiglet import Figlet # pyright: ignore[reportMissingImports]
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Check commnand-line arguments
    if len(sys.argv) == 1:
        # no args -> random font
        font = random.choice(fonts)
        figlet.setFont(font=font)

    elif len(sys.argv) == 3 and sys.argv[1] == "-f" and sys.argv[2] in fonts:
        # valid args: -f
        figlet.setFont(font=sys.argv[2])

    else:
        # invalid args
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()