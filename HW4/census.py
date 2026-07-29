"""
Your name here
CS 1210
"""
import csv


if __name__ == '__main__':
    population = 0
    income = 0
    data = []

    state = input("Enter name of state: ").lower()
    filename = state.replace(" ", "_") + ".csv"

    # Complete this program...
    # Open the file for reading using a context manager
    #     Instantiate a CSV reader
    #     Use next() to skip the column headings
    #     Read data and perform calculations as needed
    # Perform additional calculations as needed
    # Use the string method .title() to convert input string to proper case
    # Print the following
    #     Population of state
    #     Per capita income for state
    #     Counties with higher than average per capita income

