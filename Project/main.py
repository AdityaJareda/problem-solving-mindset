from modules.feedback import collect_feedback
from modules.learning import show_topics
from modules.progress import view_progress

main_menu={1: 'Learn a topic',
           2: 'View Progress',
           3: 'Provide Feedback',
           4: 'Exit'
           }

def display_menu():
    print('\n__________ Problem Solving Mindset __________')
    for key,value in main_menu.items():
        print(f'{key}. {value}')
    print('_____________________________________________\n')

def main():
    while True:
        display_menu()
        choice=input('Enter your choice: ').strip()

        try:
            choice=int(choice)

            if choice==1:
                show_topics()
            elif choice==2:
                view_progress()
            elif choice==3:
                collect_feedback()
            elif choice==4:
                print('Exiting...')
                break
            else:
                print('Invalid Input. Please Try Again.')
        except ValueError:
            print('Invalid Input. Please Enter a Number')

if __name__=='__main__':
    main()