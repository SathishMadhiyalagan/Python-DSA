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

