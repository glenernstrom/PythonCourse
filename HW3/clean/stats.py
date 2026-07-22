"""
Glen Ernstrom
CS 1210
July 21, 2026

formatting reviewed and checked by
running ruff (0.15.20) at the command line,
reviewing any errors in vim, then running
ruff format *.py prior to submission

"""

import math


def mean(x):
    return sum(x) / len(x)


def std_dev(x):

    i = 0
    total = 0

    for __ in x:
        total = total + (x[i] - mean(x)) ** 2
        i = i + 1
    return math.sqrt(total)


if __name__ == "__main__":
    prompt = "Enter a real number or q to end data entry: "
    first_input = input(prompt)

    user_list = []

    if first_input == "q":
        print("No Data")
    else:
        user_list.append(first_input)
        while "q" not in user_list:
            user_input = input(prompt)
            user_list.append(user_input)

    numstr_list = user_list[0:-1]

    i = 0
    numlist = []

    for num in numstr_list:
        f = float(numstr_list[i])
        numlist.append(f)
        i = i + 1

    print(
        f"The mean is {mean(numlist):.2f} and the "
        f"standard deviation is {std_dev(numlist):.2f}."
    )
