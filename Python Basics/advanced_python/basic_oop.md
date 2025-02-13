# Introduction to Object-Oriented Programming [OOP]

OOP is a programming paradigm that helps in creating classes and objects for real world entities.

This is helpful when creating multiple objects/components which have unique properties but similar behaviors without having to repeat the same creation process again and again.

## OOP mainly consists of 4 features: 

1. Encapsulation - Helps in hiding data.

2. Abstraction - Helps in hiding the internal working of an object focusing only on what it does.

3. Inheritance - Helps in creating sub classes by inheriting the properties and behaviors from 
parent class.

4. Polymorphism - Depending on the object type, helps in performing the same method/function differently for different objects.

## Benefits of OOP:

1. Reusability

2. Modularity

3. Scalability

4. Security

5. Increasing performance

## Basic concepts of OOP:

### 1. Class:

- Class acts as a blueprint for creating objects.

- It helps in grouping together different attributes and methods into a single unit.

- SYNTAX:
    - ``` python
        class Class_Name:
        class_body
        ```

    - You can't leave the class_body empty as python doesn't allow empty blocks. Instead can write "pass" to create an empty class.

    - Use PascalCase when naming a class for best practice.

``` python
class Bike:
    wheel = 2           # class attribute

    def __init__(self,brand,color):     # constructor for initializing objects
        self.brand = brand              # instance attribute
        self.color = color

    def display_info(self):             # creating method
        print(f'Brand: {self.brand}\nColor: {self.color}\nWheels: {Bike.wheel}')
        print('--------------------')

# Creating objects:
bike1=Bike('Honda','Red')
bike2=Bike('BMW','White')

# Calling method:
bike1.display_info()
bike2.display_info()
```

### 2. Object:
#
- Objects are basically the instances of a class.

- They store the data(attributes) and behaviors(methods).

- E.G., bike1, bike2
### 3. Attributes:
#
- They are the data/variables stored within an object.

- E.G., wheel (class attribute), self.brand (instance variable)


### -> Class attribute: 

- Defined outside __init__().

- Shared by all instances of the class.

- Modifying a class attribute affects all other instances.

### -> Instance variable:

- Defined inside __init__().

- Unique to each object (not shared).

- Modifying an instance attribute does not affect other instances.


### 4. Methods:
#
- A method is basically a function defined inside a class and it operates on objects.

- E.G., display_info(self)


# QUESTIONS:

Q1. What happens when you:
- CASE 1 - define an object "car1" inside a method of a class and then, define the same object "car1" outside the class?
- CASE 2 - define an object "car1" inside  __init()__ and then, define the same object "car1" outside the class using __init__()?

### CASE 1 SOLUTION:

``` python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def create_car_inside(self):
        car1 = Car("BMW", "Blue")  # Local object (only exists inside this method)
        print(f"Inside method: {car1.brand}, {car1.color}")

# Creating an object outside
car1 = Car("Tesla", "Red")
car1.create_car_inside()  # Output: Inside method: BMW, Blue

print(car1.brand, car1.color)  # Output: Tesla Red
```

- The object inside the class is temporary and executes when the method is called and disappears when the method finishes executing.

- The object outside the class is independent and does not get replaced.

### CASE 2 SOLUTION:

``` python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.car1 = Car("Dummy", "Black")  # Creating another object inside __init__

# Creating an object outside
car1 = Car("Tesla", "Red")
```
- This will cause a ```RecursionError: maximum recursion depth exceeded```.
- This keeps repeating infinitely until Python stops execution.
#
Q2. Can we define a class without using class keyword?

#### Solution:
- Instead of ```class``` keyword you can use ```type()```.
- Using ```type()``` you can dynamically create a class at runtime. 
``` python
Car = type('Car', (), {'wheels': 4, 'show': lambda self: f"This car has {self.wheels} wheels"})
```
1. ```'Car'``` - Name of the class.
2. ```()``` - Parent classes (empty tuple means no inheritance).
3. ```{}``` - Dictionary defining attributes and methods.

- It is useful in metaprogramming but not recommended for regular OOP programming.
- Using ```class``` is easier and better for most use cases.
#
Q3. We know ```__init__()``` constructor is used for initializing the object's attributes. What will happens when we don't define ```__init__()``` constructor.

#### SOLUTION:
- if you don’t define it, the class won’t initialize any attributes automatically, and you'll have to manually assign them after creating an object.
``` python
class Car:
    pass                # No constructor (__init__ method)

# Creating an object
car1 = Car()

# Manually assigning attributes
car1.brand = "Tesla"
car1.color = "Red"

print(car1.brand)       # Tesla
print(car1.color)       # Red
```
- The class itself does nothing when we create ```car1```.
- We have to manually add ```brand``` and ```color``` attributes after object creation.
- If a class requires attributes, always use ```__init__()``` to ensure they are assigned at object creation.
#
Q4. What Happens If We Don’t Write ```self``` parameter in ```__init__()``` constructor?

#### SOLUTION:
- The ```self``` parameter refers to the instance of the class that is being created.
- If we don’t write ```self```, Python won’t know which object to assign values to.
- Python automatically passes the object (self) as the first argument, but if ```self``` is missing, Python treats the first real argument as ```self``` by mistake, causing an error.
#
Q5.Is __init__() Really a Constructor? Meaning of Double Underscores ```__``` in ```__init__()```

#### SOLUTION:
- Yes, ```__init()___``` acts as a constructor in Python.
- It runs automatically when an object is created.
- It assigns values to instance attributes.
- ```__init()___``` has double underscores because it is a Dunder (Double UNDerscore) Method.
    - Dunder methods are special built-in methods in Python that start and end with double underscores ```__```, also called magic methods.
#
Q6. Why are we making methods in every class? If I want to do addition, I can make an addition function but why don't I define that function(method) in the class ? it takes less memory space and also fasten the program.

#### SOLUTION:
### Singleton Function (Function outside of class):
- When a function performs a simple calculation and doesn’t need object-specific behavior, we can use a standalone function.
- This is more efficient because:
    - The function is independent.
    - It doesn’t store extra data, reducing memory usage.
    - It can be used anywhere without needing a class.
### Method (Function inside class):
- When a function needs to store state or interact with object attributes.
- This is more efficient because:
    - The method has memory.
    - Each object can have separate histories.
    - It groups related functions together in the same class.
#
Q7. what will happen when we assign one object to another object?

#### SOLUTION:
- When we assign one object to another object, both variables refer to the same object.
``` python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Creating an object
car1 = Car('Tesla', 'Red')

# Assigning car1 to car2
car2 = car1

# Modifying car2
car2.color = 'Blue'

# Checking both objects
print(car1.color)  # Output: Blue
print(car2.color)  # Output: Blue
```
- Changing ```car2.color``` to ```'Blue'``` also changes ```car1.color```, because both point to the same memory location.

#### Ways to create a copy of an object:
- #### Shallow Copy (Using ```copy.copy()```):
    - Creates a new object, but references inside remain shared.
    ``` python
    import copy

    car1 = Car("Tesla", "Red")
    car2 = copy.copy(car1)  # Creating a shallow copy

    car2.color = "Blue"

    print(car1.color)       # Output: Red
    print(car2.color)       # Output: Blue
    ```
    - Now ```car1``` and ```car2``` are separate objects.
    - Modifying ```car2.color``` does not affect ```car1.color```.
- #### Deep Copy (Using ```copy.deepcopy()```):
    - Creates a completely independent copy, including nested objects.
    ``` python
    car1 = Car("Tesla", "Red")
    car2 = copy.deepcopy(car1)  # Creating a deep copy
    ```
    - Use deep copy when your object contains lists, dictionaries, or other objects inside.
#
Q8. Can we create a class with no attribute but only methods? If yes, then how is it useful?

#### SOLUTION:
- Yes, we can create a class containing only methods and no attributes. But, it's only helpful in certain cases:
    - When you need a utility class with helper functions.
    - When defining abstract base classes for other classes to follow.
    - When implementing shared behaviors without storing data.
- NOTE - If you only need a single function, create a module with function instead of a class.
#
Q9. Is It Compulsory to Create an Object from a Class?

#### SOLUTION:
- It isn't compulsory, in fact object creation depends on your use case.
- Objects are created when we want to:
    - Store unique data for each instance.
    - Use instance method.

- When we don't need to create an object:
    - When using static methods:
        - Static methods doesn't depend on instance data.
        - An object is not required to call a static method.
    - When using abstract classes:
        - An abstract class acts as a blueprint for child classes and Methods defined in it must be implemented in child classes. So, you cannot create classes for abstract class
    - When using only class attributes and class methods:
        - You don't need an object when defining a class-level attributes and methods.
        - You can directly access class methods using class name.
#
Q10. What is instance dictionary?

#### SOLUTION:
- Every objects's attributes are stored in an internal dictionary. This dictionary is called the instance dictionary, and it can be accessed using the special attribute ```__dict__```.
- ```__dict__``` is a built-in attribute of an object that stores all instance attributes in the form of a dictionary (key-value pairs).

``` python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Creating an Object
car1 = Car("Tesla", "Red")

# Printing Instance Dictionary
print(car1.__dict__)


# OUTPUT:
{'brand': 'Tesla', 'color': 'Red'}
```

- This allows Python to dynamically store and access attributes without a fixed structure.
``` python
car1.year = 2023        # Adding a new attribute dynamically

print(car1.__dict__)


# OUTPUT:
{'brand': 'Tesla', 'color': 'Red', 'year': 2023}
```

- ```year``` was not defined in the class, but Python allows us to add it dynamically.

#### Instance vs. Class Dictionary:
- Classes also have their own ```__dict__```, which stores class attributes.
``` PYTHON
class Car:
    wheels = 4          # Class Attribute

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Print Class Dictionary
print(Car.__dict__)  

# Create Object and Print Instance Dictionary
car1 = Car('BMW', 'Black')
print(car1.__dict__)


# OUTPUT:
{
  '__module__': '__main__',
  'wheels': 4,          # Class Attribute
  '__init__': <function Car.__init__ at 0x000002D4>,
  '__dict__': <attribute '__dict__' of 'Car' objects>,
  '__weakref__': <attribute '__weakref__' of 'Car' objects>,
  '__doc__': None
}

{'brand': 'BMW', 'color': 'Black'}
```
- ```Car.__dict__``` contains class attributes and metadata.
- ```car1.__dict__``` contains only instance attributes (no wheels because it's a class attribute).

#### ```__dict__``` should be used when:
1. Debugging
2. Dynamically modifying attributes at runtime.
#
Q11. If we create multiple instances, it increases memory overhead so what we have to do to avoid this?

#### SOLUTION:
- Every time we create an object, Python allocates memory for its attributes, and each object stores its own instance attributes seperately. This increases memory usage.

#### Ways to reduce memory overhead:
1. Using ```__slots__```:
    - By default, Python stores instance attributes in a dictionary (```__dict__```), which takes extra memory. We can prevent this using ```__slots__```.
    ``` python
    class Car:
        __slots__ = ['brand', 'color']  # Restricts attributes, removes `__dict__`

        def __init__(self, brand, color):
            self.brand = brand
            self.color = color

    car1 = Car("Tesla", "Red")
    # print(car1.__dict__)              # ERROR: `__dict__` no longer exists!

    print(car1.brand)      # Tesla
    ```
    - Saves memory by preventing the creation of a dictionary (```__dict__```).
    - Instead, Python allocates fixed memory for brand and color.

2. Using Class Attributes instead of Instance Attributes:
    - If an attribute's value is shared among all instances, store it as a class attribute instead of an instance attribute.
#
Q12. Does a class get stored in memory even before we create an object?

#### SOLUTION:
- Yes, a class gets stored in memory as soon as it is defined, even before creating any objects.
- This happens because Python treates everything as an object, even classes.
1. When Python encounters a ```class``` definition, it:
    - Creates a class object in memory.
    - Stores attributes and methods inside the class object.
    - Links the class to its parent (object by default).
2. When you create an object (instance), Python:
    - Allocates memory for a new instance.
    - Copies the class structure into the instance.
    - Stores instance-specific attributes separately.
#
Q13. How to ensure that an attribute is only accessible inside the class?

#### SOLUTION:
- To make an attribute only accessible inside the class, use double underscores (```__```) before the attribute name.
``` python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number    # Public attribute
        self.__balance = balance                # Private attribute

    def show_balance(self):                     # Method to access private attribute
        print(f"Your balance is: ₹{self.__balance}")

# Creating an object
account = BankAccount("12345", 1000)

print(account.account_number)                   # Works fine (Public attribute)
print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'
```
- ```account_number``` is public, so it can be accessed outside the class.
- ```__balance``` is private, so it cannot be accessed directly from outside.
- Python uses name mangling to change ```__balance``` internally to ```_BankAccount__balance```.
This prevents accidental access but still allows access if necessary.
Q13. Can you create unlimited object inside a class? If yes, how can you restrict the number of objects to be create inside a class?

#### SOLUTION:
- Yes! In Python, there is no built-in limit to the number of objects you can create from a class.

#### Way to restrict number of objects:
- You can restrict the number of objects using a class attribute (or counter method).
- You can use a class attribute to keep track of the number of objects created and prevent more than a set limit.
```python
class Car:
    instances = 0               # Class attribute to count instances
    MAX_INSTANCES = 3           # Limit

    def __init__(self, brand, color):
        if Car.instances >= Car.MAX_INSTANCES:
            raise Exception("Cannot create more than 3 cars!")  # Restrict object creation
        self.brand = brand
        self.color = color
        Car.instances += 1      # Increment count

# Creating objects
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")
car3 = Car("Audi", "Blue")

# Attempting to create the fourth object will raise an error
car4 = Car("Ford", "White")     # Exception: Cannot create more than 3 cars!
```
- The ```instances``` counter tracks the number of created objects.
- If the number exceeds ```MAX_INSTANCES```, an exception is raised.
- Objects ```car1```, ```car2```, and ```car3``` are created successfully, but ```car4``` causes an error.
