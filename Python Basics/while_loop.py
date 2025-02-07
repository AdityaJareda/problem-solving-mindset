# Task 9 Details: Loops – while Loop

# while Loop: Repeatedly executes a block of code as long as a given condition remains true. Once the condition becomes false, the loop stops.

# Syntax:
# while condition:
    # block of code

# condition: If the condition evaluates to True, the loop continues. If it evaluates to False, the loop stops.
# block of code: The block of code inside the loop that gets executed repeatedly as long as the condition is true.


# 1. while loop:
print("1. while Loop:")

countdown1 = 5

print('Countdown 1:')
while countdown1>0:              # while loop checks if countdown > 0. If True, it enter the loop. If False, terminates the loop.
    print(countdown1)            
    countdown1 -= 1              # Decreases countdown by 1.


# 2. Breaking out of an infite loop:

countdown2 = 5

print('\nCountdown 2:')
while True:
     print(countdown2)
     countdown2-=1
     if countdown2== -5:
          break


# 3. Implementing Menu:

menu = {1: 'Enter',
        2: 'Exit'}

while True:
    for key, value in menu.items():             # The for loop iterates through each key-value pair in the dictionary. 'menu.item()' returns a tuple of pairs, with each pair have a key and value.
         print(f'{key}. {value}')               # printing key and value in a formatted string.

    choice=int(input('Enter your choice [1 or 2]: '))

    if choice==1:
         print('Welcome!')
         break
    elif choice==2:
         print('Exiting...')
         break
    else:
         print('Invalid Input!')
        