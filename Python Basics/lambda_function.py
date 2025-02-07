# Task 12: Lambda Functions & Higher Order Functions

# Lambda Function: Similar to a normal function but written in a single line. It can have any number of arguments but only one expression.

# Lambda functions are useful when you need a simple function for a short period of time (for example, inside another function).

# Syntax:
# lambda arguments: expression

# 1. Normal vs lambda function:

def square1(x):
    return x * x

print('Normal Function:', square1(5))


square2 = lambda x: x * x
print('Lambda Function:', square2(10))

print('-----------------------------------------------------')


# 3. lambda function with multiple arguments:

add = lambda x, y: x + y
print(add(3, 7))

print('-----------------------------------------------------')



# Higher-Order Functions: Takes another function as an argument or returns a function.

# 1. Using map() with lambda:

# map() - Applies a function to each element of a list.

numbers1 = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers1))          # map() applies lambda x:x*x to each element of the list.
print(squared_numbers)

print('-----------------------------------------------------')


# 2. Using filter() with lambda:

# filter() - Selects elements that meet a condition.

numbers2 = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers2))     # Filters out the even numbers.
print(even_numbers)

print('-----------------------------------------------------')


# 3. Using sorted() with Lambda:

points = [("Player1", 1025), ("Player2", 920), ("Player3", 1122)] 

leaderboard = sorted(points, key=lambda point: point[1], reverse=True)      # Sorts in descending order.

print(leaderboard)
