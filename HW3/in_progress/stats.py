"""
Glen Ernstrom
CS 1210
July 21, 2026
"""


# def mean(x):
#    return sum(x) / len(x)
    
# def std_dev(x):


# first focusing on getting input we can do stuff with

if __name__ == "__main__":
    
    
    prompt = input("Enter a real number or q to end data entry: ")

    user_list = []
        
    if prompt == 'q':
        print("No Data")
    else:
        user_list.append(prompt)
        while 'q' not in user_list:
            prompt = input("Enter a real number or q to end data entry: ")
            user_list.append(prompt)
       
    # now that we have number_list, let's get rid of the 'q'
    
    numstr_list = user_list[0:-1] # from index 0 up to but not including last element
    
    print(user_list) # here just for testing
    print(numstr_list)
    
    # Ok, we have a list, numstr_list of user input numbers as strings ...
    
    
    # attempting to get the number string sequence into numbers we can compute, trying
    # to model basketball.py but my gut is telling me I'm going down a rabbit hole
    
    # for num in numstr_list:
       # num_list = numstr_list.replace("'", ' ')
    

    


        
        
    

    
    
        