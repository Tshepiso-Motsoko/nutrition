def main():
    # Create a dictionary where key is the fruit name and value is the calories for that fruit
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 105,
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
        "plum": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Ask user for the fruit name
    fruit = input("Item: ").lower()

    # Check if the fruit is in the dictionary
    if fruit in fruits:
        # If yes, print its calories
        print("Calories:", fruits[fruit])

main()
