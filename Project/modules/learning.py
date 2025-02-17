from modules.progress import mark_topic_completed

class Modules:
    def __init__(self,module_name,description,status="Not Started"):
        self.module_name=module_name
        self.description=description
        self.status=status
        self.quiz_score=0

    def display_info(self):
        print(f'======== {self.module_name} ========\n')
        print(f'Description:\n{self.description}\n')
        print(f'Status: {self.status}')

    def module_start(self):
        self.status='In Progress'
        print(f'The {self.module_name} module is now in progress.')

    def module_complete(self):
        self.status='Module Completed'
        print(f'You have completed the {self.module_name} module.')

    def update_score(self,score):
        self.quiz_score=score
        print(f'Your score for the {self.module_name} module quiz is: {self.quiz_score}/1')


def show_topics():
    topics={
        1: 'Variables',
        2: 'Data Types',
        3: 'Control Flow',
        4: 'Loops',
        5: 'Functions',
        6: 'List & Tuples',
        7: 'Dictionaries',
        8: 'File Handling',
        9: 'Exception Handling',
        10: 'Modules and Imports',
        11: 'Exit'
    }

    topic_description={

        1: ('Variables', "Variables store data in memory. No need to declare type explicitly.\nExample: x = 10  # x stores the integer 10"),
        2: ('Data Types', "Python has int, float, str, list, tuple, dict, etc.\nExample: name = 'Alice'  # A string variable"),
        3: ('Control Flow', "Control flow (if-else) helps make decisions in code.\nExample:\nif x > 5:\n    print('x is greater than 5')\nelse:\n   print('x is less than 5)"),
        4: ('Loops', "Loops repeat code multiple times. Python has 'for' and 'while' loops.\nExample:\nfor i in range(3):\n    print(i)  # Prints 0, 1, 2"),
        5: ('Functions', "Functions help organize reusable code. Defined using 'def'.\nExample:\ndef greet(name):\n    return 'Hello ' + name"),
        6: ('Lists & Tuples', "Lists are mutable, tuples are immutable.\nExample:\nnumbers = [1, 2, 3]  # List\ncoordinates = (10, 20)  # Tuple"),
        7: ('Dictionaries', "Dictionaries store key-value pairs.\nExample:\nstudent = {'name': 'John', 'age': 20}"),
        8: ('File Handling', "Python allows reading/writing files using open().\nExample:\nwith open('file.txt', 'w') as f:\n    f.write('Hello, World!')"),
        9: ('Exception Handling', "Use try-except to handle errors.\nExample:\ntry:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"),
        10: ('Modules & Imports', "Modules help organize code.\nExample:\nimport math\nprint(math.sqrt(16))  # Output: 4.0")
    }

    modules={key:Modules(value[0],value[1]) for key, value in topic_description.items()}

    while True:
        print('\n_____ Learning Topics _____\n')
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
                    module=modules.get(choice)
                    if module:
                        module.display_info()
                        module.module_start()
                        module.module_complete()
                        run_quiz(choice,module)
            else:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please enter an integer.')


def run_quiz(topic,module):
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
        score=1 if user_answer.lower()==correct_answer.lower() else 0
        if score==1:
            print('_______ CORRECT! _______\n')
        else:
            print(f'_______ INCORRECT! _______\nThe correct answer is: {correct_answer}\n')

        module.update_score(score)
        mark_topic_completed(topic, score)