# Inheritance & Subclasses
## Inheritance: 
It is one of the most important concept of OOP. Inheritance allows a new class (child class) to inherit properties and methods from the parent class.

Other than inheriting the properties and behaviors, the child class also has the ability to modify those behaviors without making any changes to the parent class.

Inheritance allows you to establish an 'is-a' relationship.
#### Syntax:
``` python
class ParentClass:
    # parent class code

class ChildClass(ParentClass):      # Inheriting from ParentClass
    # child class code
```
* You have to specify the class you want to inherit from using ```()```.

#### Example:
``` python
class Vehicle:
    def __init__(self,brand,wheel):
        self.brand=brand
        self.wheel=wheel

    def info(self):
        print(f'Brand : {self.brand} | Wheel : {self.wheel}')

class Car(Vehicle):
    pass

car1=Car('BMW',4)
car2=Car('Tesla',4)

car1.info()
car2.info()

# ========================
# OUTPUT:

# Brand : BMW | Wheel : 4
# Brand : Tesla | Wheel : 4
```
* ```Car``` inherits from ```Vehicle```.
* ```Car``` automatically obtains attributes (```brand```,```wheel```) and method (```info()```) of ```Vehicle```.

## Adding New Functionalities in a Child Class and Method Overriding:
``` python
class Vehicle:
    def __init__(self,brand,wheel):
        self.brand=brand
        self.wheel=wheel

    def info(self):
        print(f'Brand : {self.brand} | Wheel : {self.wheel}')

class Car(Vehicle):
    def __init__(self,brand,wheel,fuel_type):
        super().__init__(brand,wheel)          # calling parent class constructor
        self.fuel_type=fuel_type             # new attribute

    def fuel_info(self):
        print(f'{self.brand} runs on {self.fuel_type}.')

    def info(self):             # Overriding the original method.
        print(f'Brand : {self.brand} | Wheel : {self.wheel} | Fuel Type : {self.fuel_type}')

car1=Car('BMW',4,'Gasoline')
car2=Car('Tesla',4,'Electric')

car1.fuel_info()
car2.fuel_info()

car1.info()             # calls the method from 'Car' instead of 'Vehicle'
car2.info()

# ========================
# OUTPUT:

# BMW runs on Gasoline.
# Tesla runs on Electric.
# Brand : BMW | Wheel : 4 | Fuel Type : Gasoline
# Brand : Tesla | Wheel : 4 | Fuel Type : Electric
```
* ```fuel_info()``` is a new method unique to the ```Car``` class.
* The ```info()``` method in ```Car``` class overrides the one from ```Vehicle``` class but doesn't make any changes to the original ```info()``` method.

## Types of Inheritance
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Heirarchical Inheritance
5. Hybrid Inheritance

### 1. Single Inheritance:
A class inherits from single parent class.
#### -> Pros:
- Simplicity – Easy to understand and implement.
- Less complexity – Minimal chances of conflicts.
- Encourages code reusability – The child class reuses the parent’s functionality.
#### -> Cons:
- Limited flexibility - Cannot inherit from multiple sources.
- Might lead to redundancy - If some other class needs similar functionalities, they must re-implement it seperately.
### 2. Multiple Inheritance:
Here a child class inherits from multiple parent class.

#### Example:
```python
class Vehicle:
    def __init__(self,brand,wheel):
        self.brand=brand
        self.wheel=wheel

class Engine:
    def __init__(self,engine_type):
        self.engine_type=engine_type

class Car(Vehicle,Engine):          # Inherits from both 'Vehicle' and 'Engine'
    def __init__(self,brand,wheel,engine_type):
        Vehicle.__init__(self,brand,wheel)
        Engine.__init__(self,engine_type)
    def info(self):
        print(f'{self.brand} has {self.wheel} wheels and has {self.engine_type} engine.')

car1=Car('BMW',4,'Petroleum')
car2=Car('Tesla',4,'Electric')

car1.info()
car2.info()

# ========================
# OUTPUT:

# BMW has 4 wheels and has Petroleum engine.
# Tesla has 4 wheels and has Electric engine.
```
- It should be used when an object shares the same characterstics from multiple sources.

- Avoid Multiple Inheritance unless necessary as it can make debugging complex.

#### -> Pros:
- Combines functionalities from different classes.
- No code duplication - Features from multiple parents are inherited.
- Encourages modularity - Can resuse specialized methods from different classes.
#### -> Cons:
- Possible name conflicts - if parents have methods with same name, it could possibly lead to some issue.
- Method Resolution Error (MRO) issues.
- Complexity increases – Managing multiple parent classes can be difficult.

### 3. Multilevel Inheritance:
A class can inherit from another child class, forming a chain.
```python
class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

class ElectricCar(Car):         # Inherits from Car
    def battery_info(self):
        print("This car has a battery.")

# Creating an object of the lowest-level class
ecar = ElectricCar()
ecar.vehicle_info()         # From 'Vehicle'
ecar.car_info()             # From 'Car'
ecar.battery_info()         # From 'ElectricCar'


# ========================
# OUTPUT:

# This is a vehicle.
# This is a car.
# This car has a battery.
```
* ```ElectricCar``` inherits from ```Car```, which inherits from ```Vehicle```.
* Each class in the chain can access all inherited methods.

#### -> Pros:
- Code reusability - Each level builds upon the previous one.
- Stepwise specialization - The base class provides generic functionality, while subclasses specialize further.
#### -> Cons:
- Increases dependency - If the parent class changes, it affects every other child class.
- Harder to debug - Bugs may span across multiple level.
- Deep hierarchies can make code harder to understand.
### 4. Heirarchical Inheritance:
Multiple child classes inherit from the same parent.
```python
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):             # First child class
    def drive(self):
        print("Car is being driven")

class Truck(Vehicle):           # Second child class
    def load_cargo(self):
        print("Truck is loading cargo")

car = Car()
truck = Truck()

car.move()          # Inherited method
truck.move()        # Inherited method
truck.load_cargo()


# ========================
# OUTPUT:

# Vehicle is moving
# Vehicle is moving
# Truck is loading cargo
```
#### -> Pros:
- Code reusability — The common functionality is in the base class.
- Encourages modularity — Different subclasses can extend the parent differently.
- Prevents duplicate code — All subclasses share a common base class.
#### -> Cons:
- Changes in the parent class affect all child classes — Can lead to unintended side effects.
- If a method is not in the parent each child must implement it separately.
### 5. Hybrid Inheritance:
A combination of multiple Inheritance types.
```python
class Engine:
    def engine_type(self):
        return "Electric"

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle, Engine):         # Hybrid inheritance
    def show_details(self):
        print(f"Car moves and has an {self.engine_type()} engine.")

car = Car()
car.move()          # From Vehicle
car.show_details()  # From Car

# ========================
# OUTPUT:

# Vehicle is moving
# Car moves and has an Electric engine.
```
#### -> Pros:
- Reusability - Uses existing structures efficiently.
- Enhances flexibility - Combines advantages of multiple inheritance types.
- Encapsulates different behaviors - Can mix functionalities from different sources.
#### -> Cons:
- Can be very complex — Hard to track method resolution.
- May lead to conflicts in method resolution — Must carefully manage dependencies.
- Debugging can be challenging — Finding errors in deep inheritance chains is hard.

## Composition:
Composition is a design principle in OOP where one object contains references to other objects in order to build more complex functionality.

Composition allows you to establish a 'has-a' relationship.

```python
class Engine:
    def start(self):
        print("Engine starting...")

class Wheel:
    def rotate(self):
        print("Wheel rotating...")

class Car:
    def __init__(self):
        # Composition: Car has Engine and Wheel
        self.engine = Engine()
        self.wheel = Wheel()

    def drive(self):
        self.engine.start()     # Using Engine's start method
        self.wheel.rotate()     # Using Wheel's rotate method

# Create a Car object
car = Car()
car.drive()
```
- The ```Car``` class doesn't inherit from ```Engine``` or ```Wheel```.
- The ```Car``` object is composed of instances of ```Engine``` and ```Wheel```, allowing it to use their methods.

Use composition when you need a "has-a" relationship or want to avoid tight coupling.

Inheritance is best when there is an "is-a" relationship and you need to extend behavior.