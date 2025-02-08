# Task 15: File I/O – Reading and Writing Files

# Basic Syntax:
# open('filename', 'mode')

# Modes:
# 'r' - Read (default).
# 'w' - Write (creates new file or overwrites existing).
# 'a' - Append (adds to the file without deleting existing content).
# 'x' - Create a new file (gives error if file already exists).
# 'r+' - Read and write (does not create a new file, must exist).
# 'w+'	Write and read (overwrites the file if it exists, creates a new one if it doesn’t).
# 'a+'	Append and read (keeps old data, allows reading).

# Closing a file: file.close()


# 1. Writing to a File:

file = open('Python Basics/files_IO/text.txt', 'w')                 # Opening file 'text.txt' inside 'files_IO' folder in write mode. ('w' - overwrites already existing file content)

file.write('This is how you write in a file using Python.\n')       # Writing content to the file.
file.write('This is the second line.\n')

file.close()                                                        # Closing the file.

print('File writing completed.')

print('-----------------------------------------------------')


# 2. Reading from a File:

file = open('Python Basics/files_IO/text.txt', 'r')                 # Opening file 'text.txt' inside 'files_IO' folder in read mode.

content = file.read()                                               # Read the entire file content.

file.close()

print(f'File Content:\n{content}')                                  # Displaying the content

# read() reads the entire file into a string.

print('-----------------------------------------------------')


# 3. Reading Line by Line:

file = open('Python Basics/files_IO/text.txt', 'r')

for line in file:
    print('Read Line:', line.strip())                               # strip() removes extra spaces/newline.

file.close()

# Useful for reading large files without loading everything into memory.

print('-----------------------------------------------------')


# 4. Appending Data to a File:

file = open('Python Basics/files_IO/text.txt', 'a')                 # Opening file 'text.txt' inside 'files_IO' folder in append mode. ('a' keeps old and adds new content)

file.write('This is an appended line.\n')

file.close()

print('Appending completed.')

print('-----------------------------------------------------')


# 5. Using 'with' Statement:

with open('Python Basics/files_IO/text.txt', 'r') as file:
    content = file.read()
    print(f'File Content:\n{content}')

# Best Practice - Using 'with' ensures the file closes automatically after execution and there's no need to call 'file.close()' manually.

print('-----------------------------------------------------')


# 6. Mini Project:

my_file = 'Python Basics/files_IO/tasks.txt'

def add_task():
    task = input('Enter your task: ')
    with open(my_file, 'a') as file:
        file.write(task + '\n')
    print('Task added successfully!')

def view_task():
    try:
        with open(my_file, 'r') as file:
            tasks=file.readlines()
            if not file:
                print('No tasks found!')
            else:
                print('\nTO-DO List:')
                for index,tasks in enumerate(tasks,start=1):
                    print(f'{index}.{tasks}')
    except FileNotFoundError:
        print('No tasks found! Start by adding some.')

menu = {1: 'Add Task',
        2: 'View Task',
        3: 'Exit'}

def main():
    while True:
        print('TO-DO List Menu:')
        for key,value in menu.items():
            print(f'{key}.{value}')
    
        choice = input('Enter your choice: ')

        try:
            choice = int(choice)

            if choice == 1:
                add_task()
                print('-----------------------------------------------------')
            elif choice == 2:
                view_task()
                print('-----------------------------------------------------')
            elif choice == 3:
                print('Goodbye! Your tasks are saved.')
                break
            else:
                print('Invalid input entered. Please try again.')
        except ValueError:
            print('Invalid input entered. Please enter a number.')
main()