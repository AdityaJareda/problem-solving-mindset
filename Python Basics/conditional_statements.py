# Task 7: Conditional Statements (if, elif, else)

# Conditional statement are used when you need to make decisions based on data.
# It helps in executing the code differently based on the outcome.

# 1. if Statement:
print('if Statement:')
age = int(input('Enter your age: '))

if age>=18:                         # Checks whether age is greater than or equal to 18. If True, the block of code inside is executed. If False, executes nothing.
    print('Eligible to vote.')


# 2. else Statement:
print('\nelse Statement:')

if age>=18:                         # Checks whether age is greater than or equal to 18. If True, the block of code inside is executed. If False, moves onto else statement and executes the block of code inside else statement.
    print('Eligible to vote.')
else:
    print('Not Eligible to vote.')


# 3. elif Statement:

print('\nelif Statement:')
if age < 13:
    print("You are a child.")
elif age < 20:                                  # Used to check additional conditions after if statement.
    print("You are a teenager.")                # Each elif block is evaluated only if the previous conditions were False.
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# 4. Nesting Conditional Statement:
print('\nNested if Statement:')
id = input('Do you have a voter id? (yes/no) : ')

if age>=18:                                     # If the condition is True, it enters the second if statement.
    if id.lower()=='yes':
        print('Eligible to vote.')
    elif id.lower()=='no':
        print('Eligible to vote but get a voter id.')
    else:
        print('Invalid input!')
else:
    print('Not eligible to vote.')


'''
Learning Outcomes:
                1. if: Executes the code block if the condition is True.
                2. elif: Used for additional conditions if the if condition is False.
                3. else: Executes if all previous conditions are False.
                4. Nesting: You can nest conditional statements inside each other.
'''