"""
Glen Ernstrom
CS 1210
July 27, 2026

Finds prime numbers.
"""

import math

def prime_test(n):
    for div in range(2, int(math.sqrt(n))+1):
        if n % div == 0:
            return False
    return True
    
   
if __name__ == '__main__':
    while True:
        user_int = int(input("Enter an integer > 1: "))
        if user_int > 1:
            break
        print("Invalid input.")
        
    prime_test(user_int)
    
    if prime_test(user_int) == True:
        print(f"{user_int} is prime.")
    else:
        print(f"{user_int} is not prime.")
    
                   

