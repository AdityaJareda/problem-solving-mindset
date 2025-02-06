# Task 6: Operators - Arithmetic, Assignment, Comparison, Logical

# 1. Arithmetic Operators: Performs mathematical tasks. [Addition, Subtraction, Multiplication, Division, Floor Division, Modulus, Exponentiation.]

a=15
b=4

addition = a+b              # '+' operator adds the integer 15 and 4.
subtraction = a-b           # '-' operator subtracts the integer 4 from 15.
multiplication = a*b        # '*' operator multiplies the integer 15 and 4.
division = a/b              # '/' operator divides the integer 15 with 4. [always returns a float]
floor_division = a//b       # '//' operator is similar to division, only difference is that it always returns an integer and removes the decimal part.
modulus = a%b               # '%' operator divides the integer 15 with 4 and returns the remainder.
exponentiation = a**b       # '**' operator takes the integer 15 as base and 4 as exponent.

print("Arithmetic Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)


# 2. Assignment Operators: Assigning and updating variable values. [ = (Simple assignment), +=, -=, *=, /=, //=, %=, **= (Augmented assignment operators) ]

num = 21
print("\nInitial num:", num)

print('Augmentated Assignment Operations:')
num += 10                       # Equivalent to: num = num + 10.
print("num after += 10:", num)

num -= 5                        # Equivalent to: num = num - 5.
print("num after -= 5:", num)

num *= 2                        # Equivalent to: num = num * 2.
print("num after *= 2:", num)

num /= 4                        # Equivalent to: num = num / 4. [returns float]
print("num after /= 4:", num)


# 3. Comparison Operators: Compare two values and return Boolean (True/False) results. 
# Types: == (equal), != (not equal), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to)

x = 10
y = 5

print('\nComparison Operations:')
print("x == y:", x == y)    # '==' operator checks if x and y are equal. [use '==' instead of 'is' for value comparison.] 
print("x != y:", x != y)    # '==' operator checks if x and y are not equal.
print("x > y:", x > y)      # '==' operator checks if x is greater than y.
print("x < y:", x < y)      # '==' operator checks if x is less than y.
print("x >= y:", x >= y)    # '==' operator checks if x is greater than or equal to y.
print("x <= y:", x <= y)    # '==' operator checks if x is less than or equal to y.

# 4. Logical Operators: used to combine multiple conditions. ['and', 'or', 'not']

print('\nLogical Operators: ')
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

# Implementing 'and' operator:
if (age>=18) and (height>=160):
    print('Condition: Age and Height are sufficient.')
    print('Result: Allowed on the ride.')
else:
    print('Condition: Age and Height are not sufficient.')
    print('Result: Not allowed on the ride.')

# Implementing 'or' operator:
free_ride=False
if (height>184) or free_ride:
    print("Result: Allowed on the ride for free.")
else:
    print('Result: Pay for the ticket.')

# Implementing 'not' operator:

if not (height>184):
    print('Result: Not Eligible for a chance for free ride.')
else:
    print('Result: Eligible for a chance for free ride.')
