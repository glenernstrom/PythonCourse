"""
Simulate repeated rolling of two dice
"""

import random

PIPS = [1, 2, 3, 4, 5, 6]
if __name__ == '__main__':
    
    while True:
        response = input("Roll? or quit? Enter return to roll or q to quit.").lower()
        if response == 'q':
            print("Goodbye")
            break
        roll = random.choice(PIPS), random.choice(PIPS)
        points = sum(roll)
        print(points)
        if points == 7:
            print("You win!")
        elif points == 2:
            print("Snake eyes!")
        elif points == 12:
            print("Boxcars!")

