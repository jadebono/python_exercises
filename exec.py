'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.  
Suppose the following input is supplied to the program: without,hello,bag,world  
Then, the output should be: bag,hello,without,world

Hints:

1. In case of input data being supplied to the question, it should be assumed to from input();
2. Add input validation to ensure that the supplied string is indeed a comma-separated sequence.
'''

# input validation 
def input_validation(inp):
    test = [i for i in inp]
    comma = False
    for i in test:
        if i == ",":
            comma = True
    return comma
    

# input
def get_input():
    flag = False
    while (not flag):
        inp = input("Please input a sequence of strings separated by comma:\t")
        flag = input_validation(inp)
        if (not flag):
            print("This is not a comma-separated sequence! Please try again.")
    return inp
    
    
if __name__ == "__main__":
    inp = [i for i in get_input().split(",")]
    # note: .sort() sorts the old array in place without returning a new value. Use sorted to return a new sorted array
    inp.sort()
    print(",".join(inp))
    
    
    
    
    
        
            
    
    

