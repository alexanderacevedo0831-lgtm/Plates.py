def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "sweet cherries": 100,
        "strawberries": 50,
        "tangerine": 50,
        "watermelon": 80
    }

    fruit = input("Item: ").strip().lower()

    # Next check if the fruit is in the dictionary and print calories
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
    

if __name__ == "__main__":
    main()