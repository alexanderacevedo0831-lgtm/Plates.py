import validators

# Prompts user for an email address and validates it
# Prints "Valid" if the email is valid, otherwise prints "Invalid"
# Only if the input is syntactically valid according to common email format rules
def main():
    email = input("Email: ").strip()
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()