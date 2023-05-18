'''

Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

1. C = 50;
1. H = 30;
1. D is the variable whose values should be input to your program in a comma-separated sequence, ex: 100,150,180.

Example:

Let us assume the following comma separated input sequence is given to the program: 100,150,180

The output of the program should be: 18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26). In case of input data being supplied to the question, it should be assumed to be from input().
'''

'''
def validate_csv(csv):
    tokens = [i for i in csv.split(",")]
    for elem in tokens:
        try: 
            int(elem)
        except Exception: 
            return False
    return True
    
    
    
    
if __name__ == "__main__":
    a = "1,2,3,4,5"
    b = "1,2.3,3,4,5"
    c = "1.2#3^5"
    d = "Hello world"
    print(validate_csv(a))
    print(validate_csv(b))
    print(validate_csv(c))
    print(validate_csv(d))
    

#     import math

# # Fixed values
# C = 50
# H = 30

# # Function to validate if input string can be converted to integer
# def is_integer(n):
#     try:
#         int(n)
#         return True
#     except ValueError:
#         return False

# # Get and validate user input
# user_input = input("Enter values of D in a comma-separated sequence: ").split(',')

# # Initialize an empty list to store the results
# results = []

# # Loop through the values provided by the user
# for D_str in user_input:
#     # Validate that D can be converted to an integer
#     if is_integer(D_str):
#         D = int(D_str)
#         # Calculate Q using the provided formula and round the result to the nearest integer
#         Q = round(math.sqrt((2 * C * D) / H))
#         results.append(Q)
#     else:
#         print(f"Invalid input: {D_str}. Skipping this value.")

# # Print the results
# print(",".join(map(str, results)))
'''

import greek

def count_numbers(n):
    return [i for i in range(1, n+1)]


if __name__ == "__main__":
    n = 10000
    print(count_numbers(n))



















