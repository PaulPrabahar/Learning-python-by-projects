# Use random function to get random values
# Define function to roll the dice
# Create a dictionary that will have the drawings of the dice

import random

dice_diagram = {
    1: '''
    ┌───────┐
    │       │
    │   ●   │
    │       │
    └───────┘
    ''',
    2: '''
    ┌───────┐
    │ ●     │
    │       │
    │     ● │
    └───────┘
    ''',
    3: '''
    ┌───────┐
    │ ●     │
    │   ●   │
    │     ● │
    └───────┘
    ''',
    4: '''
    ┌───────┐
    │ ●   ● │
    │       │
    │ ●   ● │
    └───────┘
    ''',
    5: '''
    ┌───────┐
    │ ●   ● │
    │   ●   │
    │ ●   ● │
    └───────┘
    ''',
    6: '''
    ┌───────┐
    │ ●   ● │
    │ ●   ● │
    │ ●   ● │
    └───────┘
    '''
}


def dice_roll(dice_diagram):

    roll = input("roll dice yes or no : ")

    while roll.lower() == "yes".lower():

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled : {} and {} ".format(dice1, dice2))
        print(dice_diagram[dice1])
        print(dice_diagram[dice2])

        roll = input("Roll again? (yes/no) : ")


dice_roll(dice_diagram)
