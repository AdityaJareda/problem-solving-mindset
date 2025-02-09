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
        print(f'\n_______ {topic[0]} _______')
        print(topic[1])
        run_quiz(choice)
    else:
        print('Invalid choice. Please enter a valid topic number.')

def run_quiz(topic):
    quiz={
        1: ("What will be the output of `x = 5; print(x)`?", "5"),
        2: ("What is the data type of `3.14` in Python?", "float"),
        3: ("What will be printed? `x = 10; if x > 5: print('Yes') else: print('No')`", "Yes"),
        4: ("How many times will this loop execute? `for i in range(3): print(i)`", "3"),
        5: ("Which keyword is used to define a function in Python?", "def"),
        6: ("What is the main difference between a list and a tuple?", "Lists are mutable, tuples are immutable."),
        7: ("How do you access the value associated with key `'name'` in `student = {'name': 'John', 'age': 20}`?", "student['name']"),
        8: ("Which mode is used to append data to an existing file?", "a"),
        9: ("What type of error does `10 / 0` cause in Python?", "ZeroDivisionError"),
        10: ("How do you import the `math` module in Python?", "import math")
    }

    question, correct_answer=quiz.get(topic, ("", ""))

    if question:
        user_answer=input(f'\nQUIZ:\n-> {question}\nYour Answer: ').strip()
        if user_answer.lower() == correct_answer.lower():
            print('_______ CORRECT! _______')
        else:
            print(f'_______ INCORRECT! _______\nThe correct answer is: {correct_answer}')