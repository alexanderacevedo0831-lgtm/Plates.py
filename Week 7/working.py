import re
import sys

def main():
        print(convert(input("Hours: ")))
        if not convert:
            sys.exit(1)

# Expects a string in any 12-hour format (e.g., "9 AM to 5 PM") and converts it to the corresponding 24-hour format (e.g., "09:00 to 17:00")
# AM/PM are capitalized and have a space before them
# Raises a ValueError if the input is invalid
# Assume that these times represent actual times, not neccessarily 9:00 AM and 5:00 PM specifically
# Don't assume someone's hours will start before noon and end after noon (e.g., "9 PM to 5 AM" is valid)
def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError

    return (
        f"{to_24(match.group(1), match.group(2), match.group(3))} to "
        f"{to_24(match.group(4), match.group(5), match.group(6))}"
    )

def to_24(hour, minute, period):
        hour = int(hour)

        # default minutes here
        if minute is None:
            minute = "00"

        minute = int(minute)
        if minute > 59:
            raise ValueError
        
        if hour < 1 or hour > 12:
            raise ValueError
        
        if period == "AM":
            if hour == 12:
                hour = 0
        
        else:
            if hour != 12:
                hour += 12
        
        return f"{hour:02}:{minute:02}"
    
if __name__ == "__main__":
    main()