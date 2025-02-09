def show_topics():
    topics={1: 'Variables',
            2: 'Data Types',
            3: 'Control Flow',
            4: 'Loops',
            5: 'Functions',
            6: 'List & Tuples',
            7: 'Dictionaries',
            8: 'File Handling',
            9: 'Exception Handling',
            10: 'Modules and Imports',
            11: 'Exit'}
    
    while True:

        print('\n_____ Learning Topics _____')
        for key,value in topics.items():
            print(f'{key}. {value}')
        print('_____________________________\n')

        choice=input('\nSelect a Topic you want to learn: ').strip()

        try:
            choice=int(choice)

            if choice in topics:    
                if choice==11:
                    print('Returning to Main Menu...')
                    break
                else:
                    topic_content(choice)
            else:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please enter an integer.')
    
def topic_content(choice):
    topics = {
        1: ('Variables', "Variables store data in memory. No need to declare type explicitly.\nExample: x = 10  # x stores the integer 10"),
        2: ('Data Types', "Python has int, float, str, list, tuple, dict, etc.\nExample: name = 'Alice'  # A string variable"),
        3: ('Control Flow', "Control flow (if-else) helps make decisions in code.\nExample:\nif x > 5:\n    print('x is greater than 5')"),
        4: ('Loops', "Loops repeat code multiple times. Python has 'for' and 'while' loops.\nExample:\nfor i in range(3):\n    print(i)  # Prints 0, 1, 2"),
        5: ('Functions', "Functions help organize reusable code. Defined using 'def'.\nExample:\ndef greet(name):\n    return 'Hello ' + name"),
        6: ('Lists & Tuples', "Lists are mutable, tuples are immutable.\nExample:\nnumbers = [1, 2, 3]  # List\ncoordinates = (10, 20)  # Tuple"),
        7: ('Dictionaries', "Dictionaries store key-value pairs.\nExample:\nstudent = {'name': 'John', 'age': 20}"),
        8: ('File Handling', "Python allows reading/writing files using open().\nExample:\nwith open('file.txt', 'w') as f:\n    f.write('Hello, World!')"),
        9: ('Exception Handling', "Use try-except to handle errors.\nExample:\ntry:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"),
        10: ('Modules & Imports', "Modules help organize code.\nExample:\nimport math\nprint(math.sqrt(16))  # Output: 4.0")
    }

    topic = topics.get(choice)
    if topic:
        print(f'\n___ {topic[0]} ___')
        print(topic[1])
    else:
        print('Invalid choice. Please enter a valid topic number.')

