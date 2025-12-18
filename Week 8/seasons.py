from datetime import date
import sys

# Prompt the user to enter their date of birth in the format YYYY-MM-DD format
# Prints how old they are in minutes, rounded to the nearest integer
# Using English words instead of numerals, without any "and" between words 
# Assume the user was born at midnight (00:00:00) on their date of birth
# Example: "Five hundred twenty-five thousand, six hundred minutes"

def main():
        # Prompt the user for their date of birth
        dob_str = input("Date of Birth (YYYY-MM-DD): ")
        try:
            dob = date.fromisoformat(dob_str)
        except ValueError:
            sys.exit(1)

        # Calculate the age in minutes
        today = date.today()
        age_in_days = (today - dob).days
        age_in_minutes = age_in_days * 24 * 60

        # Convert the age in minutes to words
        age_in_minutes_words = number_to_words(age_in_minutes) + " minutes"

        # Print the result
        final = age_in_minutes_words.capitalize()
        print(final)


def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def three_digit_to_words(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ("-" + units[n % 10] if n % 10 != 0 else "")
        else:
            return units[n // 100] + " hundred" + (" " + three_digit_to_words(n % 100) if n % 100 != 0 else "")

    if num == 0:
        return "zero"

    words = []
    for i in range(len(thousands)):
        if num % 1000 != 0:
            words.append(three_digit_to_words(num % 1000) + " " + thousands[i])
        num //= 1000

    return ", ".join(reversed(words)).strip()


if __name__ == "__main__":
    main()