import random


def roll_dice():
    dice_drawing = {
        1: (
            "-------",
            "|     |",
            "|  o  |",
            "|     |",
            "-------",
        ),
        2: (
            "-------",
            "|o    |",
            "|     |",
            "|    o|",
            "-------",
        ),
        3: (
            "-------",
            "|o    |",
            "|  o  |",
            "|    o|",
            "-------",
        ),
        4: (
            "-------",
            "|o   o|",
            "|     |",
            "|o   o|",
            "-------",
        ),
        5: (
            "-------",
            "|o   o|",
            "|  o  |",
            "|o   o|",
            "-------",
        ),
        6: (
            "-------",
            "|o   o|",
            "|o   o|",
            "|o   o|",
            "-------",
        ),

    }
    print("Roll higher than the computer to win")
    roll = input("Play game?(y/n): ")
    while roll.lower() == "y":
        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print("You rolled: {}, Computer rolled: {}".format(player_roll, computer_roll))
        print("\n".join(dice_drawing[player_roll]))
        print("\n".join(dice_drawing[computer_roll]))
        if player_roll > computer_roll:
            print("You win")
        elif computer_roll > player_roll:
            print("Computer wins")
        else:
            print("It's a tie")

        roll = input('Roll again?(y/n): ')


roll_dice()
