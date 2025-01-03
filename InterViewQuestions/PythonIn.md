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

