# `100 Python Exercises in Object Oriented Programming``

Adapted from the [Python Exercises of Jeffrey Hu](https://github.com/zhiwehu/Python-programming-exercises).
[Github: Jeffrey Hu](https://github.com/zhiwehu)

Adapted by: [Joseph Anthony Debono](https://github.com/jadebono).
[Email Joseph](joe@jadebono.com)

This file contains the same 100-exercise Python programming challenge based on the exercises by Jeffrey Hu except that all exercises are solved using Object Oriented Programming (OOP).

1. The README file: [README.md](./README.md);  
1. The standard solutions: [standard exercises and solutions](./exercises.md).



---

## Question 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. Solve this problem using OOP.

Solution:

```py

class Divisible_Seven_Not_Five: 
    """
    This class finds and prints all numbers within a given range that are divisible by 7 but not a multiple of 5.
    """

    def __init__(self, n_start, n_end):
        """
        Initialize the Divisible_Seven_Not_Five object with start and end values, and prepare storage for the results.
        """
        # validate the inputs submitted at the creation of the class
        self.n_start = self.validate_input(n_start, "starting")
        self.n_end = self.validate_input(n_end, "ending")
        # initialize instance variables for storage
        # These are instance variables because each object will have its own
        self.div_by_seven_not_five_arr = []
        self.div_by_seven_not_five_csv = ""
     
        
    # the validation function is part of the class
    def validate_input(self, n, type):
        """
        Validate that the input is a digit and return it as an integer. If the input is not valid, continue asking until a valid input is provided.
        """
        while True:
            if n.isdigit():
                return int(n)
            else:
                n = input(f'Invalid input. Please input a {type} integer:\t')


    #  This function uses a list comprehension and the instance variables created
    # in the __init__ function to create a list of the numbers that satisfy the
    # requirements of the problem
    def create_arr(self):
        """
        Generate a list of numbers within the object's range that are divisible by 7 but not a multiple of 5.
        """
        self.div_by_seven_not_five_arr = [str(i) for i in range(self.n_start, self.n_end + 1) if i % 7 == 0 and i % 5 != 0]
        

    # This is the function that converts the solution array to a CSV
    def convert_to_csv(self):
        """
        Convert the list of valid numbers to a CSV string.
        """
        self.div_by_seven_not_five_csv = ",".join(self.div_by_seven_not_five_arr)
        

    # The class that executes the logic to generate the solution
    def get_solution(self):
        """
        Generate the list of valid numbers and convert it to a CSV string, then return the result.
        """
        self.create_arr()
        self.convert_to_csv()
        return self.div_by_seven_not_five_csv


if __name__ == "__main__":
    # the start and end integers are obtained before the creation of the object
    n_start = input("Please input a starting integer:\t")
    n_end = input("Please input an ending integer:\t")
    # The start and end integers are passed as parameters to the new object
    new_solution = Divisible_Seven_Not_Five(n_start, n_end)
    # printing the new_solution with the .get_solution() method
    print(new_solution.get_solution())
```

---

## Question 2

Write a program which can compute the factorial of a given numbers. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320. Solve this problem using OOP.

Hints:

1. In case of input data being supplied to the question, take the input from the user using input();
1. If you take user input, remember to add input validation;
1. There is a problem with submitting arguments to a compute_factorial method since if take the recursion integer from an instance variable of a class instance (self.n), this will not exist at the time of method definition. You may want to use a default argument in the method definition and then set it to your instance variable of the class instance.

Solution:

```py
class Factorial:
    
    def __init__(self, n):
        """
        Initialize the Factorial class. Validates and stores the input number.
        """
        # Validate and store the input number
        self.n = self.validate(n)


    def validate(self, n):
        """
        Validate the input number. If the input is not a digit, keep asking for a valid input.
        """
        while True:
            if n.isdigit():
                return int(n)
            else:
                n = input("Invalid input! Please input a valid integer to calculate its factorial:\t")


    def compute_factorial(self, n=None):
        """
        Compute the factorial of a given number.

        The method takes an argument 'n' which defaults to None. This argument is needed for the recursion.
        If no argument is passed when calling this method, 'n' is set to the instance variable 'self.n'. Note that self.n is the instance variable n of the class instance self.
        We use 'n=None' in the method definition because at the time of method definition, 'self.n' does not exist yet.
        Therefore, we cannot use 'n=self.n' as the default argument, but we can assign 'n' to 'self.n' within the method.

        The method then calculates and returns the factorial of 'n'.
        """
        # If no argument is provided, use the stored number
        if n is None:
            n = self.n
        # Calculate and return the factorial
        return 1 if n == 0 else n * self.compute_factorial(n - 1)


if __name__ == "__main__":
    n = input("Please input a valid integer to calculate its factorial:\t")
    my_fac = Factorial(n)
    print(my_fac.compute_factorial())
```

---

## Question 3

With a given integral number n, write a program to generate an object that contains (i, i*i) such that i is an integral number between 1 and n (both included). and then the program should print the object. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}. Solve this problem using OOP

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Remember to use input validation if you take input from the user.
1. Remember to separate the process of dictionary creation and the process of data validation, creation, and printing. This way, you're not creating the dictionary immediately upon instantiation of the object, but rather when you call a specific method. This allows you to reuse the same object for different numbers if needed.

Solution:

```py
class GenerateIntegerDict:
    
    def __init__(self, n):
        self.n = self.validate_n(n)
        
        
    def validate_n(self, n):
        while True:
            if n.isdigit():
                return int(n)
            else:
                n = input("Invalid input! Please input an integer:\t")
        
                
    def create_integer_dict(self):
        self.integer_dict = {i: i**2 for i in range(1, self.n+1)}
            

    def print_dict(self):
        print(self.integer_dict)
        
        
if __name__ == "__main__":
    my_n = input("Please input an integer to create a integer dictionary:\t")
    new_integer_dict = GenerateIntegerDict(my_n)
    new_integer_dict.create_integer_dict()
    new_integer_dict.print_dict()
```

---

## Question 4

Write a program which takes a sequence of comma-separated numbers and generates an array and an object which contains every number. Solve this problem using OOP.

Example:
Suppose the following input is supplied to the program: 34,67,55,33,12,98;
Then, the output should be: ['34', '67', '55', '33', '12', '98'] {'34':34, '67':67, '55':55, '33':33, '12':12, '98':98}

Hints:
1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add input validation.

Solution:

```py
class CSVNums:
    
    """
    user validation is made through a static method that is called in the constructor function of the class
    """
    @staticmethod
    def input_validation(csv):
        while True:
            test = all(i.isdigit() for i in csv.split(","))
            if test:
                return csv
            else:
                csv = input("Input error! Please input a list of comma separated integers:\t")
    
    
    def __init__(self, csv):
        self.csv = self.input_validation(csv)
        # call the methods to create the stores 
        self.create_arr()
        self.create_dic()
        
        
    def create_arr(self):
        # the instance arr is created here
        self.csv_arr = [int(i) for i in self.csv.split(",")]
    
    
    def create_dic(self):
        # the instance object is created here
        self.csv_dic = {i:int(i) for i in self.csv.split(",")}
    

    def get_csv_arr(self):
        # a getter method for self.csv_arr
        return str(self.csv_arr)
        

    def get_csv_dic(self):
        # a getter method for self.csv_dic
        return str(self.csv_dic)


if __name__ == "__main__":
    user_csv = input("Please input a list of comma separated integers. Only integers separated by a comma will be accepted:\t")
    first_csv = CSVNums(user_csv)
    print(first_csv.get_csv_arr())
    print(first_csv.get_csv_dic())
```


---

## Question 5

Write a class that generates objects that can calculate and print the value according to the given formula: Q = √((2 * C * d)/H)

Following are the fixed values of C and H:

C = 50;
H = 30;
d is the variable whose values should be input to your program using input() 

Example:

if d = 100, q = 18;
if d = 150, q = 22;
if d = 180, q = 24.


Hints:

1. Since C and H are constants, you may want to make them class variables;
1. If the input received is in decimal form, it should be rounded off to its nearest value (for example, if the input received is 26.0, it should be printed as 26);
1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. If you take input from the user, add input validation.

Solution:

```py
from math import sqrt

class StrangeEquation:
    """
    A class to compute the equation Q = √((2 * C * d)/H) for various instances of d.
    C and H are constants so are defined as class variables.
    validate_input does not depend on the state of any instance so is defined as a static method.
    """
    
    
    C = 50
    H = 30
    
    
    @staticmethod
    # Input validation, with a try/except clause.
    def validate_input(d):
        while True:
            try:
                return round(float(d))
            except Exception:
                d = input("Invalid input! Please input an integer or a float:\t")
    
    
    def __init__(self, d):
        # Initializes self.d and computes self.q immediately.
        self.d = d
        self.q = self.calculate_q()
        
       
    def calculate_q(self):
        # Calculates q.
        return round(sqrt((2*StrangeEquation.C*self.d)/StrangeEquation.H)   )
    
    
    def get_q(self):
        # Returns a formatted string showing the result q for the given d.
        return f'The solution to the equation √((2 * C * d)/H) for your input {self.d} is {self.q}'

    
if __name__ == "__main__":
    d = StrangeEquation.validate_input(input("Please input an integer or a float to serve as d in the equation q = √((2 * C * d)/H):\t"))
    new_d = StrangeEquation(d)
    new_d_q = new_d.get_q()
    print(new_d_q)
```


---

## Question 6

Write a program which takes 2 digits, i,j as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Note that i = rows, j = cols. Solve this problem using OOP.

Example:  
Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:

1. Create an array;
1. The external loop (rows) should create an empty array for each of its iterations and push each array into the parent array;
1. The inner loop should multiply the current value of row with each of the values of cols and push each product into the current iteration of array[rows];
1. It will be helpful to use descriptive names for the variables (and everything else) - rows and cols are much easier to understand in the code than i and j;
1. In case of input data being supplied to the question, it should be assumed to come from the input() function.



Solution:

```py
class TwoDArray:
    
    @staticmethod
    def validate_input(n):
        while True:
            if n.isdigit():
                return int(n)
            else:
                n = input("Invalid input! Please input a valid integer:\t")
                
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.arr_2d = self.array_2d()
        
        
    def array_2d(self):
        """
        Generates a 2-dimensional array with `rows` number of rows and `cols` number of columns.  Each element in the i-th row and j-th column is the product of i and j. Here j is an value in the range of columns, while i is a value in the range of rows.
        """
        return [[i * j for j in range(self.cols)] for i in range(self.rows)]
        
        
    def get_2d_array(self):
        return self.arr_2d

    
if __name__ == "__main__":
    print("Input two integers to generate a 2d Array")
    rows = TwoDArray.validate_input(input("Please input the number of rows:\t"))
    cols = TwoDArray.validate_input(input("Please input the number of columns:\t"))
    my_2d_arr = TwoDArray(rows, cols)
    print(my_2d_arr.get_2d_array())
```

---

## Question 7

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program: without,hello,bag,world
Then the output should be: bag,hello,without,world. Solve this problem using OOP.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Add input validation to ensure that the supplied string is indeed a comma-separated sequence;
1. Use sorted() (returns a new sorted array) or .sort() (sorts array in place) to do the sorting. 

Solution:

```py
class CSVSort:
    
    
    @staticmethod
    def take_input():
        user_input = input("Please enter a sequence of comma separated words for this program to sort:\t")
        return CSVSort.validate_input(user_input)


    @staticmethod
    def validate_input(inp):
        while True:
            # the .strip() method strips whitespace from the elements
            csv_arr = [i.strip() for i in inp.split(",")]
            if len(csv_arr) >= 2:
                return csv_arr
            inp = input("Invalid input! Please enter a sequence of at least two comma separated words for this program to sort:\t")
    
    
    def __init__(self, ):
        self.csv_arr = sorted(CSVSort.take_input())
        
            
    def get_sorted_csv(self):
        return ",".join(self.csv_arr)

    
if __name__ == "__main__":
    new_csv_arr = CSVSort()
    print(new_csv_arr.get_sorted_csv())
```

---

## Question 8

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Solve this program using OOP.

Suppose the following input is supplied to the program:
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
class NewCapitalStr():
    """
    This class creates an object that takes an array of strings and then returns them capitalized when the .print_capitalized_lines() method is called on it.
    """

    
    def __init__(self, my_str_arr):
        self.my_str_arr = my_str_arr
        
    
    def print_capitalized_lines(self):
        for elem in [i.upper() for i in self.my_str_arr]:
            print(elem)
    
    

def get_input():
    user_str_arr = []
    while True:
        user_str = input("Please input a string to capitalize. Q to exit:\t")
        if user_str.lower() != "q":
            user_str_arr.append(user_str)
        else:
            return user_str_arr


        
if __name__ == "__main__":
    arr_str = get_input()
    my_first_upper_arrs = NewCapitalStr(arr_str)
    my_first_upper_arrs.print_capitalized_lines()

```


---

## Question 9

Write a program that accepts a sequence of whitespace separated words in a single string as input and prints the words in ascending order after removing all duplicate words and sorting them alphanumerically. Output them once more as whitespace-separated string. Solve this problem using OOP.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

Solution:

```py
class SortStr:
    

    def __init__(self, arr):
        self.msg_arr = arr


    def print_sorted_str(self):
        my_set = set(self.msg_arr)
        # sorts the elements stripped of whitespace and prints them as a whitespace separated string
        print(" ".join(sorted([i.strip() for i in my_set])))
        

def get_str():
    return input("Please input a string of words separated by whitespaces for this program to remove duplicates and print sorted:\t")


if __name__ == "__main__":
    my_str_arr = get_str().split()
    new_sorted_str = SortStr(my_str_arr)
    new_sorted_str.print_sorted_str()
```

---

## Question 10

Write a program that accepts a sequence of 4 comma-separated binary nibbles (a string of 4 bits) as its input and then checks whether they are divisible by 5 or not. The nibbles that are divisible by 5 are to be printed in a comma separated sequence. Solve this problem using OOP.

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
class NibByFive:
    
    
    @staticmethod
    def is_valid_nibble(bin_str):
        """
        The function is_binary_string(bin_str) checks if all characters in the string bin_str are either '0' or '1'. It does this by checking if the set of characters in bin_str is a subset of the set {'0', '1'}. If bin_str is a binary string, all of its characters will be either '0' or '1', so set(bin_str).issubset('01') will return True if bin_str is a string that contains a byte. 

        Note that this function will return True for an empty string, because an empty string doesn't contain any characters that are not '0' or '1'. So add a check for this. In this implementation, the function also checks that the bin_str is of length of 4 characters and rejects bytes of other length as well.
        """
        return set(bin_str).issubset("01") if len(bin_str) == 4 else False


    @staticmethod
    def validate_input(nib_str):
        # Start the validate_input loop
        while True:
            # split str and check if there are any commas to confirm that nib_str is a 
            # comma-separated string.
            if "," in nib_str:
                nib_arr = [i.strip() for i in nib_str.split(",") if NibByFive.is_valid_nibble(i)]
                # returns the array of nibbles converted to bytes
                return [int(i, 2) for i in nib_arr]
            else:
                nib_str = input("Your original input is invalid. Please input a string of nibbles (a string of 4 bits) separated by commas:\t")
    
    
    def __init__(self, nib_arr):
        self.nib_arr = nib_arr


    def get_nibbles_divisible_by_five(self):
        # bin(i) converts the int back to a byte however, since the output of bin(i)
        # starts with "0b", for example the decimal integer 20 is 0b10100 in binary. To get
        # only the string of bits, slice the string from the character with the index 2 
        # onward.
        return ",".join([bin(i)[2:] for i in self.nib_arr if i % 5 == 0])
    
        
        
if __name__ == "__main__":
    nibble_str = input("Please input a string of nibbles (a string of 4 bits) separated by commas. Everything else will be discarded:\t")
    my_nibble_arr = NibByFive.validate_input(nibble_str)
    my_nib_class = NibByFive(my_nibble_arr)
    divided_nibs_by_five = my_nib_class.get_nibbles_divisible_by_five()
    if len(divided_nibs_by_five) > 0:
        print(divided_nibs_by_five)
    else:
        print(f'None of your nibbles, {[bin(i)[2:] for i in my_nibble_arr]}, is divisible by five!')
```

---


## Question 11

Write a program, which will take two numbers (such as 1000 and 3000) and find all such numbers between those two numbers (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line. Solve this problem using OOP.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function.

Solution:

```py
class FindEvenDigits:
    
    
    @staticmethod
    def check_even_digits(n):
       """Check if all digits in the number are even."""
       return all(digit in '02468' for digit in str(n))
        
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.csv_even_seq = self.generate_csv_even_sequence()
        
        
    def generate_csv_even_sequence(self):
        return [str(i) for i in range(int(self.a), int(self.b)+1) if FindEvenDigits.check_even_digits(i)]
        
        
    def get_csv_even_sequence(self):
        return ",".join(self.csv_even_seq)
        

    
def validate_input(n, a=0):
    """
    Adding a second parameter, with a default value of 0 allows the function
    to ensure that the the first user_input (a) is greater than 0, and the second user_input (b) is greater than the first one (a). This will allow us to provide the requested output of the programme in ascending order.
    """
    while True:
        if n.isdigit() and int(n) > a:
            return n
        else:
            n = input("Invalid input! Please input a valid integer:\t")
        
        
if __name__ == "__main__":
    a = validate_input(input("Please input an integer:\t"))
    b = validate_input(input("Please input an integer:\t"), int(a))
    new_even_digits_sequence = FindEvenDigits(a, b)
    print(new_even_digits_sequence.get_csv_even_sequence())
```

---
## Question 12

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello1 world23 Then, the output should be:

Letters 10
Numbers 3

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Input validation not needed for this one.

Solution:

```py
class LettersNumbersCounter:
    
    def __init__(self, my_str):
        self.input_str = my_str
        self.letters = 0
        self.numbers = 0
        self.count_letters_nums()
    
    
    def count_letters_nums(self):
        for elem in self.input_str:
            if elem.isalpha():
                self.letters += 1
            elif elem.isdigit():
                self.numbers += 1
    
    
    def get_results(self):
        return f'The numbers of letters and numbers in your string "{self.input_str}" are: Letters = {self.letters}; Numbers = {self.numbers}'


if __name__ == "__main__":
    my_str = input("Please input a string. This program will count the number of letters and numbers in your code:\t")
    my_counted_letters_nums = LettersNumbersCounter(my_str)
    my_result = my_counted_letters_nums.get_results()
    print(my_result)
```

---
## Question 13

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be:

UPPER CASE 1
LOWER CASE 9

Solve the problem using OOP.

Hints:

1. In case of input data being supplied to the question, it should be assumed to come from the input() function;
1. Use .isupper() and .islower() for this problem as only these two methods will restrict their counting to uppercase and lowercase letters;
1. Input validation not needed for this one.

Solution:

```py
class CalcUpperAndLower:
    
    @staticmethod
    def get_input():
        return input("Please input a string:\t")
    
    
    def __init__(self, sentence):
        self.sentence = sentence
        self.upper = 0
        self.lower = 0
        self.calc_cases()
        
           
    def calc_cases(self):
        for elem in self.sentence:
            if elem.isupper():
                self.upper += 1
            elif elem.islower():
                self.lower +=1
               
    
    def display_counts(self):
        return f'In your string {self.sentence}, you have {self.lower} lowercase letters and {self.upper} uppercase letters'


if __name__ == "__main__":
    my_sentence = CalcUpperAndLower.get_input()
    my_new_calc_upper_lower = CalcUpperAndLower(my_sentence)
    print(my_new_calc_upper_lower.display_counts())
```

---

## Question 14

Write a class that creates an object and return the length of the object.

Hints:

1. Use a magic/dunder method for this purpose;
1. The appropriate dunder method is __len__ that defines what happens when you run len() on your object. 

```py
class Person:
    

    def __init__(self, name="", qualities=None): 
        """
        By setting parameters to empty as default values, you can first create an empty object and then  provide the properties later. Note that:
        
        name="" is straighforward;
        
        qualities=None is not straighforward: If you use qualities=[] as a default value, you run into a problem. When using a mutable data type like a list as a default value for a parameter, such as qualities=[], you need to be careful. In Python, default parameter values are evaluated only once when the function or method is defined, not each time it is called. This means that if you modify the default value in one instance, it will affect all instances of the class that don't provide their own value for that parameter.

        To avoid this issue, it is recommended to set the default value to None and create a new empty list inside the __init__ method if no value is provided for qualities. This ensures that each instance has its own separate list.
        """
        self.name = name
        self.qualities = qualities or None
        

    def __len__(self):
        return len(self.qualities)
    
   
if __name__ == "__main__":
    john = Person("John", ["sedentary", "greedy", "educated", "employed"])
    # calling the __len__ method
    print(f'The length of the john object is: {len(john)}')

```

---
## Question 15

Extend the class you created for Question 14 and make it subscriptable. 

Hints:

1. Use a magic/dunder method for this purpose;
1. The appropriate dunder method to make this object subscriptable is __getitem__ that defines what happens when you try to retrieve an element from the object with an index. 

```py
class Person:
    
    
    def __init__(self, name="", qualities=None): 
        """
        By setting parameters to empty as default values, you can first create an empty object and then  provide the properties later. Note that:
        
        name="" is straighforward;
        
        qualities=None is not straighforward: If you use qualities=[] as a default value, you run into a problem. When using a mutable data type like a list as a default value for a parameter, such as qualities=[], you need to be careful. In Python, default parameter values are evaluated only once when the function or method is defined, not each time it is called. This means that if you modify the default value in one instance, it will affect all instances of the class that don't provide their own value for that parameter.

        To avoid this issue, it is recommended to set the default value to None and create a new empty list inside the __init__ method if no value is provided for qualities. This ensures that each instance has its own separate list.
        """
        self.name = name
        self.qualities = qualities or []
        
        
    def __len__(self):
        return len(self.qualities)
    
    
    def __getitem__(self, index):
        return self.qualities[index]
    
    
if __name__ == "__main__":
    john = Person("John", ["sedentary", "greedy", "educated", "employed"])
    # calling the __len__ method
    print(f'The length of the john object is: {len(john)}')
    # calling the __getitem__ method
    print(f'The element at john[1] is {john[1]}')
```

---
## Question 16

Extend the class you created for Question 15 and return an "official" string representation of an object. 

Hints:

1. Use a magic/dunder method for this purpose; 
1. __repr__ is the magic method to use for this purpose;
1. It's generally good practice to define __repr__ for your classes, because it makes debugging and logging easier. You can immediately see the "official" string representation of your objects when you print them or log them;
1. The Python Enhancement Proposal (PEP) 8, which is Python's official style guide, recommends that the __repr__ method return a string that is a valid Python expression whenever possible. This means that ideally, you should be able to copy the string returned by __repr__, paste it into a Python interpreter, and get an equivalent object back;
1. If it's not feasible to return a string that is a valid Python expression (for example, if the object has a complex internal state that can't be easily recreated), the __repr__ method should return a string in the form <...> that gives a detailed description of the object. For example, a file object's __repr__ might look like <open file '/path/to/file', mode 'r' at 0x10d38d0d0>.

```py
class Person:
    
    
    def __init__(self, name="", qualities=None): 
        """
        By setting parameters to empty as default values, you can first create an empty object and then  provide the properties later. Note that:
        
        name="" is straighforward;
        
        qualities=None is not straighforward: If you use qualities=[] as a default value, you run into a problem. When using a mutable data type like a list as a default value for a parameter, such as qualities=[], you need to be careful. In Python, default parameter values are evaluated only once when the function or method is defined, not each time it is called. This means that if you modify the default value in one instance, it will affect all instances of the class that don't provide their own value for that parameter.

        To avoid this issue, it is recommended to set the default value to None and create a new empty list inside the __init__ method if no value is provided for qualities. This ensures that each instance has its own separate list.
        """
        self.name = name
        self.qualities = qualities or []
        
        
    def __len__(self):
        return len(self.qualities)
    
    
    def __getitem__(self, index):
        return self.qualities[index]
    

    def __repr__(self):
        qualities_str = ", ".join(self.qualities)
        return f"Person - Name: '{self.name}'; qualities: {qualities_str}"
    
    
if __name__ == "__main__":
    john = Person("John", ["sedentary", "greedy", "educated", "employed"])
    # calling the __repr__ method. Note that if you have the __repr__ method
    # without the __str__ method, you can just use print() on your object.
    print(f'The representation of the john object is {repr(john)}')
```

---

## Question 17

Extend the class you created for Question 16 and print out a representation of the class objects as a string 

Hints:

1. Use a magic/dunder method for this purpose; 
1. __str__ is the magic method to use for this purpose. The __str__ method should be the most human-readable form of the object and should be thoroughly understandable. If __str__ is not provided then Python interpreter will use the result of __repr__ as a fallback;
1. When you print the object, Python will call the __str__ method, and print the string it returns.

```py
class Person:
    
    
    def __init__(self, name="", qualities=None): 
        """
        By setting parameters to empty as default values, you can first create an empty object and then  provide the properties later. Note that:
        
        name="" is straighforward;
        
        qualities=None is not straighforward: If you use qualities=[] as a default value, you run into a problem. When using a mutable data type like a list as a default value for a parameter, such as qualities=[], you need to be careful. In Python, default parameter values are evaluated only once when the function or method is defined, not each time it is called. This means that if you modify the default value in one instance, it will affect all instances of the class that don't provide their own value for that parameter.

        To avoid this issue, it is recommended to set the default value to None and create a new empty list inside the __init__ method if no value is provided for qualities. This ensures that each instance has its own separate list.
        """
        
        self.name = name
        self.qualities = qualities or []
        
        
    def __len__(self):
        return len(self.qualities)
    
    
    def __getitem__(self, index):
        return self.qualities[index]
    
    
    def __repr__(self):
        qualities_str = ", ".join(self.qualities)
        return f"Person - Name: '{self.name}'; qualities: {qualities_str}"
    
    
    def __str__(self):
        qualities_str = ", ".join(self.qualities)
        return f"The Person's name is {self.name} and his qualities are: {qualities_str}"
    
    
if __name__ == "__main__":
    """
    Please note that the print() function in Python uses the __str__ method to display the string representation of the object. If __str__ is not defined, Python will use __repr__ as a fallback.

    If you want to specifically use __repr__ while having both __repr__ and __str__ methods in your class, you can call repr() function on the object.
    """
    john = Person("John", ["sedentary", "greedy", "educated", "employed"])
    # calling the __len__ method
    print(f'The length of the john object is: {len(john)}')
    # calling the __getitem__ method
    print(f'The element at john[1] is {john[1]}')
    # calling the __repr__ method
    print(f'The representation of the john object is {repr(john)}')
    # calling the __str__method
    print(john)
```

---

## Question 18

```py
```

---
