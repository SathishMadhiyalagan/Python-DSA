### Basic Python Questions Repository  

---

### Key Features of Python  
Python is a powerful and versatile programming language. Its notable features include:  
- Easy to learn and use  
- Interpreted and dynamically typed  
- High-level language with extensive libraries  
- Platform independent  
- Ideal for diverse domains like web development, data analysis, and machine learning  

---

### Difference Between Python 2 and Python 3  
| Feature           | Python 2                | Python 3                |  
|--------------------|-------------------------|-------------------------|  
| Print Statement    | `print` statement       | `print()` function      |  
| Unicode Handling   | ASCII by default        | Unicode by default      |  
| Integer Division   | Truncates to integer    | Returns float           |  
| Maintenance        | Ended in 2020          | Actively maintained     |  

---

### Python as an Interpreted Language  
Python executes code line by line, translating it into machine-readable instructions at runtime.  

---

### Python Data Types  
Python supports various built-in data types, including:  
- Numeric: `int`, `float`, `complex`  
- Sequence: `list`, `tuple`, `range`  
- Text: `str`  
- Set Types: `set`, `frozenset`  
- Mapping: `dict`  
- Boolean: `bool`  
- Binary: `bytes`, `bytearray`, `memoryview`  

---

### List vs Tuple  
| Attribute     | List              | Tuple             |  
|---------------|-------------------|-------------------|  
| Mutability    | Mutable           | Immutable         |  
| Syntax        | `[1, 2, 3]`       | `(1, 2, 3)`       |  
| Performance   | Slower            | Faster            |  
| Use Case      | Dynamic data      | Static data       |  

---

### Functions in Python  
Functions in Python are defined using the `def` keyword:  
```python  
def function_name(parameters):  
    """Optional docstring"""  
    # Function body  
    return result  
```  

---

### Understanding *args and **kwargs  
- `*args`: For variable-length positional arguments.  
- `**kwargs`: For variable-length keyword arguments.  

Example:  
```python  
def demo_function(*args, **kwargs):  
    print(args, kwargs)  

demo_function(1, 2, key1="value1", key2="value2")  
```  

---

### Global Interpreter Lock (GIL)  
The GIL is a mutex in CPython to ensure thread safety but can limit parallel thread execution in CPU-bound tasks.  

---

### Shallow vs Deep Copy  
| Copy Type     | Description                               | Example Code                       |  
|---------------|-------------------------------------------|-------------------------------------|  
| Shallow Copy  | Copies the outer object, references inner | `copy.copy(original)`              |  
| Deep Copy     | Copies both outer and inner objects       | `copy.deepcopy(original)`          |  

---

### Exception Handling  
Python exceptions are managed using `try-except` blocks:  
```python  
try:  
    result = 10 / 0  
except ZeroDivisionError:  
    print("Cannot divide by zero.")  
finally:  
    print("Execution complete.")  
```  

---

---

### **Intermediate Python Questions and Answers**  

---

**1. Explain Python's `is` vs `==`.**  
- **`is`**: Checks if two objects refer to the same memory location (identity).  
- **`==`**: Checks if two objects have the same value (equality).  

Example:  
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, as values are the same
print(a is b)  # False, as they are different objects
```

---

**2. What are Python decorators?**  
Decorators are functions that modify the behavior of another function or method. They are applied using the `@decorator_name` syntax.  

Example:  
```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def my_function():
    print("Hello!")

my_function()
# Output:
# Before function call
# Hello!
# After function call
```

---

**3. How does Python handle memory management?**  
- Python uses **automatic garbage collection** to manage memory.  
- Objects are stored in a private heap space.  
- **Reference counting** is used to track objects, and a cyclic garbage collector handles circular references.  
- Unused memory is deallocated automatically.

---

**4. What is the purpose of the `with` statement?**  
The `with` statement simplifies resource management by ensuring proper acquisition and release of resources, such as closing files or managing locks.  

Example:  
```python
with open("file.txt", "r") as file:
    content = file.read()
# The file is automatically closed after the block.
```

---

**5. Explain list comprehension with an example.**  
List comprehension is a concise way to create lists.  

Example:  
```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

**6. What are Python generators?**  
Generators are functions that yield values one at a time using the `yield` keyword, allowing for lazy evaluation and efficient memory usage.  

Example:  
```python
def my_generator():
    for i in range(3):
        yield i

for value in my_generator():
    print(value)
# Output:
# 0
# 1
# 2
```

---

**7. Explain the difference between Python's `deepcopy` and `copy`.**  
- **`copy`**: Creates a shallow copy where changes to nested objects reflect in both copies.  
- **`deepcopy`**: Creates an independent copy, including nested objects, ensuring no shared references.  

Example:  
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 10
print(original)  # Affects original: [[10, 2], [3, 4]]

deep[0][0] = 20
print(original)  # Unaffected: [[10, 2], [3, 4]]
```

---

**8. How can you merge two dictionaries in Python?**  
- Using the `update()` method:  
```python
dict1 = {'a': 1}
dict2 = {'b': 2}
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2}
```

- Using the `**` operator (Python 3.5+):  
```python
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2}
```

- Using the `|` operator (Python 3.9+):  
```python
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 2}
```

---

**9. What is the difference between `isinstance()` and `type()`?**  
- **`isinstance()`**: Checks if an object is an instance of a class or subclass.  
- **`type()`**: Checks the exact type of an object.  

Example:  
```python
print(isinstance(5, int))  # True
print(isinstance(True, int))  # True (bool is a subclass of int)

print(type(5) == int)  # True
print(type(True) == int)  # False
```

---

**10. How do you manage Python's `pip` and virtual environments?**  
- Install packages using `pip`:  
```bash
pip install package_name
```

- Create a virtual environment using `venv`:  
```bash
python -m venv env
```

- Activate the virtual environment:  
  - **Windows**:  
    ```bash
    env\Scripts\activate
    ```
  - **Linux/Mac**:  
    ```bash
    source env/bin/activate
    ```

- Deactivate the virtual environment:  
```bash
deactivate
```



---
---

### **OOP Concepts in Python - Questions and Answers**

---

**1. What is object-oriented programming (OOP)?**  
OOP is a programming paradigm that uses **objects** to model real-world entities. These objects encapsulate data (attributes) and behavior (methods), making code modular, reusable, and easier to maintain. Core principles include:  
- **Encapsulation**  
- **Inheritance**  
- **Polymorphism**  
- **Abstraction**

1. Encapsulation: Bundling data and methods within a single unit (class) and restricting direct access to some components.
2. Inheritance: Mechanism to create new classes based on existing classes.
3. Polymorphism: Ability to use a single interface for different data types or classes.
4. Abstraction: Hiding complex implementation details and showing only the necessary features of an object.

---

**2. Define class and object in Python.**  
- **Class**: A blueprint for creating objects, defining attributes and methods.  
- **Object**: An instance of a class, representing a specific entity.

Example:  
```python
class Animal:
    def __init__(self, name):
        self.name = name

dog = Animal("Dog")  # Object creation
print(dog.name)  # Output: Dog
```

---

**3. Explain encapsulation with an example.**  
Encapsulation restricts access to certain attributes or methods using private or protected access specifiers.  

Example:  
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

emp = Employee("John", 50000)
print(emp.get_salary())  # Output: 50000
# print(emp.__salary)  # Error: AttributeError
```

---

**4. What is abstraction in Python?**  
Abstraction hides complex details and exposes only essential features. In Python, it is achieved using abstract base classes (`ABC`) from the `abc` module.  

Example:  
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

---

**5. What is polymorphism in Python?**  
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It can be achieved via method overriding or operator overloading.  

Example:  
```python
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

def flying_test(bird):
    bird.fly()

flying_test(Bird())     # Output: Bird can fly
flying_test(Penguin())  # Output: Penguin can't fly
```

---

**6. What is the `self` parameter in Python?**  
`self` refers to the instance of the class. It is used to access attributes and methods of the class within the class itself.  

Example:  
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

p = Person("Alice")
p.greet()  # Output: Hello, my name is Alice
```

---

**7. Explain multiple inheritance with a conflict resolution example.**  
Python uses the **Method Resolution Order (MRO)** to resolve conflicts in multiple inheritance.  

Example:  
```python
class A:
    def greet(self):
        print("Hello from A!")

class B:
    def greet(self):
        print("Hello from B!")

class C(A, B):
    pass

obj = C()
obj.greet()  # Output: Hello from A! (follows MRO)
```

---

**8. How is operator overloading achieved in Python?**  
Operator overloading is achieved by defining special methods (e.g., `__add__`, `__sub__`) for operators.  

Example:  
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)
result = v1 + v2  # Calls __add__
print(result.x, result.y)  # Output: 6 8
```

---

**9. What is the difference between protected and private attributes?**  
- **Protected Attributes**: Prefix with a single underscore (`_`). Accessible within the class and subclasses.  
- **Private Attributes**: Prefix with double underscores (`__`). Accessible only within the class.  

Example:  
```python
class MyClass:
    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"

obj = MyClass()
print(obj._protected)  # Output: Protected
# print(obj.__private)  # Error: AttributeError
```

---

**10. How does Python achieve dynamic binding?**  
Python achieves dynamic binding by resolving method calls at runtime. This supports polymorphism, allowing a derived class's method to override the base class's method.  

Example:  
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Dog()
animal.speak()  # Output: Dog barks
```

---

---

### **Advanced Python Questions and Answers**

---

**1. Explain Python's metaclasses.**  
Metaclasses define the behavior of classes and are used to control class creation. In Python, `type` is the default metaclass. Custom metaclasses are created by subclassing `type`.  

Example:  
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['greet'] = lambda self: f"Hello from {name}!"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.greet())  # Output: Hello from MyClass!
```

---

**2. How do you implement abstract classes in Python?**  
Abstract classes are created using the `abc` module. They serve as blueprints for subclasses and cannot be instantiated directly.  

Example:  
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark!"

dog = Dog()
print(dog.sound())  # Output: Bark!
```

---

**3. What are Python's descriptors?**  
Descriptors are objects that manage attribute access in other objects. They define methods like `__get__`, `__set__`, and `__delete__`.

Example:  
```python
class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class MyClass:
    attr = Descriptor("attr")

obj = MyClass()
obj.attr = 42
print(obj.attr)  # Output: 42
```

---

**4. What are coroutines in Python?**  
Coroutines are a special type of generator used for asynchronous programming. They can `await` results instead of blocking execution.  

Example:  
```python
import asyncio

async def greet():
    await asyncio.sleep(1)
    return "Hello!"

async def main():
    result = await greet()
    print(result)

asyncio.run(main())  # Output: Hello!
```

---

**5. Explain Python's context managers.**  
Context managers handle resource management (e.g., file handling). They use the `with` statement and define `__enter__` and `__exit__` methods.  

Example:  
```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContext():
    print("Inside context")
# Output:
# Entering context
# Inside context
# Exiting context
```

---

**6. How does Python's garbage collector work?**  
Python uses reference counting and a cyclic garbage collector to manage memory.  
- **Reference Counting**: An object is destroyed when its reference count drops to zero.  
- **Cyclic Garbage Collector**: Handles reference cycles where objects reference each other.

---

**7. What is the `yield` keyword used for?**  
The `yield` keyword is used to create generators. It pauses the function and returns a value but retains its state for subsequent calls.

Example:  
```python
def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)
# Output:
# 1
# 2
# 3
```

---

**8. Explain Python's `asyncio` module.**  
The `asyncio` module is used for writing concurrent code using async/await syntax. It handles asynchronous tasks and I/O-bound operations.

Example:  
```python
import asyncio

async def task(name):
    print(f"Task {name} starts")
    await asyncio.sleep(1)
    print(f"Task {name} ends")

async def main():
    await asyncio.gather(task("A"), task("B"))

asyncio.run(main())
# Output:
# Task A starts
# Task B starts
# Task A ends
# Task B ends
```

---

**9. What are Python slots, and how do you use them?**  
`__slots__` limit the attributes of a class to a predefined set, saving memory by preventing the creation of a `__dict__`.  

Example:  
```python
class MyClass:
    __slots__ = ['x', 'y']

obj = MyClass()
obj.x = 10
obj.y = 20
# obj.z = 30  # AttributeError: 'MyClass' object has no attribute 'z'
```

---

**10. What is monkey patching in Python?**  
Monkey patching dynamically modifies or extends a class or module at runtime.  

Example:  
```python
class MyClass:
    def greet(self):
        return "Hello!"

def new_greet(self):
    return "Hi!"

MyClass.greet = new_greet  # Monkey patching
obj = MyClass()
print(obj.greet())  # Output: Hi!
```

---
---

## File Handling

### 1. How do you read and write files in Python?
Use the built-in `open()` function to read and write files. You can use modes like `'r'` (read), `'w'` (write), `'a'` (append), and `'rb'` (read binary).

```python
# Writing to a file
with open('file.txt', 'w') as file:
    file.write("Hello, World!")

# Reading from a file
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
```

### 2. What is the difference between `rb` and `r` modes in file handling?
- `'r'` mode opens the file in text mode, meaning data is read as a string.
- `'rb'` mode opens the file in binary mode, where data is read as bytes.

### 3. How do you handle binary files in Python?
To read and write binary files, use `'rb'` and `'wb'` modes with `open()`. Binary data is handled as `bytes` objects.

Example:
```python
with open('image.jpg', 'rb') as file:
    data = file.read()
```

### 4. What is the use of the `seek()` method?
The `seek()` method moves the file pointer to a specified position. It allows random access to a file, meaning you can read/write from any part of the file.

Example:
```python
with open('file.txt', 'r') as file:
    file.seek(10)  # Moves pointer to 10th byte
    print(file.read())  # Reads content from the 10th byte onward
```

### 5. How can you handle file exceptions in Python?
File-related exceptions can be handled using `try-except` blocks, such as `FileNotFoundError`, `PermissionError`, etc.

Example:
```python
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```

### 6. Explain the difference between `open()` and `with open()`.
- `open()` simply opens a file and returns a file object, but you must manually close it using `close()`.
- `with open()` is used for better resource management. It automatically closes the file after the block of code is executed.

---

## Data Structures

### 1. What are Python's built-in data structures?
Python includes the following built-in data structures:
- **List**: Ordered, mutable, allows duplicate elements.
- **Tuple**: Ordered, immutable, allows duplicate elements.
- **Set**: Unordered, mutable, does not allow duplicate elements.
- **Dictionary**: Unordered, mutable, key-value pairs.

### 2. How do you implement a stack in Python?
A stack can be implemented using a list with `append()` (push) and `pop()` methods.

Example:
```python
stack = []
stack.append(1)  # Push
stack.append(2)
print(stack.pop())  # Pop
```

### 3. Explain the difference between a set and a frozenset.
- **Set**: Mutable; elements can be added or removed.
- **Frozenset**: Immutable; cannot be modified once created.

### 4. How do you implement a queue in Python?
A queue can be implemented using the `collections.deque` class, which provides an efficient way to append and pop elements from both ends.

Example:
```python
from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
print(queue.popleft())  # Dequeue
```

### 5. How do you sort a dictionary by keys or values?
- To sort by keys: `sorted(dictionary)`
- To sort by values: `sorted(dictionary.items(), key=lambda x: x[1])`

Example:
```python
d = {'b': 2, 'a': 1, 'c': 3}
print(sorted(d))  # Sort by keys
print(sorted(d.items(), key=lambda x: x[1]))  # Sort by values
```

### 6. What are Python's `defaultdict` and `Counter`?
- **`defaultdict`**: A subclass of `dict` that provides a default value for missing keys.
```python
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d['a'])  # Output: 1
```
- **`Counter`**: A subclass of `dict` designed to count hashable objects.
```python
from collections import Counter

c = Counter('abracadabra')
print(c)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

---

## Libraries and Frameworks

### 1. What is the purpose of the NumPy library?
NumPy is a library for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

Example:
```python
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr + 1)  # Output: [2 3 4 5]
```

### 2. Explain pandas DataFrames.
A `DataFrame` in pandas is a 2-dimensional labeled data structure with columns of potentially different types. It is similar to a table or a spreadsheet.

Example:
```python
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)
```

### 3. What is the use of the Matplotlib library?
Matplotlib is a plotting library used for creating static, animated, and interactive visualizations in Python. It is widely used for data visualization.

Example:
```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()
```

### 4. How does Django differ from Flask?
- **Django**: A full-stack, high-level framework that comes with built-in features such as authentication, database ORM, and an admin panel.
- **Flask**: A lightweight micro-framework with minimal features, allowing you to choose additional components for your project.

### 5. What is Pytest, and how do you use it?
Pytest is a testing framework for Python. It simplifies the process of writing simple and scalable test cases.
Example:
```python
def test_addition():
    assert 1 + 1 == 2
```
Run tests with:
```bash
pytest
```

### 6. What are Python's asyncio and threading libraries used for?
- **`asyncio`**: A library for writing asynchronous programs using `async` and `await` syntax. It is used for I/O-bound tasks.
- **`threading`**: A library for creating concurrent threads of execution. It is suitable for CPU-bound tasks that can run in parallel.

---

## Python and Databases

### 1. How do you connect to a database using Python?
You can use libraries such as `sqlite3`, `MySQLdb`, or `psycopg2` to connect to databases.

Example for SQLite:
```python
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
conn.close()
```

### 2. What is the difference between MySQL and SQLite?
- **MySQL**: A full-fledged database management system that requires a server and is suited for large-scale applications.
- **SQLite**: A lightweight, file-based database used for smaller, less complex applications.

### 3. How do you execute a SQL query in Python?
You can use libraries like `sqlite3` or `mysql.connector` to execute SQL queries.

Example for SQLite:
```python
cursor.execute("SELECT * FROM users")
```

### 4. What is an ORM in Python?
ORM (Object-Relational Mapping) is a technique for converting between incompatible types (objects and database rows). Libraries like Django ORM and SQLAlchemy provide this abstraction layer.

### 5. How does Django's ORM work?
Django's ORM allows you to interact with the database using Python objects. You define models as classes, and Django automatically handles the SQL queries.

Example:
```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
```
You can query the database using:
```python
User.objects.all()
```

---

