def convert(text):
    # Replace emoticons with emoji
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt user for input
    user_input = input("Enter text: ")
    # Call convert and print result
    print(convert(user_input))

# Run main when program is executed
if __name__ == "__main__":
    main()