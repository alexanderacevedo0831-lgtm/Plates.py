def main():
    while True:
        fraction = input("Fraction: ")
        if convert(fraction):
            break

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        # Reject division by zero
        if y == 0:
            return False

        value = x / y

        # Reject negatives or fractions greater than 1
        if value < 0 or value > 1:
            return False
        
        gauge(value)
        return True
        
    except (ValueError, ZeroDivisionError):
        return False

def gauge(percentage):
    percentage = round(percentage * 100)

    # Handle edge cases explicitly
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
    