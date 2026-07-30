"""
Glen Ernstrom
CS 1210
"""

import csv

if __name__ == "__main__":
    population = 0
    income = 0
    data = []

    state = input("Enter name of state: ").lower()
    filename = state.replace(" ", "_") + ".csv"
    with open(filename, 'r', newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data.append([row[0], int(row[1]), int(row[4])])

        county_pop = []
        i = 0
        for _ in data:
            county_pop.append(data[i][2])
            population = sum(county_pop)
            i += 1
        
        county_percap = []
        i = 0
        for _ in data:
            county_percap.append(data[i][1])
            income = sum(county_percap)
            i += 1
                        
        state_percap = income / len(county_percap)
        
        above_avg = []
        i = 0
        for _ in data:
            county = data[i][0]
            county_income = data[i][1]
            if county_income > state_percap:
                above_avg.append(county)
            i += 1

        print(f"The population of {state.title()} is {population:,}.")
        print(f"{state.title()} per capita income is ${state_percap:,.2f}.")
        print("Counties with higher than average per capita income:")
        for county in above_avg:
            print(f"{county}")

