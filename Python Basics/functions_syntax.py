# Task 10: Functions – Definition and Basic Syntax

# Function - Block of reusable code that performs a specific task. Instead of writing the same code again and again, we can write it once inside a function and call it whenever needed.

# Reasons to use function:
# 1. Improve readability and organization
# 2. Easier debugging and maintenance
# 3. Modular approach (divide large programs into small parts)
# 4. Avoid repetition

# _______________________________________________________

# Syntax:
# def function_name():
    # code block (function body)

# def - Used to define a function.
# function_name - The name you choose for the function.
# () - Parameters go inside parenthesis.

# IMPORTANT - All code inside the function must be indented.

# _______________________________________________________


# 1. Defining and calling a function:

def calling():
    print('This is how you call a function.')                      

calling()


print('-----------------------------------------------------')


#  2. Function with parameter:

def day(today):                       # 'day' is a parameter.
    print(f'Today is {today}.')

day('Friday')                       # 'Friday' is an argument.

# We can make functions more flexible by using parameters.
# You can also use same keyword for function name and parameter. [But it's not ideal as it create confusion and overwrite the function itself if you're not careful.]