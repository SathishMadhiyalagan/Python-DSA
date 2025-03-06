
### **1. What are the different data types in JavaScript?**  
JavaScript has **8 primitive data types** and **1 non-primitive** type:  
- **Primitive Types**:  
  1. `String` → `"Hello"`  
  2. `Number` → `42`, `3.14`  
  3. `BigInt` → `1234567890123456789n`  
  4. `Boolean` → `true`, `false`  
  5. `Undefined` → `let x;` (not assigned)  
  6. `Null` → `let y = null;` (empty value)  
  7. `Symbol` → `Symbol("id")` (unique identifier)  
- **Non-Primitive Type**:  
  - `Object` → `{ name: "Sathish", age: 30 }`  

---

### **2. What is the difference between `let`, `const`, and `var`?**  
| Feature  | `var` | `let` | `const` |
|----------|------|------|------|
| Scope | Function-scoped | Block-scoped | Block-scoped |
| Re-declaration | Allowed | Not Allowed | Not Allowed |
| Re-assignment | Allowed | Allowed | Not Allowed |
| Hoisting | Hoisted (with `undefined`) | Hoisted (but not initialized) | Hoisted (but not initialized) |

Example:  
```js
var x = 10;    // Function-scoped
let y = 20;    // Block-scoped
const z = 30;  // Cannot be changed
```

---

### **3. What is the difference between `==` and `===` in JavaScript?**  
- `==` (loose equality) → Checks only **values** (performs type coercion).  
- `===` (strict equality) → Checks **both value and type** (no type coercion).  

Example:  
```js
console.log(5 == "5");   // true  (type conversion happens)
console.log(5 === "5");  // false (different types)
```

---

### **4. What are truthy and falsy values in JavaScript?**  
- **Truthy values**: Any value that evaluates to `true` in a Boolean context (e.g., `"hello"`, `1`, `[]`, `{}`).
- **Falsy values**: Values that evaluate to `false` (e.g., `0`, `""`, `null`, `undefined`, `NaN`, `false`).

Example:  
```js
if ("hello") console.log("Truthy"); // ✅ Executes
if (0) console.log("Falsy");       // ❌ Doesn't execute
```

---

### **5. What is hoisting in JavaScript?**  
Hoisting moves **variable and function declarations** to the top of their scope before code execution.  

Example:  
```js
console.log(a); // undefined (hoisted)
var a = 10; 

hello(); // ✅ Works due to hoisting
function hello() { console.log("Hello World"); }
```

---

### **6. What is a closure in JavaScript?**  
A **closure** is a function that remembers variables from its parent scope, even after the parent function has executed.

Example:  
```js
function outer() {
  let count = 0;
  return function inner() {
    count++;
    console.log(count);
  };
}

const counter = outer();
counter(); // 1
counter(); // 2
```

---

### **7. What is the difference between function declaration and function expression?**  
| Feature  | Function Declaration | Function Expression |
|----------|---------------------|----------------------|
| Hoisting | Yes | No |
| Syntax | `function greet() {}` | `const greet = function() {};` |
| Naming | Named | Can be anonymous |

Example:  
```js
// Function Declaration (hoisted)
function sayHello() { console.log("Hello"); }

// Function Expression (not hoisted)
const sayHi = function() { console.log("Hi"); };
```

---

### **8. What are arrow functions, and how are they different from regular functions?**  
Arrow functions are a shorter way to write functions **without `function` keyword**.  
**Differences:**  
✅ No `this` binding  
✅ More concise syntax  
✅ Cannot be used as constructors  

Example:  
```js
const add = (a, b) => a + b; // Arrow function
console.log(add(2, 3)); // 5
```

---

### **9. What is the difference between `null` and `undefined`?**  
| Feature | `null` | `undefined` |
|---------|-------|------------|
| Meaning | Empty or intentional absence of value | Variable declared but not assigned |
| Type | `object` | `undefined` |
| Example | `let x = null;` | `let y;` |

Example:  
```js
let a = null; // Empty value
let b;        // Undefined value
console.log(typeof a); // "object"
console.log(typeof b); // "undefined"
```

---

### **10. What is the difference between pass-by-value and pass-by-reference in JavaScript?**  
| Type | Passed By Value | Passed By Reference |
|------|---------------|----------------|
| Data Type | Primitives (`Number`, `String`, `Boolean`) | Objects (`Array`, `Function`, `Object`) |
| Changes Affect Original? | No | Yes |

Example:  
```js
let x = 10;
let y = x; // Pass-by-value (copy)
y = 20;
console.log(x); // 10

let obj1 = { a: 10 };
let obj2 = obj1; // Pass-by-reference (same memory)
obj2.a = 20;
console.log(obj1.a); // 20
```

---

### **11. What is an Immediately Invoked Function Expression (IIFE)?**  
An **IIFE** is a function that runs immediately after it is defined.  

✅ Used to create a private scope and avoid polluting the global namespace.  

Example:  
```js
(function () {
  console.log("IIFE executed!");
})();  
// Output: "IIFE executed!"
```

---

### **12. What is the difference between synchronous and asynchronous JavaScript?**  
| Feature | Synchronous | Asynchronous |
|---------|------------|--------------|
| Execution | Code runs line by line | Code runs in the background |
| Blocking | Blocks execution until task is done | Doesn't block execution |
| Example | `console.log("Hello")` | `setTimeout(() => console.log("Hello"), 1000)` |

Example:  
```js
console.log("Start");
setTimeout(() => console.log("Async Task"), 1000);
console.log("End");
// Output: "Start" → "End" → "Async Task"
```

---

### **13. What are Promises in JavaScript?**  
A **Promise** represents a future value that is either resolved or rejected.  

States of a Promise:  
1. **Pending**  
2. **Resolved (fulfilled)**  
3. **Rejected**  

Example:  
```js
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Success!"), 2000);
});

myPromise.then(result => console.log(result)); // "Success!" (after 2 sec)
```

---

### **14. What is `async` and `await` in JavaScript?**  
`async` and `await` make handling Promises easier by making asynchronous code look synchronous.  

Example:  
```js
async function fetchData() {
  let response = await fetch("https://jsonplaceholder.typicode.com/todos/1");
  let data = await response.json();
  console.log(data);
}

fetchData();
```
✅ `await` pauses execution until the Promise resolves.  

---

### **15. What is event bubbling and event capturing in JavaScript?**  
- **Event Bubbling** → Inner element's event **bubbles up** to parent elements.  
- **Event Capturing** → Event is **captured from the outer** element and then reaches the inner element.  

Example:  
```js
document.getElementById("child").addEventListener("click", () => {
  console.log("Child clicked");
});

document.getElementById("parent").addEventListener("click", () => {
  console.log("Parent clicked");
});
```
If `child` is clicked:  
✅ **Bubbling Mode**: Logs `"Child clicked"` → `"Parent clicked"`  
✅ **Capturing Mode**: Logs `"Parent clicked"` → `"Child clicked"`  

---

### **16. What is the difference between localStorage, sessionStorage, and cookies?**  
| Feature | `localStorage` | `sessionStorage` | `cookies` |
|---------|--------------|---------------|----------|
| Expiry | Never (until manually cleared) | When the session ends | Can be set manually |
| Storage Limit | 5MB | 5MB | 4KB |
| Access | Only on client-side | Only on client-side | Sent with HTTP requests |

Example:  
```js
// localStorage
localStorage.setItem("key", "value");

// sessionStorage
sessionStorage.setItem("sessionKey", "value");

// Cookies
document.cookie = "user=Sathish; expires=Fri, 31 Dec 2025 23:59:59 UTC";
```

---

### **17. What is debouncing and throttling in JavaScript?**  
✅ **Debouncing** → Delays function execution until a pause in events.  
✅ **Throttling** → Limits function execution to a fixed interval.  

Example:  
```js
// Debounce Example
function debounce(func, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => func(...args), delay);
  };
}

// Throttle Example
function throttle(func, interval) {
  let lastTime = 0;
  return function (...args) {
    let now = Date.now();
    if (now - lastTime >= interval) {
      func(...args);
      lastTime = now;
    }
  };
}
```

---

### **18. What is the `this` keyword in JavaScript?**  
The `this` keyword refers to the **context** in which a function is called.  

✅ `this` in a function → Depends on how it's called  
✅ `this` in an arrow function → Uses lexical scope  

Example:  
```js
console.log(this); // Window object in browser

function show() {
  console.log(this); // Global object (Window in browser)
}

const obj = {
  name: "Sathish",
  show() {
    console.log(this.name); // "Sathish"
  }
};

obj.show();
```

---

### **19. What are template literals in JavaScript?**  
✅ **Template literals** allow embedding expressions inside strings using backticks `` ` ``.  

Example:  
```js
const name = "Sathish";
const age = 30;
console.log(`My name is ${name} and I am ${age} years old.`);
```
🔹 Without template literals:  
```js
console.log("My name is " + name + " and I am " + age + " years old.");
```

---

### **20. What is destructuring in JavaScript?**  
✅ **Destructuring** allows extracting values from arrays or objects easily.  

🔹 **Array Destructuring**:  
```js
const [first, second] = [10, 20];
console.log(first); // 10
console.log(second); // 20
```

🔹 **Object Destructuring**:  
```js
const user = { name: "Sathish", age: 30 };
const { name, age } = user;
console.log(name); // "Sathish"
console.log(age); // 30
```

---

### **21. What is the difference between `==` and `===` in JavaScript?**  
✅ **`==` (Loose Equality)** → Checks only values, allowing type coercion.  
✅ **`===` (Strict Equality)** → Checks both values and types.  

Example:  
```js
console.log(5 == "5");  // true  (type coercion)
console.log(5 === "5"); // false (strict comparison)
```

---

### **22. What is a closure in JavaScript?**  
A **closure** is a function that remembers the variables from its outer scope even after the outer function has finished executing.

Example:  
```js
function outer() {
  let count = 0;
  return function inner() {
    count++;
    console.log(count);
  };
}

const counter = outer();
counter(); // 1
counter(); // 2
```
✅ The `inner` function retains access to `count`, forming a **closure**.

---

### **23. What is the difference between `map()`, `forEach()`, `filter()`, and `reduce()`?**  

| Method  | Purpose | Returns |
|---------|---------|---------|
| `map()`  | Transforms each array element | **New array** |
| `forEach()`  | Iterates over elements | **Nothing (undefined)** |
| `filter()`  | Filters elements based on condition | **New array** |
| `reduce()`  | Reduces elements to a single value | **Single value** |

Example:  
```js
const numbers = [1, 2, 3, 4];

const squared = numbers.map(num => num * num);
console.log(squared); // [1, 4, 9, 16]

numbers.forEach(num => console.log(num * 2)); // Logs: 2, 4, 6, 8

const evens = numbers.filter(num => num % 2 === 0);
console.log(evens); // [2, 4]

const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // 10
```

---

### **24. What is the difference between function declaration and function expression?**  
✅ **Function Declaration** → Hoisted (can be called before definition).  
✅ **Function Expression** → Not hoisted.  

Example:  
```js
// Function Declaration
function greet() {
  console.log("Hello!");
}

// Function Expression
const greet = function () {
  console.log("Hello!");
};
```
🚀 **Best Practice:** Use function expressions for consistency.

---

### **25. What is the difference between `var`, `let`, and `const`?**  

| Feature  | `var` | `let` | `const` |
|----------|------|------|------|
| Scope | Function-scoped | Block-scoped | Block-scoped |
| Hoisting | Hoisted (undefined) | Hoisted (not initialized) | Hoisted (not initialized) |
| Reassignment | Allowed | Allowed | ❌ Not Allowed |

Example:  
```js
var x = 10;  // Function-scoped
let y = 20;  // Block-scoped
const z = 30; // Cannot be reassigned
```

---

### **26. What is the spread operator (`...`) in JavaScript?**  
✅ The **spread operator** expands an array or object into individual elements.

Example:  
```js
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2); // [1, 2, 3, 4, 5]

const obj1 = { name: "Sathish" };
const obj2 = { ...obj1, age: 30 };
console.log(obj2); // { name: "Sathish", age: 30 }
```

---

### **27. What is the rest operator (`...`) in JavaScript?**  
✅ The **rest operator** gathers multiple arguments into a single array.

Example:  
```js
function sum(...numbers) {
  return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4)); // 10
```

---

### **28. What is `call()`, `apply()`, and `bind()` in JavaScript?**  
✅ Used to change the value of `this` in a function.

| Method  | Purpose |
|---------|---------|
| `call()`  | Calls a function with a given `this` and arguments |
| `apply()` | Similar to `call()` but arguments are passed as an array |
| `bind()`  | Returns a new function with `this` bound |

Example:  
```js
const person = { name: "Sathish" };

function greet(message) {
  console.log(`${message}, ${this.name}`);
}

greet.call(person, "Hello");   // "Hello, Sathish"
greet.apply(person, ["Hi"]);   // "Hi, Sathish"
const boundGreet = greet.bind(person);
boundGreet("Hey");  // "Hey, Sathish"
```

---

### **29. What is `typeof` and `instanceof` in JavaScript?**  
✅ **`typeof`** checks the data type of a value.  
✅ **`instanceof`** checks if an object is an instance of a constructor.

Example:  
```js
console.log(typeof "Hello"); // "string"
console.log(typeof 42);      // "number"

class Animal {}
const dog = new Animal();
console.log(dog instanceof Animal); // true
```

---

### **30. How do you deep clone an object in JavaScript?**  
✅ Use `JSON.parse(JSON.stringify(obj))` or `structuredClone()`.  

Example:  
```js
const obj1 = { a: 1, b: { c: 2 } };
const obj2 = JSON.parse(JSON.stringify(obj1));

obj2.b.c = 99;
console.log(obj1.b.c); // 2 (original object remains unchanged)
```

🚀 **Best Practice:** Use `structuredClone()` for better performance.  
```js
const objClone = structuredClone(obj1);
```

---

