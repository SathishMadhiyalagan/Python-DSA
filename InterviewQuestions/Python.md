
# 🐍 Python Interview Questions with Answers

This document contains **detailed answers** to the top Python interview questions.

---

## 1. What are Python’s key features?
Python is a high-level, dynamically typed, and interpreted programming language. Some key features include:
- **Simple & Readable**: Uses an easy-to-read syntax.
- **Dynamically Typed**: No need to declare variable types.
- **Interpreted Language**: Code runs line by line without compilation.
- **Object-Oriented & Functional**: Supports both paradigms.
- **Extensive Libraries**: Includes built-in and third-party modules.
- **Cross-Platform**: Runs on Windows, macOS, and Linux.

---

## 2. What is the difference between `is` and `==`?
- `is` checks **identity** (whether two objects refer to the same memory location).
- `==` checks **equality** (whether values are the same).

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (values are the same)
print(a is b)  # False (different memory locations)
```

---

## 3. How does Python manage memory?
Python uses **automatic memory management** with:
- **Reference Counting**: An object is deleted when no references exist.
- **Garbage Collection (GC)**: Removes cyclic references.
- **Memory Pooling**: Uses memory blocks for small objects.

You can manually control garbage collection using:
```python
import gc
gc.collect()  # Force garbage collection
```

---

## 4. What are mutable and immutable data types in Python?
- **Mutable**: Can be modified after creation.
  - Lists (`list`), Dictionaries (`dict`), Sets (`set`).
- **Immutable**: Cannot be changed after creation.
  - Strings (`str`), Tuples (`tuple`), Integers (`int`).

Example:
```python
x = "hello"
x[0] = "H"  # ❌ Error, strings are immutable
```

---

## 5. What is list comprehension? Provide an example.
List comprehension is a concise way to create lists.

Example:
```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```
Equivalent to:
```python
squares = []
for x in range(5):
    squares.append(x**2)
```

---

## 6. What is the difference between a shallow copy and a deep copy?
- **Shallow Copy**: Copies object reference (changes reflect in both copies).
- **Deep Copy**: Creates an independent copy of the object.

Example:
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99
print(shallow)  # [[99, 2, 3], [4, 5, 6]]
print(deep)     # [[1, 2, 3], [4, 5, 6]]
```

---

## 7. What is the difference between a Python list and a tuple?
| Feature  | List (`list`) | Tuple (`tuple`) |
|----------|-------------|--------------|
| Mutability | ✅ Mutable | ❌ Immutable |
| Performance | ❌ Slower | ✅ Faster |
| Memory | ❌ More memory | ✅ Less memory |
| Syntax | `[]` | `()` |

Example:
```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
```

---

## 8. What are `*args` and `**kwargs` in Python?
- `*args`: Allows passing **multiple positional arguments** as a tuple.
- `**kwargs`: Allows passing **multiple keyword arguments** as a dictionary.

Example:
```python
def greet(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

greet("Hello", "Python", name="John", age=25)
# Args: ('Hello', 'Python')
# Kwargs: {'name': 'John', 'age': 25}
```

---

## 9. What is the difference between `@staticmethod`, `@classmethod`, and instance methods?
| Type | Uses `self`? | Uses `cls`? | Can access instance variables? | Can access class variables? |
|------|------------|------------|--------------------------|----------------------|
| Instance Method | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Class Method | ❌ No | ✅ Yes | ❌ No | ✅ Yes |
| Static Method | ❌ No | ❌ No | ❌ No | ❌ No |

Example:
```python
class MyClass:
    def instance_method(self):
        return "Instance method", self

    @classmethod
    def class_method(cls):
        return "Class method", cls

    @staticmethod
    def static_method():
        return "Static method"

obj = MyClass()
print(obj.instance_method())  # Uses self
print(MyClass.class_method()) # Uses cls
print(MyClass.static_method()) # No self or cls
```

---

## 10. What is the difference between Python generators and iterators?
- **Iterator**: An object that can be iterated using `__iter__()` and `__next__()`.
- **Generator**: A special type of iterator that **uses `yield`** instead of `return`.

Example:
```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```
Generators are **memory-efficient** because they generate values lazily.

---


## 11. What is the Global Interpreter Lock (GIL) in Python?
The **Global Interpreter Lock (GIL)** is a mechanism in CPython that allows only **one thread** to execute Python bytecode at a time.  
This means Python **threads cannot run in true parallel** on multi-core processors.  

🔹 **Why does Python have GIL?**  
- Ensures **memory safety** for Python’s dynamic memory management.
- Prevents race conditions.

🔹 **How to overcome GIL limitations?**  
- Use **multiprocessing** (instead of threading) for parallel execution.
- Perform I/O-bound tasks (networking, file operations) using **asyncio**.

Example:
```python
import threading

def task():
    print("Task running")

t1 = threading.Thread(target=task)
t1.start()
```
🔹 **For CPU-bound tasks** ➝ Use `multiprocessing`  
🔹 **For I/O-bound tasks** ➝ Use `threading` or `asyncio`

---

## 12. Explain the difference between `deepcopy` and `copy`
- `copy.copy()` → **Shallow copy** (copies references, not the objects).
- `copy.deepcopy()` → **Deep copy** (creates new independent objects).

Example:
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]  (Deep copy remains unchanged)
```

---

## 13. How does Python handle exceptions? Provide an example.
Python uses `try-except-finally` to handle exceptions.

Example:
```python
try:
    x = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")
```

---

## 14. What is a lambda function? How is it different from a normal function?
A **lambda function** is an **anonymous function** (i.e., a function without a name).

🔹 **Syntax**:
```python
lambda arguments: expression
```

Example:
```python
# Lambda function
square = lambda x: x * x
print(square(5))  # Output: 25

# Equivalent normal function
def square_func(x):
    return x * x
```
🔹 **Differences from normal functions:**
| Feature  | Lambda Function | Normal Function |
|----------|---------------|---------------|
| Name     | Anonymous      | Named function |
| Usage    | Small, inline  | Larger code blocks |
| Returns  | Implicit       | Uses `return` |

---

## 15. Explain the difference between `map()`, `filter()`, and `reduce()`
- `map(function, iterable)`: Applies a function to each element.
- `filter(function, iterable)`: Filters elements based on a condition.
- `reduce(function, iterable)`: Reduces iterable to a single value.

Example:
```python
from functools import reduce

nums = [1, 2, 3, 4]

# map: square each element
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]

# filter: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# reduce: sum of elements
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)  # 10
```

---

## 16. What are metaclasses in Python?
A **metaclass** is a class **that defines the behavior of other classes**.  
In Python, **classes themselves are instances of a metaclass** (default: `type`).

Example:
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass  # This triggers the metaclass

# Output: "Creating class: MyClass"
```
Metaclasses allow **custom class creation and modification**.

---

## 17. What is monkey patching? Provide an example.
**Monkey patching** is dynamically modifying a **module or class at runtime**.

Example:
```python
class Dog:
    def speak(self):
        return "Bark!"

def new_speak():
    return "Meow!"  # Change behavior dynamically

Dog.speak = new_speak  # Monkey patching
print(Dog().speak())  # Output: "Meow!"
```
🔹 **Use Cases:**  
- Debugging  
- Fixing bugs at runtime  
- Testing  
⚠️ **Warning:** Monkey patching can make debugging harder.

---

## 18. How do you handle memory leaks in Python?
Python has **automatic garbage collection**, but memory leaks can still occur due to:
- **Unreleased references** (`global` variables, circular references).
- **Unused objects remaining in memory**.

🔹 **Solutions:**
- Use **weak references** (`weakref` module) to avoid strong references.
- Manually clean objects with `del`.
- Use `gc.collect()` to force garbage collection.

Example:
```python
import gc
gc.collect()  # Forces garbage collection
```

---

## 19. What is the difference between `@property` and `property()`?
- `@property` is a **decorator** used to define getters and setters.
- `property()` is a **built-in function** for the same purpose.

Example:
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property  # Getter
    def name(self):
        return self._name

    @name.setter  # Setter
    def name(self, value):
        self._name = value

p = Person("John")
print(p.name)  # Calls the getter
p.name = "Alice"  # Calls the setter
```
🔹 **Advantages:**  
- Encapsulates **attribute access**.
- Adds **validation** before setting values.

---

## 20. How does Python implement multithreading, and what are its limitations?
Python **supports multithreading**, but the **GIL (Global Interpreter Lock)** limits true parallel execution.

🔹 **When to use threading?**  
- **I/O-bound tasks** (file operations, API calls, web scraping).
- **Networking applications**.

🔹 **Example using threading:**
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

t = threading.Thread(target=print_numbers)
t.start()
```
🔹 **Limitations:**
- **Threads do not run in true parallel** (due to GIL).
- Use **multiprocessing** for **CPU-bound** tasks.

---


## 21. What is the difference between `is` and `==` in Python?
- `is` → Checks **object identity** (i.e., whether two variables point to the same memory location).
- `==` → Checks **value equality** (i.e., whether two objects have the same value).

Example:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True (values are the same)
print(a is c)  # False (different memory locations)
print(a is b)  # True (same object)
```
🔹 **Use `is` for checking if two variables reference the same object.**  
🔹 **Use `==` for comparing values.**

---

## 22. What are Python’s built-in data types?
Python provides several built-in data types:

| Data Type  | Example  |
|------------|---------|
| **Numeric** (int, float, complex) | `10`, `3.14`, `2+3j` |
| **Boolean** | `True`, `False` |
| **Sequence** (str, list, tuple, range) | `"hello"`, `[1,2,3]`, `(4,5,6)`, `range(5)` |
| **Set** (set, frozenset) | `{1,2,3}`, `frozenset({1,2,3})` |
| **Mapping** (dict) | `{"key": "value"}` |
| **NoneType** | `None` |

---

## 23. How do you remove duplicates from a list?
You can remove duplicates using **set**, **list comprehension**, or **collections.OrderedDict** (to preserve order).

Example:
```python
nums = [1, 2, 2, 3, 4, 4, 5]

# Method 1: Using set (Does not preserve order)
unique_nums = list(set(nums))
print(unique_nums)  # Output: [1, 2, 3, 4, 5]

# Method 2: Using list comprehension (Preserves order)
unique_nums = []
[unique_nums.append(n) for n in nums if n not in unique_nums]
print(unique_nums)  # Output: [1, 2, 3, 4, 5]

# Method 3: Using OrderedDict (Python 3.7+)
from collections import OrderedDict
unique_nums = list(OrderedDict.fromkeys(nums))
print(unique_nums)  # Output: [1, 2, 3, 4, 5]
```

---

## 24. What is the difference between `deepcopy()` and `copy()`?
- `copy.copy()` → Creates a **shallow copy** (copies references).
- `copy.deepcopy()` → Creates a **deep copy** (copies actual objects, not references).

Example:
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]  (Deep copy remains unchanged)
```

---

## 25. What is the difference between `append()` and `extend()`?
- `append()` → Adds **a single element** to the list.
- `extend()` → Adds **multiple elements** (iterable) to the list.

Example:
```python
nums = [1, 2, 3]

nums.append([4, 5])  # Adds a list as a single element
print(nums)  # Output: [1, 2, 3, [4, 5]]

nums.extend([6, 7])  # Adds elements individually
print(nums)  # Output: [1, 2, 3, [4, 5], 6, 7]
```

---

## 26. How can you reverse a string in Python?
You can reverse a string using **slicing**, **reversed()**, or **join()**.

Example:
```python
s = "hello"

# Method 1: Using slicing
print(s[::-1])  # Output: "olleh"

# Method 2: Using reversed()
print("".join(reversed(s)))  # Output: "olleh"

# Method 3: Using a loop
reversed_str = ""
for char in s:
    reversed_str = char + reversed_str
print(reversed_str)  # Output: "olleh"
```

---

## 27. How do you check if a string is a palindrome?
A **palindrome** is a word or phrase that reads the same backward.

Example:
```python
def is_palindrome(s):
    return s == s[::-1]  # Reverse and compare

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

---

## 28. What is the difference between `staticmethod` and `classmethod`?
- `@staticmethod` → Method **does not** use `self` or `cls`. Works like a normal function inside a class.
- `@classmethod` → Method **takes `cls` as a parameter** and modifies class-level attributes.

Example:
```python
class MyClass:
    class_var = "Hello"

    @staticmethod
    def static_method():
        return "I am a static method"

    @classmethod
    def class_method(cls):
        return f"Class method: {cls.class_var}"

print(MyClass.static_method())  # Output: "I am a static method"
print(MyClass.class_method())   # Output: "Class method: Hello"
```

---

## 29. How does Python manage memory?
Python uses **automatic memory management** with:
1. **Reference Counting**: Each object has a reference count.
2. **Garbage Collection (GC)**: Removes unused objects with cyclic references.
3. **Memory Pools (PyMalloc)**: Manages memory efficiently.

Example:
```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # Shows reference count

del x  # Deletes the reference, allowing GC to clean up
```
🔹 **Use `gc.collect()`** to manually trigger garbage collection.

---

## 30. How do you create and handle custom exceptions in Python?
You can create custom exceptions by **inheriting from `Exception`**.

Example:
```python
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print(f"Caught custom exception: {e}")
```
---

