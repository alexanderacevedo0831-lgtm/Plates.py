def main():
    menu = {
        "Burrito": 7.50,
        "Taco": 3.00,
        "Quesadilla": 8.50,
        "Nachos": 11.00,
        "Bowl": 8.50,
        "Baja Taco": 4.25,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Tortilla Salad": 8.00
    }

    total = 0.0

    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            break

if __name__ == "__main__":
    main()
