"""
Glen Ernstrom
CS 1210
July 21, 2026
"""

if __name__ == "__main__":
    sentence = str(input("Gimme a string: "))

    lst = sentence.split()
    while lst:
        print(lst.pop(0))
