"""
Gambler's ruin
"""

import random

def ruin(balance):
    n = 0
    while balance != 0:
        balance = balance + random.choice([-1, 1])
        n = n + 1
    return n


def mean(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    
    while True:
        start =  int(input("Enter a starting balance ($): "))
        if start > 0:
            break
    
    trials = []
    for _ in range(10):
        trials.append(ruin(start))
        
    print(f"We started with ${start:,}")
    print(f"On average it took {mean(trials):,.2f} coin tosses to go broke.")
    print(f"The longest run was  {max(trials):,}.")
    print(f"The shortest run was {min(trials):,} coin tosses.")