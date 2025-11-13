import random

def main():
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) > 0:
            level = int(level)
            break

    number = random.randint(1, level)

    while True:
        guess_str = input("Guess: ")

        if not guess_str.isdigit():
            continue

        guess = int(guess_str)

        if guess <= 0:
            continue

        if guess < number:
            print("Too ")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()