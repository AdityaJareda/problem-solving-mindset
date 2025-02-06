# Task 8: Loops - for Loop

# for Loop: Used to iterate over a sequence and execue a block of code for each item in that sequence.


# for item in sequence:
     # block of code

# item: This represents the current element from the sequence.
# sequence: This is the collection of items (like a list, string, or range).
# block of code: The block of code you want to repeat for each item.


learning_topics = ['Variables', 'Data Types', 'Operators', 'Conditional Statements', 'Loops']

for topic in learning_topics:              # iterates over the list and prints 'Topic: ' followed by the current topic.
    print(f'Topic: {topic}')


# Using range():

print('\nCountdown: ')
for i in range(3,0,-1):                     # Here range(start,stop,step) is used.
    print(i)                                

'''
start = 3: The sequence starts at 3.
stop = 0: The sequence ends just before 0 (meaning 0 will not be included).
step = -1: The sequence decreases by 1 with each iteration.
'''



# for loop with indexing:

print()
for index, topic in enumerate(learning_topics, start=1):
    print(f'{index}. {topic}')