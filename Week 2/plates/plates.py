def main():
    plates = input("Plate: ").strip()
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")
    
def is_valid(s):
    if not isinstance(s, str):
        return "False"

    if not starts_with_two_letters(s):
        return False
    
    if not length_is_valid(s):
        return False
    
    if not numbers_at_end(s):
        return False
    
    if not no_punctuation(s):
        return False
    
    return True

# Requirement 1: Must start with at least two letters
def starts_with_two_letters(s):
    return len(s) >= 2 and s[:2].isalpha()

# Requirement 2: Must be between 2 and 6 characters long
def length_is_valid(s):
    return 2 <= len(s) <= 6

# Requirement 3: Numbers, if any, must be at the end
def numbers_at_end(s):
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
            # first number cannot be '0'
                if char == '0':
                    return False
            # everything after the first number must be a number
            number_started = True
        else:
            if number_started:
                return False
    return True

# Requirement 4: No periods, spaces, or punctuation marks
def no_punctuation(s):
    return s.isalnum()

if __name__ == "__main__":
    main()