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

import math

# validation of the csv string - obviously needed only if the csv comes from the user input
def validate_csv(csv):
    tokens = [i for i in csv.split(",")]
    for elem in tokens:
        # nested try-except block to test that tokens are either integers or decimals
        try:
            int(elem) 
        except Exception: 
            try:
                float(elem)
            except Exception:
                return False
    return True
        
# decimals are rounded using banker's rounding. To round up with 0.5 use the decimal module
def process_arr(csv):
    ans = []
    d_arr = []
    C = 50
    H = 30
    for elem in csv.split(","):
        # conditional to convert elem to int if it is a float
        if float(elem):
            d_arr.append(int(round(float(elem))))
        else:
            d_arr.append(int(elem))
    ans = [round(math.sqrt((2 * C * elem)/H)) for elem in d_arr]
    return ",".join([str(i) for i in ans])
    
    
if __name__ == "__main__":
    d_csv = "100.3,150,180"
    if validate_csv(d_csv):
        new_csv_a = process_arr(d_csv)
        print(new_csv_a)
            
    
    

