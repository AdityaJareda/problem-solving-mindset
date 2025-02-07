# Task 11: Functions – Parameters, Return Values, and Scope

# Function Parameters - Passing values to functions.
# Return Values - Getting output from functions.
# Variable Scope - Where variables can be accessed. (local and global)

# 1. Function with multiple parameters:

def addition(a, b):                                     # Takes two parameters (a, b) and adds them.
    print(f'The sum of {a} and {b} is {a + b}.')

addition(5, 3)
addition(10, 20)

print('-----------------------------------------------------')


# 2. Return Values from Functions:

def square(num):
    return num * num                                  # Returns the square

num = int(input('Enter a number: '))                  # Takes user input for num
result = square(num)                                  # Storing returned value
print(f'The square of {num} is {result}.')

# return allows us to store and use the function's output.

print('-----------------------------------------------------')


# 3. Function Returning Multiple Values:

def get_info(name, surname):
    return f'First name: {name}', f'Last name: {surname}'   # Returns two values

info = get_info('Aditya', 'Singh')
print(info)                                                 # Prints a tuple

print('-----------------------------------------------------')


# 4.1. Variable Scope - Local Variable: (Defined Inside a Function) 

def greet_local():
    message = "Hello!"                      # Local variable
    print(message)

greet_local()                               # Will print 'message' since function is called.
# print(message)                            # Will raise an error since 'message' is not accessible outside.

print('-----------------------------------------------------')


# 4.2. Variable Scope - Global Variable: (Accessible Everywhere)
 
greeting = "Hello, everyone!"  # Global variable

def greet_global():
    print(greeting)  # Accessing global variable

greet_global()
print(greeting)  # Accessible outside the function

# Best Practice: Avoid modifying global variables inside functions. Instead, pass them as parameters.

print('-----------------------------------------------------')


# 5. Mini Project:

def calculate_grade(marks_obtained, total_marks):
    percentage = (marks_obtained / total_marks) * 100
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "Fail"
    
    return percentage, grade


marks_obtained=int(input('Enter marks obtained: '))
total_marks=int(input('Enter total marks: '))

percentage, grade = calculate_grade(marks_obtained, total_marks)
print(f"Percentage: {percentage}% - Grade: {grade}")
