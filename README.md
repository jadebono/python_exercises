# 100 Python Exercises

Adapted from the [Python Exercises of Jeffrey Hu](https://github.com/zhiwehu/Python-programming-exercises).
[Github: Jeffrey Hu](https://github.com/zhiwehu)

Adaptation by: [Joseph Anthony Debono](https://github.com/jadebono).
[Email Joseph](joe@jadebono.com)

---

## Question 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

Solution:

```py
def div_seven():
    x = []
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
         x.append(str(i))
    print(",".join(x))


def test():
    for i in range(1, 10):
        print(i)


if __name__ == "__main__":
    div_seven()
```

---

## Question 2

Write a program which can compute the factorial of a given numbers. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

Hints:

1. In case of input data being supplied to the question, take the input from the user using input();
1. Use a try-except block for input validation.

Solution:

```py
def test_int(n):
    try:
        int(n)
        return True
    except (ValueError, TypeError):
        return False


def get_val():
    user_input = input("Please input an integer. Note, any input that is not an integer will be discarded:\n")
    while (test_int(user_input) == False):
        user_input = input("Please input an integer. Note, any input that is not an integer will be discarded:\n")
    return int(user_input)


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


if __name__ == "__main__":
    n = get_val()
    print(fac(n))
```

---

## Question 3

With a given integral number n, write a program to generate an object that contains (i, i\*i) such that i is an integral number between 1 and n (both included). and then the program should print the object. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:

1. If the input data is to be supplied, let it supplied from input();
1. Use a try-except block for input validation.

Solution:

```py
# function to test that input is an integer
def test_int(n):
    try:
        int(n)
        return True
    except (ValueError, TypeError):
        return False


# function to get integer
def get_int():
    num = "x"
    while not test_int(num) or int(num) < 1:
        num = input("please enter an integer. Any other input will be discarded:\t")
    return int(num)


# function to create dictionary
def create_dic(i):
    return {i : i * i for i in range(1, i+1)}


if __name__ == "__main__":
    x = get_int()
    y = create_dic(x)
    print(y)
```

---

## Question 4

Write a program which takes a sequence of comma-separated numbers and generates an array and an object which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be: ['34', '67', '55', '33', '12', '98'] {'34':34, '67':67, '55':55, '33':33, '12':12, '98':98}

Hints:

1. If the input data is to be supplied, let it be supplied by the user using an input() function;
1. Add input validation.

Solution:

```py
# func to validate that CSV contains just ints and comma separators
def validate_csv(csv):
    for elem in csv:
        if not elem.isdigit() and elem not in {","}:
            return False
    return True


# func to create array
def create_array(csv):
    return csv.split(",")


# func to create dictionary
def create_dic(csv):
    csv_arr = csv.split(",")
    return {i: i for i in csv_arr}


# this func prompts the user to input a CSV, and uses a flag for the while loop
def inp_csv():
    x = False
    while not x:
        csv = input("Please input a sequence of integers separated only by a comma:\n")
        if validate_csv(csv):
            x = True
            return csv
        else:
            print("Invalid input!")


if __name__ == "__main__":
    csv = inp_csv()
    arr = create_array(csv)
    dic = create_dic(csv)
    print(arr, dic, sep='\n')
```

---

## Question 5

Define a class which has at least two methods:

1. getString: to get a string from console input.
1. printString: to print the string in upper case.

Also please include simple test function to test the class methods.

Hints:

1. Use \_\_init\_\_ method to construct some parameters.

Solution:

```py
class Twup:
    def __init__(self):
        self.name = "My name is twup"
        self.my_str = "No input yet"

    def get_string(self):
        self.my_str = input("Please input a string:\t")

    def print_string(self):
        print(self.my_str)


def run_class():
   myTwup = Twup()
   print(myTwup.name)
   myTwup.print_string()
   myTwup.get_string()
   myTwup.print_string()


if __name__ == "__main__":
    run_class()
```

---

## Question 6

Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

1. C = 50;
1. H = 30;
1. D is the variable whose values should be input to your program in a comma-separated sequence, ex: 100,150,180.

Example:

Let us assume the following comma separated input sequence is given to the program: 100,150,180

The output of the program should be: 18,22,24

Hints:

1. If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26). In case of input data being supplied to the question, it should be assumed to be from input().

```py
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
```

---

## Question 7

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i\*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1.

Example: Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:

1. Create an array;
1. The external loop (rows) should create an empty array for each of its iterations and push each array into the parent array;
1. The inner loop should multiply the current value of row with each of the values of cols and push each product into the current iteration of array[rows].

Solution:

```py
# input validation
def input_validation(i, j):
    return True if i.isdigit() and j.isdigit() and int(i) and int(j) and int(i) <= 10 and int(j) <= 10 else False


# input
def get_input():
    flag = False
    while (not flag):
        i = input("please input an integer to generate a 2D array. For the sake of this exercise, only integers between 1 and 10 will be accepted:\t")
        j = input("please input a 2nd integer to generate a 2d array. Only ints between 1 and 10 will be accepted:\t")
        flag = input_validation(i, j)
        if (not flag):
            print("One or more of your inputs are invalid! Please try again.")
    return int(i), int(j)


# array generator
def gen_arr(i, j):
    arr = []
    arr = [[i * j for j in range(0, j)] for i in range(0, i)]
    return arr


if __name__ == "__main__":
    i, j = get_input()
    twod_arr = gen_arr(i, j)
    print(twod_arr)

```

---

## Question 8

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.  
Suppose the following input is supplied to the program: without,hello,bag,world  
Then, the output should be: bag,hello,without,world

Hints:

1. In case of input data being supplied to the question, it should be assumed to from input();
2. Add input validation to ensure that the supplied string is indeed a comma-separated sequence.

Solution:

```py
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
    print(",".join(inp))g
```

---

## Question 9

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program:

Hello world  
Practice makes perfect

Then, the output should be:

HELLO WORLD  
PRACTICE MAKES PERFECT

Hints:

1. In case of input data being supplied to the question, it should be assumed to be from an input function;
1. Keep offering the user the faculty of inputting lines until the user inputs a "q";
1. There is no need for input validation, the program will ignore numbers and special characters;
1. Use the .upper() method.

Solution:

```py
# input function
def line_inputs():
    line_arr = []
    flag = False
    print("Please type in a line to capitalize. The program will keep accepting lines until you input the letter q")
    while (not flag):
        inp = input("Please input a line to capitalize:\t")
        flag = True if inp == "q" else line_arr.append(inp)
    return line_arr

# The capitalize function
def capitalize_arr(inp_arr):
    for line in inp_arr:
        print(line.upper())


if __name__ == "__main__":
    inp_arr = line_inputs()
    capitalize_arr(inp_arr) if len(inp_arr) > 0 else print("you have inputted no lines")
```

---
