# Task 5: Lists, Tuples, Dictionaries, and Sets

# 1. Lists:
'''
A list is a collection of items that:
1. Maintains order (items stay in their given sequence).
2. Allow duplicates.
3. Supports indexing and slicing.
4. Elements can be modified (add, remove, change).
5. Pro - Flexible.
6. Con - Memory overhead and performance issues (for large lists).
'''

grocery_list = ["Apples", "Bananas", "Carrots", "Tomatoes"]
grocery_list.append("Milk")             # Adds item at the end of the list
grocery_list.insert(2, "Bread")         # Inserts at index 2
grocery_list.remove("Carrots")          # removes item from the list
print("Updated Grocery List:", grocery_list)        # The updated list is printed


# 2. Tuples:
'''
A tuple is like a list but cannot be changed after creation.
1. Uses parentheses ( () instead of [] ).
2. Faster than lists (useful for fixed data).
3. Immutable (safer for read-only data).
4. Pro - Data Safety.
5. Con - Cannot update data.
'''

fruits = ("Apple", "Banana", "Cherry")
print("First Fruit:", fruits[0])        # prints first item


# 3. Dictionaries
'''
A dictionary stores data as key-value pairs.
1. Fast lookups/Access (compared to lists).
2. Keys must be unique, values can be duplicated.
3. Uses curly braces {}.
4. Pro - Fast Access and Clear Mapping.
5. Con - Ordering concept is different.
'''

grocery_prices = {"Apples": 2.5, "Bananas": 1.2, "Milk": 3.0}
print(grocery_prices["Apples"])           # Accessing value by key
grocery_prices["Eggs"] = 2.0            # Adding new item
print("Updated Grocery Prices:", grocery_prices)        # The updated dictionary is printed


# 4. Sets
'''
A set is a collection of unique elements.
1. Unordered (No specific order).
2. Duplicates are automatically removed.
3. Uses curly braces {} like dictionaries but without key-value pairs.
4. Pro - Fast membership testing and duplicate removal.
5. Con - Due to being unordered, you can't do Indexing/Slicing.
'''

grocery_set = {"Apples", "Bananas", "Milk", "Apples"}       # "Apples" is added only once
grocery_set.add("Eggs")         # Adding new item
print("Updated Grocery Set:", grocery_set)          # The updated set is printed

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print('Union: ',set1 | set2)      # prints union set
print('Intersection: ',set1 & set2)      # prints intersection
print('Difference: ',set1 - set2)     # prints difference