# Task 13: Python Modules & Importing

# Module: A Python file (.py) that contains functions, variables, and classes that can be used in other programs.

# 1. Built-in Modules: (Pre-installed in Python)

# 1.1. Importing the math module:

import math

print(math.sqrt(16))            # calling 'sqrt()' function from math module. [Calculates square root]
print(math.pi)

print('-----------------------------------------------------')


# 1.2. Importing datetime module:

import datetime

today = datetime.date.today()
print("Today's date:", today)

print('-----------------------------------------------------')



# 2. Importing Specific Functions from a Module:

# Instead of importing the whole module, you can import only the functions you need.

from math import sqrt

print(sqrt(25))

print('-----------------------------------------------------')



# 3. Renaming Modules with 'as':

# You can use 'as (alias)' to rename a module while importing.

import math as m            # Module 'math' renamed to 'm'.

print(m.factorial(5))

print('-----------------------------------------------------')



# 4. Exploring Installed Modules:

# help() - To see what functions a module contains.
# dir() - To get details about a specific function.

print(dir(math))        # Lists all functions in math module.
print('\n-----------------------------------------------------\n')
help(math.sqrt)         # Shows documentation for sqrt function.

print('-----------------------------------------------------')



# 5. Importing Your Own Module:

import my_module

print(my_module.greet("Alice"))
print(my_module.add(5, 3))

print('-----------------------------------------------------')



# 6. Using __name__ == "__main__":

# When a module is imported, all its code runs.
# To prevent this we use, ' __name__ == "__main__": '
# This ensures that some code runs only when the script is executed directly, not when imported.

# FOR IMPLEMENTATION CHECK my_module.py