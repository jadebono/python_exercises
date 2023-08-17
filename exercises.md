# 100 Python Exercises

Adapted from the [Python Exercises of Jeffrey Hu](https://github.com/zhiwehu/Python-programming-exercises).
[Github: Jeffrey Hu](https://github.com/zhiwehu)

Adapted by: [Joseph Anthony Debono](https://github.com/jadebono).
[Email Joseph](joe@jadebono.com)

These are the exercises with the standard solutions. Class-based (OOP) solutions are kept at a minimum and only as the exercise at that point.

1. The README file: [README.md](./README.md);
1. Object Oriented Programming solutions: [OOP exercises and solutions](./OOP.md)

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

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
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

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
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

1. If the input received is in decimal form, it should be rounded off to its nearest value (for example, if the input received is 26.0, it should be printed as 26);
1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

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
1. The inner loop should multiply the current value of row with each of the values of cols and push each product into the current iteration of array[rows];
1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

Solution:

```py
# input validation
def input_validation(i, j):
    return True if (i.isdigit() and j.isdigit()) and (int(i) and int(j)) and (int(i) <= 10 and int(j) <= 10) else False


# input
def get_input():
    while True:
        i = input("please input no of rows:\t")
        j = input("please input no of columns:\t")
        if (not input_validation(i, j)):
            print("One or more of your inputs are invalid! Please try again.")
        else:
            break
    return int(i), int(j)


# array generator
def gen_arr(i, j):
    return [[i * j for j in range(0, j)] for i in range(0, i)]


if __name__ == "__main__":
    print("Please input integers to create a 2D array. For the sake of this exercise, keep the numbers to a maximum of 10.")
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

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
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

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
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

## Question 10

Write a program that accepts a sequence of whitespace separated words in a single string as input and prints the words in ascending order after removing all duplicate words and sorting them alphanumerically. Output them once more as whitespace-separated string.

Suppose the following input is supplied to the program:  
hello world and practice makes perfect and hello world again

Then, the output should be:  
again and hello makes perfect practice world

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

Solution:

```py
# input validation
def input_validation(wsv):
    wsv_arr = [i for i in wsv.split(" ")]
    return True if len(wsv_arr) > 1 else False


# input
def get_input():
    wsv = input("Please input your whitespace-separated string here:\t")
    while True:
        if (not input_validation(wsv)):
            wsv = input("Your input did not consist of whitespace-separated values. Please try again:\t")
        else:
            break
    return wsv


# sort function
def sort_arr(wsv):
    #  no need to convert set to list again since you're converting it to a whitespace-separated string once more.
    return (" ").join(sorted(set([i for i in wsv.split(" ")])))


if __name__ == "__main__":
    print("Please input a string of words separated by whitespace. This program will remove all duplicate words and print them out in ascending order")
    wsv = get_input()
    sorted_wsv = sort_arr(wsv)
    print(sorted_wsv)
```

---

## Question 11

Write a program that accepts a sequence of 4 comma-separated binary nibbles (a string of 4 bits) as its input and then checks whether they are divisible by 5 or not. The nibbles that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001 Then the output should be: 1010

Hints:

1. The string of 4 nibbles should be inputted by the user;
1. As such add error handling to make sure that the input submitted by the user conforms to the format "nibble,nibble,nibble,nibble", ex: "0100,0011,1010,1001";
1. If the submitted input does not conform, return an error message to say so and stop the code;
1. You will have to convert the input from a string to bits and then to decimals to test their divisibility;
1. Finally, you'll have to convert the output back into a byte.

Solution:

```py
def check_binary_str(bin_str):
    """
    The function is_binary_string(bin_str) checks if all characters in the string bin_str are either '0' or '1'. It does this by checking if the set of characters in bin_str is a subset of the set {'0', '1'}. If bin_str is a binary string, all of its characters will be either '0' or '1', so set(bin_str).issubset('01') will return True if bin_str is a string that contains a byte.

    Note that this function will return True for an empty string, because an empty string doesn't contain any characters that are not '0' or '1'. So add a check for this. In this implementation, the function also checks that the bin_str is of length of 4 characters and rejects bytes of other length as well.
    """
    return set(bin_str).issubset("01") if len(bin_str) == 4 else False


def validate_input(nib_str):
    # start the validate_input loop
    while True:
        # split str and check if there are any commas to confirm that nib_str is a
        # comma-separated string.
        if "," in nib_str:
            nib_arr = [i.strip() for i in nib_str.split(",") if check_binary_str(i)]
            # returns the array of nibbles converted to bytes
            return [int(i, 2) for i in nib_arr]
        else:
            nib_str = input("Your original input is invalid. Please input a string of nibbles (a string of 4 bits) separated by commas:\t")


def get_nibbles_divisible_by_five(nib_arr):
    # bin(i) converts the int back to a byte however, since the output of bin(i)
    # starts with "0b", for example the decimal integer 20 is 0b10100 in binary. To get
    # only the string of bits, slice the string from the character with the index 2
    # onward.
    return ",".join([bin(i)[2:] for i in nib_arr if i % 5 == 0])


if __name__ == "__main__":
    nibble_str = input("Please input a string of nibbles (a string of 4 bits) separated by commas. Everything else will be discarded:\t")
    my_nibble_arr = validate_input(nibble_str)
    divide_nibs_by_five = get_nibbles_divisible_by_five(my_nibble_arr)
    if len(divide_nibs_by_five) > 0:
        print(divide_nibs_by_five)
    else:
        print(f'None of your nibbles, {[bin(i)[2:] for i in my_nibble_arr]}, is divisible by five!')
```

---

## Question 12

Write a program, which will take two numbers (such as 1000 and 3000) and find all such numbers between those two numbers (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

Solution:

```py
# input validation. This function must validate that the inputs are integers
def input_validation(a, b):
    try:
        int(a) and int(b)
        return True
    except Exception:
        return False


# input function
def get_ints():
    print("For the following code, only integers will be excepted, nothing else.")
    while True:
        a = input("Please input an integer:\t")
        b = input("Please input another integer:\t")
        if (not input_validation(a, b)):
            print("invalid inputs! Try again.")
        else:
            break
    n_arr = sorted([int(a), int(b)])
    return n_arr[0], n_arr[1]


# the digit analyser function
def is_even(a, b):
    return ",".join([str(i) for i in range(a, b + 1) if all(int(elem) % 2 == 0 for elem in str(i))])


if __name__ == "__main__":
    a, b = get_ints()
    csv_ints = is_even(a, b)
    print(csv_ints)
```

---

## Question 13

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello1 world23 Then, the output should be:

Letters 10
Numbers 3

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Input validation not needed for this one.

```py
def get_string():
    return input("Please input a sentence or sequence of characters. The program will count the number of letters and digits supplied:\t")


def count_letters_and_digits(input_str):
    letter_counter = 0
    digit_counter = 0
    for elem in input_str:
        if elem.isalpha():
            letter_counter += 1
        elif elem.isdigit():
            digit_counter += 1
    return f'The number of letters in your string is {letter_counter} while the number of digits is {digit_counter}.'


if __name__ == "__main__":
    my_str = get_string()
    get_results = count_letters_and_digits(my_str)
    print(get_results)
```

---

## Question 14

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be:

1. UPPER CASE 1
1. LOWER CASE 9

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Use .isupper() and .islower() for this problem as only these two methods will restrict their counting to uppercase and lowercase letters;
1. Input validation not needed for this one.

```py
def get_string():
    return input("Please input a sentence or sequence of characters. The program will count the number of lowercase and uppercase letters in your input:\t")


def count_lower_and_upper(input_str):
    lower_counter = 0
    upper_counter = 0
    for elem in input_str:
        if elem.islower():
            lower_counter += 1
        elif elem.isupper():
            upper_counter += 1
    return f'The number of lowercase letters in your string is {lower_counter} while the number of uppercase ones is {upper_counter}.'


if __name__ == "__main__":
    my_str = get_string()
    get_results = count_lower_and_upper(my_str)
    print(get_results)

```

---

## Question 15a

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106.

Hints:

1. Only ask the user to supply the value to represent "a" in the sequence "a+aa+aaa+aaaa";
1. To be clear, the user must output the sum of "9 + 99 + 999 + 9999" given a value of 9 NOT "9 + (9*9) + (9*9*9) + (9*9*9*9)";
1. Add input validation to ensure that the supplied value is an integer.

```py
def validate_input(n):
    return True if n.isdigit() else False

def get_input():
    n = input("Please input an integer value for 'a' to calculate the value of a+aa+aaa+aaaa. Only integers will be accepted:\t")
    while True:
        if (not validate_input(n)):
            n = input("You did not input a integer. Please do so:\t")
        else:
            break
    return int(n)

def calculate_value(n):
    a_counter = 0
    for elem in "a+aa+aaa+aaaa".split("+"):
        # This line first turns an iteration of n into a string for every number in the range of the length of elem
        # Then it puts that str(n) into a list, which is then joined into a single string and finally turned into an integer that can
        # be added to a_counter
        a_counter += int("".join([str(n) for i in range(len(elem))]))
    print(a_counter)


if __name__ == "__main__":
    n = get_input()
    calculate_value(n)
```

---

## Question 15b

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Each cluster of a is an exponent of a multiplied by itself for the number of iterations in its sequence. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106.

Hints:

1. Only ask the user to supply the value to represent "a" in the sequence "a+aa+aaa+aaaa";
1. To be clear, the user must output the sum of "9 + (9*9) + (9*9*9) + (9*9*9*9)" given a value of 9 NOT the sum of "9 + 99 + 999 + 9999";
1. Add input validation to ensure that the supplied value is an integer.

```py
def validate_input(n):
    return True if n.isdigit() else False

def get_input():
    n = input("Please input an integer value for 'a' to calculate the value of a+aa+aaa+aaaa. Only integers will be accepted:\t")
    while True:
        if (not validate_input(n)):
            n = input("You did not input a integer. Please do so:\t")
        else:
            break
    return int(n)

def calculate_value(n):
    a_counter = 0
    for elem in "a+aa+aaa+aaaa".split("+"):
       a_counter += n ** len(elem)
    print(a_counter)


if __name__ == "__main__":
    n = get_input()
    calculate_value(n)
```

---

## Question 16

use map() to return an array containing the square of each odd number in another array. The array is provided by a sequence of comma-separated numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then the output should be: 1,9,25,49,81

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Python's map() function applies a function taken as an argument together with another argument to which you want to apply the function;
1. map() submits each item of a submitted list as an argument to the function it takes as well, so map(this_func, this_list) submits each item of this_list as a single argument to this_func;
1. "is not" is more Pythonic than !=;
1. You can use a generator expression to produce values only when they're needed, instead of a list that generates all possible values using unnecessary memory in the process;
1. You can then transform the generator object into a list;
1. Add input validation.
   '''

```py
def validate_input(csv_str):
    return True if "," in list(csv_str) and all([i.isdigit() for i in csv_str.split(",")]) else False


def get_input():
    csv_str = input("Please input a comma-separated sequence of integers. Only integers will be accepted.\t")
    while True:
        if (not validate_input(csv_str)):
            csv_str = input("Invalid input! Please try again:\t")
        else:
            break
    return [int(i) for i in csv_str.split(",")]


def square_odd(n):
    return str(n ** 2)  if n % 2 != 0 else None


if __name__ == "__main__":
    my_csv = get_input()
    squared_odd_str = map(square_odd, my_csv)
    print(",".join(i for i in squared_odd_str if i is not None))
```

---

## Question 17

Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500.

Hints:

1. Do not take user input for this one;
1. Provide the input as any type you like;
1. Provide validation to ensure that the transaction_log contains only valid data before processing the data.

Solution:

```py
transaction_log = "D 300 D 300 W 200 D 100"


def is_tuple_valid(tp):
    # returns True if each tuple contains a D/W and a integer, false otherwise
    return True if (tp[0] == "D" or tp[0] == "W") and tp[1].isdigit() else False


# split log into tuples and check that every one of them contains either D/W and an integer
def check_valid_transaction_log(log_list):
    # check that there is an even number of items in list
    if len(log_list) % 2 == 0:
        tuple_log = [(elem, (log_list[i+1])) for i, elem in enumerate(log_list) if i % 2 == 0]
        # validate each tuple in tuple_log and return True if so, else False
        return True if all([is_tuple_valid(i) for i in tuple_log]) else False
    return False

def compute_current_net(log_list):
    deposit, withdraw = 0, 0
    for i, elem in enumerate(log_list):
        if i % 2 == 0 and elem == "D":
            deposit += int(log_list[i+1])
        elif i % 2 == 0 and elem == "W":
            withdraw += int(log_list[i+1])
    return deposit - withdraw


if __name__ == "__main__":
    log_list = transaction_log.split()
    if check_valid_transaction_log(log_list):
        net_amount = compute_current_net(log_list)
        print(f'Transaction log is valid and the current net amount is {net_amount}')
    else:
        print("The transaction log is invalid or corrupt. Rebuild file before proceeding.")
```

---

## Question 18

A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

1. At least 1 letter between [a-z]
1. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
1. At least 1 character from [$#@]
1. Minimum length of transaction password: 6
1. Maximum length of transaction password: 12
1. No whitespaces allowed in password

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example: If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E\*,2We3345,4Jr4#175 Then, the output of the program should be: ABd1234@1,4Jr4#175

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Check for leading and trailing commas and/or whitespaces and eliminate them if there;
1. Use a regular expression for this task.

Solution:

```py
import re


def test_whitespaces(elem):
    return True if " " not in elem else False


def test_password(password_str):
    pattern = r'^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@]).{6,12}$'
    return re.match(pattern, password_str)


if __name__ == "__main__":
    passwords_csv = "ABd1234@1,a F1#,2w3E\*,2We3345,4Jr4#175"
    pwd_list = [i for i in passwords_csv.split(",") if test_whitespaces(i)]
    results = ",".join([elem for elem in pwd_list if elem != "" and test_password(elem.strip())])
    print(results)

```

---

## Question 19

You are required to write a program to sort the (name, age, height) arrays by ascending order where name is string, age and height are numbers. The arrays are input by console.

The sort criteria are:

Sort based on name;  
Then sort based on age;  
Then sort by score.

The priority is that name > age > score. If the following arrays are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,16,91 Jony,17,93 Jason,21,85

Then, the output of the program should be: [ [ 'Jason', '21', '85' ],[ 'John', '20', '90' ],[ 'Jony', '16', '91' ],[ 'Jony', '17', '91' ],[ 'Jony', '17', '93' ],[ 'Tom', '19', '80' ]]

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;

Solution:

```py
player_input = "Tom,19,80 John,20,90 Jony,17,91 Jony,16,91 Jony,17,93 Jason,21,85"

# takes a list and returns a tuple in the following sequence: (name, age, score)
def sort_seq(player):
    return (player[0], int(player[1]), int(player[2]))


def list_creator(player_input):
    players = [i.split(",") for i in player_input.split()]
    # use the sort_seq function for the sorting key of sorted
    sorted_players = sorted(players, key=sort_seq)
    return sorted_players


if __name__ == "__main__":
    player_list = list_creator(player_input)
    print(player_list)

```

---

## Question 20

Define a class with a generator expression or a generator function which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add input validation to ensure that the inputted data is an integer;
1. While you can put the input gathering and validation functions in the class, you may want to separate the (separation of concerns) as this will make the main class more reusable;
1. A generator expression is like a list comprehension but generates values one at a time, while the list comprehension generates it before iteration;
1. A generator function is a special type of function that when called returns a generator objectand uses the yield statement to return a series of values on-demand, instead of a single value or a sequence of values computed at once, making it more memory efficient when dealing with large quantities of values and it also allows more complex logic;
1. This solution uses a generator expression.

Solution:

```py
def validate_n(n):
        return True if n.isdigit() else False


def get_input():
    n = input("Please input an integer:\t")
    while True:
        if not validate_n(n):
            n = input("Invalid input. Please input an integer:\t")
        else:
            break
    return int(n)



class Divisible_by_Seven:

    def __init__(self):
        self.n = get_input()

    def generate_divisible_n(self):
        print(list((i for i in range(1, self.n) if i % 7 == 0)))



if __name__ == "__main__":
    new_seven = Divisible_by_Seven()
    new_seven.generate_divisible_n()
```

---

## Question 21

A robot moves on a 2D (Cartesian) plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement to the original point. If the distance is a float, then just print the nearest integer.

Example: If the following instructions are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add input validation;
1. To find the distance between (x1, y1) and (x2, y2) Use this formula: d= √((x2−x1)**2+(y2−y1)**2);
1. Don't forget to round it to the nearest integer.

Solution:

```py
import math


def ask_coordinates():
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    coords = []
    for direction in directions:
        coords.append(input(f'Please input a distance for the robot to go {direction}:\n'))
    return coords


def get_input():
    try:
        coords = ask_coordinates()
        x_two = int(coords[3]) - int(coords[2])
        y_two = int(coords[0]) - int(coords[1])
        return x_two, y_two
    except Exception:
        print("One or more of your inputs are invalid. Please try again.")
        x_two, y_two = get_input()
        return x_two, y_two



def compute_distance(X_ONE, Y_ONE):
    return round(math.sqrt(((x_two - X_ONE)**2) + ((y_two - Y_ONE)**2)))


if __name__ == "__main__":
    X_ONE, Y_ONE = 0, 0
    x_two, y_two = get_input()
    print(f'The distance from the origin to your provided coordinates is: {compute_distance(X_ONE, Y_ONE)}')
```

---

## Question 22

Write a program to compute the frequency of the words from the input. The output should be sorted by the key alphanumerically in ascending order. Suppose the following input is supplied to the program: "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3." Then, the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Any input is acceptable here so no input validation is necessary;
1. Sort in ascending order;
1. Do not allow for case sensitivity, in other words Python and python should be counted as separate keys in the object;
1. Do not separate punctuation, in other words 3 3? and 3. should be counted as separate keys;
1. Importing collections and using collections.Counter will return a counter object with each element counted, which value you can then access using the counter[elem] key;
1. Output as a JSON object;

```py
import collections
import json

def acquire_input():
    return input("Please input a string. Your input will be transformed into a JSON object with each key pair counting the number of times a unique word is present:\t")


if __name__ == "__main__":
    input_string = acquire_input()
    input_set = sorted(set((input_string.split())))
    my_dic = {}
    counter = collections.Counter(input_string.split())
    for elem in input_set:
        my_dic[elem] = counter[elem]
    json_dic = json.dumps(my_dic)
    print(json_dic)
```

---

## Question 23

Write a function that can calculate square value of number

Hints:

1. Use the \*\* operator
1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add input validation;
1. In this case, the method isdigit() on str enables the user to check that input is a digit directly without the need for external function.

Solution:

```py

def acquire_input():
    user_input = input("Please input a number to square. Only integers will be accepted.:\t")
    while True:
        if not str.isdigit(user_input):
            user_input = input("Invalid input, please try again:\t")
        else:
            break
    return int(user_input)


def square_n(n):
    return n ** 2


if __name__ == "__main__":
    n = acquire_input()
    square_my_n = square_n(n)
    print(square_my_n)
```

---

## Question 24

Define a class, with both a class parameter and instance parameter/s. Optionally, you may create a method to print out all these parameters.

Hints:

1. Class parameter/s are defined beneath the class declaration outside any class methods;
1. Instance parameter/s are defined in the class methods.

Solution:

```py
class Human:
    species = "Homo Sapiens"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_attributes(self):
        print(f'This is the class parameter: {self.species}')
        print(f'This is the first instance parameter: {self.name}')
        print(f'This is the second instance parameter: {self.surname}')


if __name__ == "__main__":
        joe = Human("Joseph", "Debono")
        joe.print_attributes()

```

---

## Question 25

Define a function that can compute and return the sum of two numbers.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add input validation.

Solution:

```py
def acquire_input(prompt_message):
    try:
        n = input(prompt_message)
        return int(n) if n.isdigit() else acquire_input(f'Invalid input! {prompt_message}')
    except Exception:
        acquire_input(f'Invalid input! {prompt_message}')


def add_numbers():
    a = acquire_input("Please input the first of two numbers to add together:\t")
    b = acquire_input("Please input the second of two numbers to add together:\t")
    return f'The total of {a} + {b} = {a + b}'


if __name__ == "__main__":
        result = add_numbers()
        print(result)


```

---

## Question 26

Define a function that can convert a string into an integer and print it in terminal.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add input validation.

Solution:

```py
def get_input():
    integerized_string = input("please input an integer to convert from type string to type int:\t")
    while True:
        if not integerized_string.isdigit():
            integerized_string = input("Your input cannot be converted to an integer. Please try again:\t")
        else:
            break
    return int(integerized_string)


if __name__ == "__main__":
        int_my_string = get_input()
        print(f'Your input is {int_my_string} and it is of type {type(int_my_string)}')
```

---

## Question 27

Define a function that can receive two integral numbers in string form and compute their sum and then print it in terminal.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add validation if you do take the user's input;
1. Add functionality to check if the number is a float and if so first rount it and then convert it to an integer

Solution:

```py
def is_float(num):
    try:
        num = float(num)
    except Exception:
        return False
    return True

def acquire_input(prompt_message):
    user_input = input(prompt_message)
    while True:
        if not user_input.isdigit() and not is_float(n):
            user_input = input("You have not inputted a valid integer or float. Please do so:\t")
        else:
            user_input = int(round(float(user_input)))
            break
    return user_input

def add_ints(a, b):
    return a + b


if __name__ == "__main__":
    a = acquire_input("Please input the first int to add (floats are also accepted but will be rounded):\t")
    b = acquire_input("Please input the second int to add (floats are also accepted but will be rounded):\t")
    sum_a_b = add_ints(a, b)
    print(sum_a_b)
```

---

## Question 28

Define a function that can accept two strings as input and concatenate them and then print it in terminal.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. This input does not need input validation as any input is acceptable.

Solution:

```py
if __name__ == "__main__":
    str_a = input("Please input the first string to concatenate to a second one:\t")
    str_b = input("Please input the second string to concatenate to a first one:\t")
    my_concatenated_string = str_a + str_b
    print(my_concatenated_string)
```

---

## Question 29

Define a function that can accept two strings as input and print the string with maximum length in terminal. If two strings have the same length, then the function should print all strings side by side. A possible solution is to ask the user to input two strings separated by a space, and then convert it into a list. Alternatively, you may ask the user to provide two strings using two individual inputs.

Example:

1. "hey" "world" returns "world";
1. "hello" "world" returns "hello" "world".

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. This input does not need input validation as any input is acceptable;
1. However add functionality to remove any whitespaces that creep into the user's input.

Solution:

```py
def get_input(msg):
    return input(msg).split()[0].replace(" ", "")


# computing the length of the words once and then comparing that number reduces redundant
# processing
def compute_length(word_one, word_two):
    len_one, len_two = len(word_one), len(word_two)
    if len_one > len_two:
        return word_one
    elif len_two > len_one:
        return word_two
    elif len_one == len_two:
        return f'{word_one} {word_two}'


if __name__ == "__main__":
   input_one = get_input("Please input a word. Whitespaces will be discarded. Only the first word in a phrase will be accepted:\t")
   input_two = get_input("Please input another word:\t")
   longest_word = compute_length(input_one, input_two)
   print(longest_word)
```

---

## Question 31

Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number". Additional functionality could be to make the program take inputs indefinitely, exiting only when the user makes a particular input.

Hints:

1. Use % (modulus) operator to check if a number is even or odd;
1. Assume that the input can be of any type. Add functionality to check for this and reject all invalid types, but if the input is the string of an integer or float, turn it into an integer and process it accordingly;
1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

Solution:

```py
# This function both takes inputs and validates them
def get_and_validate_inputs(msg):
    while True:
        n = input(msg)
        if n == "q":
            break
        elif n.isdigit():
            n = int(n)
            break
        try:
            float(n)
            n = int(round(float(n)))
            break
        except ValueError:
            print("Wrong input provided. Input an int or a float!")
    return n


def determine_even_odd(n):
    even_odd = None
    if n % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    return f'Your input: {n} is an {even_odd} number'


if __name__ == "__main__":
    print("Please input an integer. Floats will be converted to integers. Nonething else will be accepted. Inputting q exists.\t")
    msg = "Please input an int\t"
    while True:
        n = get_and_validate_inputs(msg)
        if n == "q":
            print("exiting program!")
            break
        else:
            n_str = determine_even_odd(n)
            print(n_str)
```

---

## Question 32

Define a function which can print a dictionary where the keys are 1... n (supplied) and the values are squares of n. For example, if create_dic(3), then the created object would be: { 1: 1, 2: 4, 3: 9}. The supplied n should be an integer due to the need to ensure that the keys are in a predictably ascending range. Finally convert the dictionary into a JSON object.

Hints:

1. Assume that the input can be of any type. Add functionality to check for this and reject all invalid types, but if the input is the string of an integer or float, turn it into an integer and process it accordingly;
1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

Solution:

```py
import json

# Get inputs and submit them to the validate_inputs() function
def get_inputs(msg):
    while True:
        n = input(msg)
        n = validate_and_convert_inputs(n)
        # if check, the loop breaks and returns the n converted to a str
        # if check is false, the loop will keep looping until it gets valid input
        if n != 0:
            break
    return n


# validate_inputs checks whether the n string is an int or a float. If so, it return two values: True, and the str converted to an int. If the n is not an int or a float, it returns False, 0
def validate_and_convert_inputs(n):
    if n.isdigit():
        return int(n)
    try:
        float(n)
        return int(round(float(n)))
    except ValueError:
        print("invalid input! Please try again!")
        return 0


# This function will create a dictionary
def create_square_dict(n):
    my_dic = {i: i**2 for i in range(1, int(n)+1)}
    return my_dic


def make_json(dic):
    json_data = json.dumps(dic)
    print(json_data)


if __name__ == "__main__":
    print("Please input an int n to create a JSON object with keys from 1 to n and values that are squares of the key: {1:1**2... n:n**2}")
    n = get_inputs("Please input int:\t")
    squared_dic = create_square_dict(n)
    make_json(squared_dic)
```

---

## Question 33

Define a function which can create a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. Convert it to a JSON object and return it as such.

Hints:

1. No input and input validation;
1. The function should take no parameters either. It just returns the required object when called.

Solution:

```py
import json

# This function will create a dictionary and convert it to a JSON object
def create_square_json():
     """
    This function creates a dictionary where the keys are numbers from 1 to 20
    and the values are the squares of the keys. It then converts this dictionary
    to a JSON object and returns it.
    """
    try:
        my_dic = {i: i**2 for i in range(1, (20 + 1))}
        return json.dumps(my_dic)
    except Exception as e:
        print(f"An error occurred while creating JSON: {e}")
        return None


if __name__ == "__main__":
    squared_json = create_square_json()
    if squared_json is not None:
        print(squared_json)

```

---

## Question 34

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are the square of the keys. Convert the dictionary to a JSON object, and then print the values ONLY.

Hints:

1. No input or input validation needed;
1. The function should have no parameters either;
1. You can export the printing of the values to another function.

Solution:

```py
import json

# This function will create a dictionary and convert it to a JSON object
def create_json(my_dic):
    """
    This function creates a dictionary where the keys are numbers from 1 to 20
    and the values are the squares of the keys. It then converts this dictionary
    to a JSON object and returns it.
    """
    try:
        return json.dumps(my_dic)
    except Exception as e:
        print(f"An error occurred while creating JSON: {e}")
        return None


def create_dic_and_print_values():
    my_dic = {i: i**2 for i in range(1, (20 + 1))}
    for value in my_dic.values():
        print(f'The value of the current key is {value}')
    return my_dic

if __name__ == "__main__":
    create_and_printed_dic = create_dic_and_print_values()
    converted_to_json = create_json(create_and_printed_dic)
    if converted_to_json is not None:
        print(converted_to_json)
```

---

## Question 35

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only. You can export the printing to another function. Finally, you can print out the dictionary as a JSON object.

Hints:

1. No input or input validation needed;
1. The function should have no parameters either;
1. You can export the printing of the values to another function.

Solution:

```py
import json

# This function will create a dictionary and convert it to a JSON object
def create_json(my_dic):
    """
    This function takes a dictionary whose keys are numbers from 1 to 20
    and the values are the squares of the keys. It then converts this dictionary
    to a JSON object and returns it.
    """
    try:
        return json.dumps(my_dic)
    except Exception as e:
        print(f"An error occurred while creating JSON: {e}")
        return None


def create_dic():
    my_dic = {i: i**2 for i in range(1, (20 + 1))}
    print_keys(my_dic)
    return my_dic


def print_keys(my_dic):
    for key in my_dic.keys():
        print(f'The current key is: {key}')


if __name__ == "__main__":
    new_dic = create_dic()
    converted_to_json = create_json(new_dic)
    if converted_to_json is not None:
        print(converted_to_json)
```

---

## Question 36

Define a function which can generate a array where the values are square of numbers between 1 and 20 (both included). Then the function needs to print an array with the first 5 elements in the array. You can export the array to another function and print it there.

Hints:

1. No input or input validation needed;
1. The function should have no parameters either;
1. You can export the printing of the values to another function.

Solution:

```py
def gen_square_array(n):
    return [i**2 for i in range(1,n+1)]

def print_first_five_items(arr):
    x = [i for i in arr if i <= arr[4]]
    print(x)

if __name__ == "__main__":
    my_arr = gen_square_array(20)
    print_first_five_items(my_arr)
```

---

## Question 37

Define a function which can generate a array where the values are square of numbers between 1 and 20 (both included). Then the function needs to print an array excluding the first 5 elements in the array. You can export the array to another function and print it there.

Hints:

1. No input or input validation needed;
1. The function should have no parameters either;
1. You can export the printing of the values to another function.

Solution:

```py
def gen_square_array():
    return [i**2 for i in range(1,20+1)]

def print_items_more_than_five(arr):
    x = arr[5:]
    print(x)

if __name__ == "__main__":
    my_arr = gen_square_array()
    print_items_more_than_five(my_arr)
```

---

## Question 38

With a given array [1,2,3,4,5,6,7,8,9,10] write a program to print the first half values in one line and the last half values in one line. In case that n is an odd number, the first array should be the longer one.

Hints:

1.  Take an n integer from the user, or a float which you can turn into an integer, but reject anything else;
1.  You will need input validation if you take input from the user;
1.  You can either create two new arrays and print one under the other or you turn the array into a string and print one half over the other one both halves as strings.

Solution:

```py
def validate_input(n):
    if n.isdigit():
        return True, int(n)
    try:
        float(n)
        return True, int(round(float(n)))
    except ValueError:
        return False, 0

def create_arr(n):
    return [i for i in range(1, n+1)]

def divide_arrs(arr):
    mid = (len(arr) // 2) if len(arr) % 2 == 0 else (len(arr) // 2) + 1
    arr_one, arr_two = arr[:mid], arr[mid:]
    print(arr_one)
    print(arr_two)

if __name__ == "__main__":
    while True:
        user_input = input("Please input an integer to represent the length of the array:\t")
        check, n = validate_input(user_input)
        if check:
            my_arr = create_arr(n)
            divide_arrs(my_arr)
            break
        else:
            print("Invalid input! Please try again!")
```

---

## Question 39

Write a program to generate and print another array whose values are even numbers in the given array [1,2,3,4,5,6,7,8,9,10] => [2,3,6,8,10]. If you like, add functionality to do the same if the numbers are supplied as a comma separated string "1,2,3,4,5,6,7,8,9,10". In this case,the output should be a comma separated string. For this exercise, do not take input from the user.

Solution:

```py
def create_arr_as_csv():
    return ",".join([str(i) for i in range(1,11) if i % 2 == 0])

if __name__ == "__main__":
    csv_arr = create_arr_as_csv()
    print(csv_arr)
```

---

## Question 40

Write a program that accepts a string as input and prints "Yes" if the string is "yes" or "YES" or "Yes" only, otherwise print "No".

Hints:

1. No other variation of "yes" such as "YEs", "yeS" etc. is to be accepted.

Solution:

```py
def comply():
    valid_inputs = ["YES", "Yes", "yes"]
    user_input = input("Affirm your compliance!:\t")
    print("Yes") if user_input in valid_inputs else print("No")

if __name__ == "__main__":
    comply()

```

---

## Question 41

Write a program that can filter even numbers in an array by using the filter() function. The array is: [1,2,3,4,5,6,7,8,9,10]. For this exercise, the numbers should be of type integer.

Hints:

1. No need to take user input for this exercise, and therefore no need for validation;
1. You can use a list comprehension for this purpose but for the sake of this exercise use only Python's filter() function;
1. Likewise, do not use a lambda function for this task;
1. in Python, the filter() function takes two arguments, the filtering function itself (which should return a boolean function indicating whether the iterated element passes the filtering test or not), and the iterable, such filter(my_filter_func, my_arr), and my_arr will be sorted according to the boolean test that my_filter_func returns;
1. filter() returns an iterable that has to be converted to a list to be printed out.

Solution:

```py
def even_elements(i):
    # This expression returns a boolean value as surely as if one had to write:
    # return True if i % 2 == 0 else False
    return i % 2 == 0


if __name__ == "__main__":
    my_arr = [1,2,3,4,5,6,7,8,9,10]
    even_arr = list(filter(even_elements, my_arr))
    print(even_arr)
```

---

## Question 42

Write a program that uses map() to make an array whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]. For this exercise, the numbers should be of type integer.

Hints:

1. No need to take user input for this exercise, and therefore no need for validation;
1. You can use a list comprehension for this purpose but for the sake of this exercise use only Python's map() function;
1. Likewise, do not use a lambda function for this task.

```py
def square_elements(i):
    return i ** 2

if __name__ == "__main__":
    my_arr = [1,2,3,4,5,6,7,8,9,10]
    even_arr = list(map(square_elements, my_arr))
    print(even_arr)
```

---

## Question 43

Write a program that uses map() and filter() to make an array whose elements are squares of the even number in [1,2,3,4,5,6,7,8,9,10]. For this exercise, the numbers should be of type integer.

Hints:

1. No need to take user input for this exercise, and therefore no need for validation;
1. You can use a list comprehension for this purpose but for the sake of this exercise use only Python's filter() and map() functions without using lambda functions.

```py
def even_nums(i):
    return i % 2 == 0

def square_nums(i):
    return i ** 2

if __name__ == "__main__":
    my_arr = [1,2,3,4,5,6,7,8,9,10]
    my_evens = list(filter(even_nums, my_arr))
    my_squared_evens = list(map(square_nums, my_evens))
    print(my_squared_evens)
```

---

## Question 44

Write a program which uses map() and filter() to make an array whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]. For this exercise, the numbers should be of type integer. Moreover, use lambda functions here, NOT helper functions.

Hints:

1. No need to take user input for this exercise, and therefore no need for validation;
1. You can use a list comprehension for this purpose but for the sake of this exercise you should only use map() and filter() with lambda functions.

```py
if __name__ == "__main__":
    my_arr = [1,2,3,4,5,6,7,8,9,10]
    my_evens = list(filter(lambda x: x % 2 == 0, my_arr))
    my_squared_evens = list(map(lambda x: x **2, my_evens))
    print(my_squared_evens)
```

---

## Question 45

Write a program that can generate an array containing integers between 1... and n and then filter() that array to return an array whose elements are the even numbers in the original array.

Hints:

1. If you take user input, remember to include validation.

```py
def create_arr(n):
    return [i for i in range(1, n+1)]

# This function uses a lambda function to validate user input
def user_input():
    user_n = input("Please input an integer n:\t")
    while True:
        # The lambda function is not necessary, if n.isdigit() would have been enough
        # Note that the parentheses are required to execute the lambda function.
        if (lambda n: n.isdigit())(user_n):
            return int(user_n)
        else:
            user_n = input("Invalid input! Please input an integer n:\t")


if __name__ == "__main__":
    print("This program will take an integer n that you submit, generate an array from 1 to n, and then return an array whose elements are the even numbers in the original array.")
    n = user_input()
    user_arr = create_arr(n)
    evens_arr = list(filter(lambda x: x % 2 == 0, user_arr))
    squared_evens_arr = list(map(lambda x: x ** 2, evens_arr))
    print(squared_evens_arr)
```

---

## Question 46

Write a program that uses map() to create an array whose elements are square of numbers between 1 and 20 (both included).

1. No need to take user input for this exercise, and therefore no need for validation;

```py
if __name__ == "__main__":
    my_arr = [i for i in range(1, 21)]
    my_squared_arr = list(map(lambda x: x**2, my_arr))
    print(my_squared_arr)
```

---

## Question 47

Define a class named human which has a static method that prints a generic aphorism of your choice on humanity \. Extend it with a subclass class called Notable. The subclass should be used to define create instances of notable figures in human history.

Hints:

1. static is a keyword used to define static methods in a class;
1. These are methods that cannot be called on instances of the class, only on the class itself;
1. To create a static method, use the @staticmethod;
1. To call the constructor of the superclass in the constructor of the subclass use super().**init**() with the arguments passed to the constructor of the subclass BUT not self.

```py
class Human:
    """
    This is a base class for creating Human instances.
    """
    def __init__(self, name, surname, country):
        self.name = name
        self.surname = surname
        self.country = country


    def get_details(self):
        print(f'The name of your human is: {self.name} {self.surname}. {self.name} is a citizen of the {self.country}')


    """
    This is the static method of the Human class and it is called on the class itself, not on instances of it.
    """
    @staticmethod
    def print_aphorism():
        print("Man is the measure of all things")


class Notable(Human):
    """
    This is a subclass of the Human class. It is used for creating instances of notable figures in human history.
    """
    def __init__(self, name, surname, country, typus, achievement):
        self.typus = typus
        self.achievement = achievement
        # This line calls the constructor of the superclass, passing the arguments
        # passed to this contructor to the constructor of the superclass.
        super().__init__(name, surname, country)


    def print_achievement(self):
        print(f'{self.name} {self.surname} of the {self.country} is {"an" if self.typus[0].lower() in ["a", "e", "i", "o", "u"] else "a"} {self.typus} who {self.achievement}')


if __name__ == "__main__":
    terence = Human("Publius Terentius", "Afer", "Res Publica Romana" )
    terence.get_details()
    Human.print_aphorism()
    neil = Notable("Neil", "Armstrong", "USA", "Astronaut", "was the first man on the moon")
    neil.print_achievement()
```

---

## Question 48

Assuming that we have some email addresses in the "username@companyname.com" format, write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:

If the following email address is given as input to the program: john@gmail.com Then, the output of the program should be: john

Hints:

1. Assume that the emails are already contained in a list in the main body of the code;
1. There are at least two ways of achieving this task - either by using str.split("@") and taking the first element of the resultant split, or use str.index("@") which returns the index of the first iteration of that element in the list but raises a ValueError exception if that element does not occur in the string;
1. If you go for the str.index("@") solution, remember to add exception handling.

Solution:

```py
def get_names(email_list):
    return [i.split('@')[0] for i in email_list]


if __name__ == "__main__":
    emails = ["alexander@macedonia.imp", "scipio@respublicromana.rm", "caesar@imperiumromanum.rm"]
    names = get_names(emails)
    print(names)
```

---

## Question 49

Create an object called Colour. The **init** parameters should include r, g, b. Add a method to the object. Initialize two instances of this object.

Hints:

1. If you take user input, remember to include validation.

Solution:

```py
class Colour:

    @staticmethod
    def get_input():
        r = Colour.validate_input(input("Please input an integer value for red - 0-255:\t"))
        g = Colour.validate_input(input("Please input an integer value for green - 0-255:\t"))
        b = Colour.validate_input(input("Please input an integer value for blue - 0-255:\t"))
        return [r, g, b]

    @staticmethod
    def validate_input(colour_integer):
        while True:
            if colour_integer.isdigit() and (0 <= int(colour_integer) <= 255):
                return int(colour_integer)
            else:
                colour_integer = input("invalid input! Please try again:\t")

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_colour_values(self):
        return f'Your colour values are R:{self.r}, G:{self.g} and B:{self.b}'


if __name__ == "__main__":
    colours = Colour.get_input()
    # RGB for Royal Blue is: 65, 105, 225
    # Here *colours unpacks the three items in the list returned by Colour.get_input()
    # This saves the hassle of either referencing the individual items in that list
    # or setting them to r, g, b variables
    royal_blue = Colour(*colours)
    print(royal_blue.colour_getter())
    colours = Colour.get_input()
    # RGB for Coral is: 255, 127, 80
    coral = Colour(*colours)
    print(coral.colour_getter())
```

---

## Question 50

Define a class called European and two subclasses, one German, one Italian. On the European class, add a constructor, and a class method. On the German class, add a constructor property called self.world_wars_started. Use super().**init**() to extend the constructor of the European Class to the German subclass with its own constructor. To the Italian subclass add a method that overrides the Superclass method.

Hints:

1. Refer to question 47 for how to construct a superclass with a subclass and how to use the super().**init**() method.

Solution:

```py
class European:


    def __init__(self, name, city):
        self.name = name
        self.city = city


    def favourite_drink(self):
        return f'{self.name} of {self.city} loves drinking alcohol.'


class German(European):


    def __init__(self, name, city, world_cups):
        self.world_wars_started = 2
        self.world_cups = world_cups
        super().__init__(name, city)


class Italian(European):


    def favourite_drink(self):
        return f'{self.name} of {self.city} loves drinking Chianti.'


if __name__ == "__main__":
    pierre = European("Pierre", "Paris")
    print(pierre.favourite_drink())
    hans = German("Hans", "Berlin", 2)
    print(f'Germans started {hans.world_wars_started} world wars but won none of them. On the other hand, Germans won {hans.world_cups}. {hans.favourite_drink()}.')
    stefano = Italian("Stefano", "Firenze")
    print(stefano.favourite_drink())
```

---

## Question 51

Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

1. If you take user input, remember to include validation.

Solution:

```py
from math import pi

class Circle:

    @staticmethod
    def validate_input(r):
        while True:
            try:
                float(r)
                return float(r)
            except Exception:
                r = input("Invalid input! Please enter a valid number for the radius of a circle:\t")


    def __init__(self, radius):
        self.radius = radius

    # The property decorator lets the user access a method as a property.
    # This makes it more efficient to access if the radius changes instead of setting
    # it to a class instance.
    @property
    def area(self):
        return pi * (self.radius ** 2)



if __name__ == "__main__":
    r = Circle.validate_input(input("Please input the radius of your circle:\t"))
    my_circle = Circle(r)
    print(my_circle.area)
```

---

## Question 52

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

1. If you take user input, remember to include validation.

Solution:

```py
class Rectangle:

    @staticmethod
    def validate_input(n, dim):
        while True:
            try:
                float(n)
                return float(n)
            except Exception:
                n = input(f'Invalid input! Please enter a valid number for the {dim} of a rectangle:\t')


    def __init__(self, length, width):
        self.length = length
        self.width = width



    # The property decorator lets the user access a method as a property.
    # This makes it more efficient to access if the radius changes instead of setting
    # it to a class instance.
    @property
    def area(self):
        return (self.length * self.width)



if __name__ == "__main__":
    length_dim, width_dim = "length", "width"
    length = Rectangle.validate_input(input(f'Please input the length of your rectangle:\t'), length_dim)
    width = Rectangle.validate_input(input(f'Please input the width of your rectangle:\t'), width_dim)
    my_rectangle = Rectangle(length, width)
    print(my_rectangle.area)
```

---

## Question 53

Define a class named Shape and its subclass Square. The Square class has a constructor function which takes a length and breadth as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

1. To override a method in the superclass, we can define a method with the same name in the subclass.

Solution:

```py
class Shape:

    def __init__(self, area=0):
        self.area = area

    def get_area(self):
        return f'the area of your shape is {self.area}'

class Square(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = self.compute_area()


    def compute_area(self):
        return self.length * self.breadth


    def get_area(self):
        return f'the area of your square is {self.area}'


if __name__ == "__main__":
    my_square = Square(10,20)
    print(my_square.get_area())
```

---

## Question 54

Write a programme that raises an exception. use a try-except block to catch it.

Hints:

1. Import logging from the logging module, which is part of the standard library;
1. By default, the logging module logs the messages with a severity level of WARNING and above. The levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL in increasing order of severity.

Solution:

```py
import logging


def try_for_exception(a, b):
    """
    The try-block tests the types of a and b, and if they do not match it raises a TypeError defined in the parentheses, otherwise it returns a +b.
    However, if the exception is raised, it uses logging.error to print out the exception defined as error.

    """
    try:
        # using isinstance(a, type(b)) because it deals with inheritance while type()
        # does not. Essentially comparing a subclass with a superclass works with
        # isinstance() but not type()
        if not isinstance(a, type(b)):
            raise TypeError("Arguments do not match! Arguments should be of the same type (ints/floats with ints/floats or strings with strings) to carry out the plus operation on them")
        return a + b
    except Exception as error:
        logging.error(error)


if __name__ == "__main__":
    a = 10
    b = " World"
    c = try_for_exception(a, b)
    if c is not None:
        print(c)
```

---

## Question 54

Create your own exception. Define own properties and methods for it. Pass it to the except-block and use those properties and methods in the except-block

Hints:

1. Create a subclass to the superclass Exception

Solution:

```py
class UserUnderageException(Exception):


    def __init__(self, message, age):
        super().__init__(message)
        self.age = age


    def years_until_of_age(self):
        return 18 - self.age



if __name__ == "__main__":
    # Raise the custom exception
    try:
        user_age = 16
        if user_age < 18:
            raise UserUnderageException("User is underage.", user_age)
    except UserUnderageException as error:
        print(error)  # Prints: User is underage.
        print(f"User's age: {error.age}")  # Prints: User's age: 16
        print(f"Years until user is of age: {error.years_until_of_age()}")  # Prints: Years until user is of age: 2
```

---

## Question 55

Write a function to return something that causes an exception and use try/except to catch the exception.

Solution:

```py
import logging


def divide_args(a, b):
    try:
        return a / b
    except TypeError as error:
        logging.error(f'TypeError discovered: {error}')


if __name__ == "__main__":
    a = 10
    b = "hello"
    ans = divide_args(a, b)
    # None is returned from a function that returns no other value. In this case, when
    # an exception is caught, the function just returns None, so it would be pointless
    # printing it. So we only print ans if its value is not None.
    if ans != None:
        print(ans)
```

---

## Question 56

Assuming that we have some email addresses, in the "username@companyname.com" format, stored in a list, please write program to print the username of a given email address. Both user names and company names are composed of letters only. Capitalize the username.

Example: If the following email address is given as input to the program: john@google.com, then, the output of the program should be: John

Hints:

1. Assume that the emails are already provided and validated;
1. You can use the str.index(char) to get the index of a character in a string or a list, but be aware that it can throw up a ValueError if the substring is not found.

Solution:

```py
def get_usernames(email_list):
    names_list = []
    for email in email_list:
        at_indx = email.index("@")
        names_list.append(email[:at_indx].capitalize())
    return names_list



if __name__ == "__main__":
    email_addresses = email_addresses = [
    "john@gmail.com",
    "sarah@yahoo.com",
    "michael@outlook.com",
    "emma@hotmail.com",
    "david@aol.com",
    "olivia@icloud.com",
    "daniel@zoho.com",
    "sophia@protonmail.com",
    "james@yandex.com",
    "isabella@mail.com"
]
    email_usernames = get_usernames(email_addresses)
    for name in email_usernames:
        print(name)
```

---

## Question 57

Assuming that we have some email addresses in the "username@companyname.com" format, which addresses are stored in a list, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program: john@google.com Then, the output of the program should be: google

Hints:

1. Instead of using the .index() method, you may want to use split(), discarding the part of the string you do not want into a throwaway variable.

Solution:

```py
if __name__ == "__main__":
    email_addresses = [
    "john@gmail.com",
    "sarah@yahoo.com",
    "michael@outlook.com",
    "emma@hotmail.com",
    "david@aol.com",
    "olivia@icloud.com",
    "daniel@zoho.com",
    "sophia@protonmail.com",
    "james@yandex.com",
    "isabella@mail.com"
]
    for email in email_addresses:
        # split("@") is returning two values, name the value before "@" and domain is
        # the value after "@". In this case we need to split domain too, so we retain it.
        name, domain = email.split("@")
        # the effect of splitting domain is to return two strings, the second of which,
        # after the "." is not required and therefore assigned to the throwaway variable
        # _
        company, _ = domain.split(".")
        print(company)
```

---

## Question 58

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example: If the following words is given as input to the program: 2 cats and 3 dogs. Then, the output of the program should be: ['2', '3']

Hints:

1. Accept only digits that are integers;
1. No input validation needed for this problem.

Solution:

```py
def get_num_arr(my_seq):
    return [i for i in my_seq.strip().split() if i.isdigit()]

if __name__ == "__main__":
    seq = input("Please input a string. The program will then output any integer digits in the string:\t")
    num_arr = get_num_arr(seq)
    if num_arr != []:
        print(num_arr)
    else:
        print("There were no digits in your input!")
```

---

## Question 59

Create an async function.

Hints:

1. An async function returns a promise without the need to use resolve and reject. The value returned is resolved, while errors are rejected. Use then() and catch() to consume the promise;
1. Python introduced the async and await keywords in Python 3.5 as part of its asyncio library. The asyncio library is used for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives;
1. You may want to use asyncio.sleep(1) which is a stand-in for IO-bound work. Although it actually blocks the execution of the script for 1 second, in a real-world scenario, this could be replaced with non-blocking IO-bound tasks;

Solution:

```py
import asyncio
import time

async def count():
    """
    This async function count() is a coroutine that prints "One", waits for 1 second in a non-blocking way, then prints "Two".
    """
    print("One")

    """
    The await keyword is used in Python's asyncio library to pause the execution of the coroutine until the awaited object is complete. In the context of await asyncio.sleep(1), it's telling the event loop "I have nothing to do for 1 second, you can go and run other tasks".

    asyncio.sleep(1) is a coroutine that mimics IO-bound work by sleeping for 1 second. It's a non-blocking operation, meaning that it doesn't block the entire program while it's sleeping. Instead, it gives control back to the event loop, which can go and run other tasks.

    When the sleep is over (after 1 second), the event loop will resume the coroutine that was paused at the await asyncio.sleep(1) line.

    So, in short, await asyncio.sleep(1) is saying "pause this coroutine and give control back to the event loop for 1 second, then resume this coroutine". This allows other tasks to run during that 1 second, which is the essence of asynchronous programming.
    """
    await asyncio.sleep(1)
    print("Two")


async def count_main():
    """
    The count_main() coroutine uses asyncio.gather() to run three count() coroutines concurrently.

    asyncio.gather() is used when you want to run multiple coroutines concurrently and gather their results. It returns a future aggregating results from the given coroutine objects and will finish when all the coroutines have finished.
    """
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":

    s = time.perf_counter()
    try:
        """
    asyncio.run() is used to execute a single coroutine and return the result. It's a convenience function that creates an event loop, runs the given coroutine, closes the loop, and finally returns the result. It's typically used as the main entry point for asyncio-based programs.
        """
        asyncio.run(count_main())
    except Exception as e:
        print(f"An error occurred: {e}")
    elapsed = time.perf_counter() - s
    print(f"Program completed in {elapsed:0.2f} seconds.")
```

---

## Question 60

Create a RegEx pattern dynamically from a supplied variable. The pattern should match a letter or more (the target) at the end of the supplied string.

Hints:

1. Import re, Python's regular expression module;
1. use re.compile() to create the regular expression that matches the target;
1. Then use the .search() method and pass the string to it to search the string for the regular expression created from the target.

Solution:

```py
import re  # Python's regular expression module

def confirm_ending(my_str, target):
    try:
        # Create a regular expression that matches the target at the end of a string
        target_regex = re.compile(f'{target}$')
        # Search for the regular expression in my_str and return True if found, False otherwise
        return bool(target_regex.search(my_str))
    except re.error:
        print("Invalid regular expression pattern.")
        return False


if __name__ == "__main__":
    my_str = "Arma virumque cano"
    my_target = "no"
    x = confirm_ending(my_str, my_target)
    print(x)
```

---

## Question 61

Define a mixin class from which two other classes inherit one common method and one common property.

Hints:

1.  A Mixin is a base class that contains methods for use by other classes without having to be the parent class of those other classes;
1.  Instead of using inheritance to distribute functionalities to different classes, you can use Mixins to package the functionality you want in one class, then inherit from that class wherever you want to use the functionality;
1.  Essentially create a mixin class that two other classes inherit from.

Solution:

```py
class Engine:

    '''
    The class Engine is the mixin class
    '''

    #  the @property decorator indicates a class property and is considered pythonic
    @property
    def eng_type(self):
        return "internal combustion engine"

    def move(self):
        print("Your vehicle moves")


# a second class to inherit a property and method from the mixin base class
class Car(Engine):
    pass

# a third class to inherit a property and method from the mixin base class
class Ship(Engine):
    pass


if __name__ == "__main__":
    # Instantiating classes from the second and third class
    car = Car()
    ship = Ship()
    # printing the common property inherited from the mixin class
    print(car.eng_type)
    print(ship.eng_type)
    # running the common method inherited from the mixin class
    car.move()
    ship.move()
```

---
