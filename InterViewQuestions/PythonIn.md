### Basic Python Questions Repository  

Welcome to the **Basic Python Questions** repository! This repository contains an organized list of essential Python interview questions, ranging from fundamental concepts to intermediate-level topics, accompanied by concise answers and code examples.  

#### Table of Contents  
1. [Introduction](#introduction)  
2. [Key Features of Python](#key-features-of-python)  
3. [Difference Between Python 2 and Python 3](#difference-between-python-2-and-python-3)  
4. [Python as an Interpreted Language](#python-as-an-interpreted-language)  
5. [Python Data Types](#python-data-types)  
6. [List vs Tuple](#list-vs-tuple)  
7. [Functions in Python](#functions-in-python)  
8. [Understanding *args and **kwargs](#understanding-args-and-kwargs)  
9. [Global Interpreter Lock (GIL)](#global-interpreter-lock-gil)  
10. [Shallow vs Deep Copy](#shallow-vs-deep-copy)  
11. [Exception Handling](#exception-handling)  

### Introduction  
This repository is designed for Python learners and developers preparing for interviews or brushing up on Python fundamentals. Each section includes theoretical explanations and code examples for better understanding.  

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
Polymorphism allows objects of different classes to be treated as objects of a common super class. It can be achieved via method overriding or operator overloading.  

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
