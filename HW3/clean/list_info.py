"""
Glen Ernstrom
CS 1210
July 21, 2026
"""

DATA = [11, 8, 19, 16, 3, 17, 6, 12, 16, 1, 14, 7, 12, 6, 2, 5, 16, 14, 16, 18]


def mean(x):
    return sum(x) / len(x)


if __name__ == "__main__":
    index_input = int(input("Enter an index from 0 to 19 (inclusive): "))
    if index_input in range(0, len(DATA)):
        print(f"The element at index {index_input} is {DATA[index_input]}.")
        print(f"The sum of the elements in DATA is {sum(DATA)}.")
        print(f"The largest value in DATA is {max(DATA)}.")
        print(f"The smallest value in DATA is {min(DATA)}.")
        print(f"DATA has {len(DATA)} elements.")
        print(f"The mean of elements in DATA is {mean(DATA):.2f}.")
    else:
        print("Invalid input.")
