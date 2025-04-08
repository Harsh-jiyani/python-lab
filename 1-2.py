import random
roll = input("Roll the dice? (y/n): ")
if roll.lower() == 'y':
    print("You rolled:", random.randint(1, 6))
