# Task 14: Error Handling – try, except, finally

# try - Code that might cause an error.
# except - Handles specific errors.
# finally - Runs whether an error occurs or not.
# else - Runs if no error occurs.

# try-except:

# Instead of letting the program crash, we can use try-except to handle errors gracefully.

# Basic Syntax:

# try:
     # Code that may cause an error

# except <ExceptionType>:
     # Code that runs if an error occurs

# finally:
    # Code that runs no matter what (optional)

# 1. Handling division by zero error:

try:
    result = 10 / 0                                 # This will cause a ZeroDivisionError
except ZeroDivisionError:                           # Prevents from crashing the program
    print('Error: You cannot divide by zero!')  

print('-----------------------------------------------------')



# 2. Handling multiple exceptions:

try:
    number = int(input('Enter a number: '))
    result = 10 / number
    print('Result:', result)
except ZeroDivisionError:
    print('Error: Cannot divide by zero!')
except ValueError:                                      # If the user enters a non-numeric value, we catch ValueError.
    print('Error: Please enter a valid number!')

print('-----------------------------------------------------')



# 3. Using finally: (Code that runs no matter what)

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    
    result = num1 / num2
    print('Result:', result)

except ValueError:
    print('Error: Please enter valid integer numbers!')             # Handles non-numeric input

except ZeroDivisionError:
    print('Error: Division by zero is not allowed!')                # Handles division by zero

finally:
    print('Program execution completed.')                           # Runs no matter what

print('-----------------------------------------------------')



# 4. Using else: (Only runs if no error occurs)

try:
    num = int(input('Enter a number: '))
    print('You entered:', num)
except ValueError:
    print('Invalid input! Please enter a number.')
else:                                                           # If the user enters a valid number, the else block runs.
    print('No errors occurred!')