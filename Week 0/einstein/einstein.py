def main():
    # Prompt user for mass
    mass = int(input("Mass in kilograms: "))

    # Speed of Light (c)
    c = 300000000

    # Energy calculation
    energy = mass * (c ** 2)

    # Print result as interger
    print(energy)

if __name__ == "__main__":
    main()