# Task 4: Detailed exploration of Strings

# 1. Taking user input as string

name = input('Enter your name: ')

# 2. Print the input

print(f'You are {name}!')

# 3. Uppercase Conversion:

name_upper = name.upper()           # .upper() function converts every character in the string into capital letters.
print(f'Your name in uppercase {name_upper}')

# 4. Lowercase Conversion:

name_lower = name.lower()           # .lower() function converts every character in the string into small letters.
print(f'Your name in lowercase {name_lower}')

# 5. String Splitting:

day = 'Today is Wednesday.'
day_split = day.split()             # .split() function splits the string into list of substrings
print(day_split)

# 6. String Concatenation:

surname = input('Enter your surname: ') 
print('Your fullname is ',name + surname,'.')       # Concatenates name and surname using '+' operator

# 7. String Slicing:

day2 = 'Today is Wednesday and tomorrow is Thursday.'
day2_slice = day2[:18]          # Here the string in 'day2' variable is sliced and first 18 character of the string is assigned to 'day2_slice'       
print(day2_slice)

# 8. f-string formatting:

fullname = f'Your fullname is {name} {surname}.'     # Using f-string you can directly embed variables in a string
print(fullname)

# 9. format() method formatting:

fullname1 = 'Your fullname is {} {}.'.format(name,surname)     # Similar to f-string
print(fullname1)

# 10. Reversed string:

reverse_day = day[::-1]     # Reversing the string
print(reverse_day)

# 11. Replacing string:

day_replace = day.replace('Wednesday','Thrusday')       # replace() function replaces 'Wednesday' with 'Thrusday' from the string.
print(day_replace)