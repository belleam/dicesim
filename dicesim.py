## Generate the first dice role with a random integer

import random
dice_1 = random.randint(1,6)
print(f"You rolled a {dice_1}!")

## While loop generates a second dice roll depending on user's input

second_roll = input(f"Would you like to roll again? Yes or no?")
while second_roll.lower() == "yes":
    dice_2 = random.randint(1,6)
    print(f"You rolled a {dice_2}!")
    break
else:
    print(f"You have decided not to roll again.")