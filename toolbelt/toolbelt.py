# === TOOL FUNCTIONS ===

def indoor_voice():
    while True:
        user_input = input("\n[Indoor Voice] Type something (or 'back'): ").strip()
        if user_input.lower() == "back":
            break
        else:
            print(user_input.lower())


def playback():
    while True:
        user_input = input("\n[Playback] Say something (or 'back'): ").strip()
        if user_input.lower() == "back":
            break
        else:
            print(user_input.replace(" ", "..."))


def faces():
    while True:
        user_input = input("\n[Faces] Say something (or 'back'): ").strip()
        if user_input.lower() == "back":
            break
        else:
            text = user_input.replace(":)", "🙂").replace(":(", "🙁")
            print(text)


def tip_calculator():
    while True:
        dollars = input("\n[Tip Calculator] Meal cost (or 'back'): ").strip().lower()
        if dollars == "back":
            break
        percent = input("Tip percentage: ").strip().lower()
        try:
            dollars = float(dollars.replace("$", ""))
            percent = float(percent.replace("%", "")) / 100
            tip = dollars * percent
            print(f"Leave ${tip:.2f}")
        except ValueError:
            print("[Tip Calculator] Invalid input, try again.")


def deep_thought():
    while True:
        answer = input("\n[Deep Thought] What is the answer? (or 'back'): ").strip().lower()
        if answer == "back":
            break
        elif answer in ["42", "forty-two", "forty two"]:
            print("Yes")
        else:
            print("No")


def bank():
    while True:
        greeting = input("\n[Bank Greeting] Greeting (or 'back'): ").strip().lower()
        if greeting == "back":
            break
        elif greeting.startswith("hello"):
            print("$0")
        elif greeting.startswith("h"):
            print("$20")
        else:
            print("$100")


def extension_checker():
    while True:
        filename = input("\n[Extension Checker] File name (or 'back'): ").strip().lower()
        if filename == "back":
            break
        if filename.endswith(".gif"):
            print("image/gif")
        elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
            print("image/jpeg")
        elif filename.endswith(".png"):
            print("image/png")
        elif filename.endswith(".pdf"):
            print("application/pdf")
        elif filename.endswith(".txt"):
            print("text/plain")
        elif filename.endswith(".zip"):
            print("application/zip")
        else:
            print("application/octet-stream")


# === MAIN MENU ===

def main():
    tools = {
        "1": indoor_voice,
        "2": playback,
        "3": faces,
        "4": tip_calculator,
        "5": deep_thought,
        "6": bank,
        "7": extension_checker,
    }

    while True:
        print("\n=== TOOLBELT MENU ===")
        print("1. Indoor Voice")
        print("2. Playback")
        print("3. Faces")
        print("4. Tip Calculator")
        print("5. Deep Thought")
        print("6. Bank Greeting")
        print("7. File Extension Checker")
        print("8. Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice in tools:
            tools[choice]()  # Run the chosen tool
        elif choice in ["8", "exit"]:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
