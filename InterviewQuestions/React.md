

# React.js Interview Questions & Answers  

This document provides answers to some of the most frequently asked React.js interview questions.  

## 1. What are the key features of React.js?  
React.js is a JavaScript library for building UI components. Key features include:  
- **JSX** – A syntax extension that allows writing HTML in JavaScript.  
- **Virtual DOM** – Optimizes updates and improves performance.  
- **Component-Based Architecture** – UI is split into reusable components.  
- **Unidirectional Data Flow** – Helps maintain predictable state changes.  
- **React Hooks** – Allows functional components to use state and lifecycle methods.  

## 2. What is JSX, and how is it different from HTML?  
JSX (JavaScript XML) is a syntax extension used in React that looks similar to HTML but has some differences:  
- JSX allows embedding JavaScript expressions inside `{}`.  
- JSX must return a **single parent element** (use fragments `<></>` if needed).  
- JSX uses **camelCase** for attributes (e.g., `className` instead of `class`).  

Example:  
```jsx
const element = <h1>Hello, {user.name}!</h1>;
```

## 3. What is the Virtual DOM, and how does it improve performance?  
The **Virtual DOM (VDOM)** is a lightweight copy of the real DOM. React updates this VDOM first, then compares it with the previous version (**diffing**), and applies only the necessary changes to the real DOM (**reconciliation**).  
This improves performance by reducing direct DOM manipulations, which are costly in terms of performance.  

## 4. What are props in React? How are they used?  
**Props (short for properties)** are used to pass data from parent to child components. Props are **read-only** and cannot be modified by the child component.  

Example:  
```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}
<Welcome name="Sathish" />;
```

## 5. What is state in React? How does it differ from props?  
**State** is a built-in object in React that stores dynamic data and affects a component’s behavior. Unlike props, state is **mutable** and is managed within the component.  

Example:  
```jsx
import { useState } from "react";
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
```
**Difference between Props and State:**  
| Props | State |
|-------|------|
| Passed from parent to child | Managed within the component |
| Immutable (read-only) | Mutable (can change over time) |
| Can be used in functional & class components | Requires `useState` in functional components |

## 6. What is `useEffect`, and how does it work?  
The `useEffect` hook is used to handle **side effects** (API calls, subscriptions, DOM updates) in functional components. It runs after every render unless dependencies are specified.  

Example:  
```jsx
import { useEffect, useState } from "react";
function Timer() {
  const [time, setTime] = useState(0);
  
  useEffect(() => {
    const interval = setInterval(() => setTime(time + 1), 1000);
    return () => clearInterval(interval); // Cleanup function
  }, [time]);

  return <p>Time: {time}</p>;
}
```

## 7. What is the significance of the `key` attribute in lists?  
The `key` attribute helps React identify and update elements efficiently when rendering lists. It should be **unique, stable, and consistent** (e.g., using a unique ID instead of `index`).  

Example:  
```jsx
const items = ["Apple", "Banana", "Cherry"];
items.map((item, index) => <li key={index}>{item}</li>); // Bad practice  
items.map((item) => <li key={item.id}>{item.name}</li>); // Best practice  
```

## 8. What is the difference between `useState` and `useReducer`?  
Both `useState` and `useReducer` manage state, but `useReducer` is better for complex state logic involving multiple values.  

| `useState` | `useReducer` |
|------------|-------------|
| Simple state updates | Handles complex state logic |
| Uses `setState` to update | Uses `dispatch` with an action object |
| Good for local state | Suitable for state that depends on previous state |

Example of `useReducer`:  
```jsx
import { useReducer } from "react";

const reducer = (state, action) => {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    default:
      return state;
  }
};

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
    </>
  );
}
```

## 9. What is lazy loading in React, and how does `React.lazy` work?  
Lazy loading is a technique that loads components **only when needed**, reducing the initial load time. `React.lazy()` allows dynamic imports.  

Example:  
```jsx
import { Suspense, lazy } from "react";

const LazyComponent = lazy(() => import("./LazyComponent"));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

## 10. How do you optimize React app performance?  
Some common ways to improve React app performance:  
- **Use React.memo** to prevent unnecessary re-renders.  
- **Use useCallback and useMemo** to optimize function and value references.  
- **Lazy load components** using `React.lazy`.  
- **Use virtualization** with libraries like `react-window` for large lists.  
- **Avoid unnecessary state updates** to prevent extra renders.  

---

This guide provides essential React interview questions and answers to help you prepare effectively. 🚀  
```

---


Here’s the **next 10 React.js interview questions with answers** in **GitHub README.md** format:  

---

```md
# React.js Interview Questions & Answers (Part 2)

This document contains another set of important React.js interview questions with clear explanations.

## 11. What are Higher-Order Components (HOC) in React?
A **Higher-Order Component (HOC)** is a function that takes a component as input and returns a new enhanced component. HOCs are used for **code reusability, logic abstraction, and prop manipulation**.

Example:
```jsx
function withLogger(WrappedComponent) {
  return function EnhancedComponent(props) {
    console.log("Component rendered!");
    return <WrappedComponent {...props} />;
  };
}

const HelloWorld = () => <h1>Hello, World!</h1>;
const EnhancedHelloWorld = withLogger(HelloWorld);
```
HOCs are commonly used for authentication, logging, and performance optimization.

---

## 12. What is the difference between controlled and uncontrolled components?
| Controlled Component | Uncontrolled Component |
|----------------------|----------------------|
| State is managed by React (`useState`) | State is managed by the DOM (`ref`) |
| Values are updated via `setState` | Uses `ref` to access values |
| Easier to control & test | Suitable for simple uncontrolled inputs |

Example of a **Controlled Component**:
```jsx
function ControlledInput() {
  const [value, setValue] = useState("");

  return (
    <input type="text" value={value} onChange={(e) => setValue(e.target.value)} />
  );
}
```
Example of an **Uncontrolled Component**:
```jsx
function UncontrolledInput() {
  const inputRef = useRef();

  const handleSubmit = () => {
    alert(inputRef.current.value);
  };

  return <input type="text" ref={inputRef} />;
}
```

---

## 13. What is `useRef`, and where is it used?
`useRef` creates a **mutable reference** that persists across renders without causing re-renders.

### Use cases:
- **Accessing DOM elements** (e.g., focusing an input)
- **Storing previous values** (like a cache)
- **Keeping values between renders without re-rendering**

Example:
```jsx
function FocusInput() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return <input ref={inputRef} type="text" />;
}
```

---

## 14. What is `useMemo`, and when should you use it?
`useMemo` **memoizes** computed values to prevent expensive recalculations.

Example:
```jsx
const expensiveCalculation = useMemo(() => {
  return slowFunction(value);
}, [value]);
```
Use `useMemo` when:
- You have **expensive calculations** inside a component.
- You want to **avoid unnecessary recalculations**.

---

## 15. What is the difference between `useEffect` and `useLayoutEffect`?
| `useEffect` | `useLayoutEffect` |
|------------|------------------|
| Runs **after** the browser paints the screen | Runs **before** the browser paints the screen |
| Non-blocking | Blocking (can delay rendering) |
| Suitable for API calls, timers | Used for DOM measurements, animations |

Example:
```jsx
useLayoutEffect(() => {
  console.log("Executed before paint");
});
useEffect(() => {
  console.log("Executed after paint");
});
```

---

## 16. What is Context API, and how does it work?
The **Context API** provides a way to pass data **without prop drilling**.

### Steps:
1. **Create a Context**
2. **Provide the context value**
3. **Consume the context value using `useContext`**

Example:
```jsx
const ThemeContext = createContext();

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ChildComponent />
    </ThemeContext.Provider>
  );
}

function ChildComponent() {
  const theme = useContext(ThemeContext);
  return <p>Theme: {theme}</p>;
}
```

---

## 17. What is React Fiber, and how does it improve performance?
**React Fiber** is a re-implementation of the React core algorithm, making rendering more efficient.

### Benefits:
- **Asynchronous rendering** (splitting updates into chunks)
- **Better UI responsiveness**
- **Prioritization of updates** (e.g., animations vs. data fetching)

---

## 18. What is `React.PureComponent`?
`PureComponent` is a class component that implements **shouldComponentUpdate()** automatically.

### Difference between `Component` and `PureComponent`
| `Component` | `PureComponent` |
|------------|----------------|
| Rerenders on any state/prop change | Rerenders only if state/props change |
| Requires `shouldComponentUpdate` manually | Automatic shallow comparison |

Example:
```jsx
class MyComponent extends React.PureComponent {
  render() {
    return <h1>{this.props.value}</h1>;
  }
}
```
For functional components, use `React.memo()` instead.

---

## 19. How does error handling work in React?
React handles errors using **Error Boundaries**.

### Features:
- Catches errors in child components
- Prevents UI crashes
- Logs errors gracefully

Example:
```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.error("Error:", error, info);
  }

  render() {
    return this.state.hasError ? <h1>Something went wrong.</h1> : this.props.children;
  }
}
```
Usage:
```jsx
<ErrorBoundary>
  <MyComponent />
</ErrorBoundary>
```

---

## 20. What are React Portals?
**React Portals** allow rendering a component outside its normal hierarchy in the DOM.

### Use case:
- Rendering **modals, tooltips, dropdowns** outside the parent container.

Example:
```jsx
const modalRoot = document.getElementById("modal-root");

function Modal({ children }) {
  return ReactDOM.createPortal(children, modalRoot);
}
```
Usage:
```jsx
<Modal>
  <div className="modal">This is a modal!</div>
</Modal>
```

---

```md
# React.js Interview Questions & Answers (Part 3)

This document contains the final set of important React.js interview questions with clear explanations.

---

## 21. What is the difference between `React.memo` and `useMemo`?
Both `React.memo` and `useMemo` help with performance optimization, but they serve different purposes.

| Feature | `React.memo` | `useMemo` |
|---------|------------|----------|
| Type | Higher-order component (HOC) | Hook |
| Purpose | Memoizes a **component** | Memoizes a **computed value** |
| Usage | Prevents unnecessary re-renders | Prevents unnecessary recalculations |

Example of `React.memo`:
```jsx
const MyComponent = React.memo(({ value }) => {
  console.log("Rendered!");
  return <p>{value}</p>;
});
```
Example of `useMemo`:
```jsx
const expensiveCalculation = useMemo(() => compute(value), [value]);
```

---

## 22. What is `useCallback`, and when should you use it?
`useCallback` **memoizes** a function so that it does not get re-created on every render.

### When to use:
- When passing functions as **props** to child components
- To optimize performance in large applications

Example:
```jsx
const memoizedFunction = useCallback(() => {
  console.log("This function is memoized");
}, []);
```

---

## 23. What is lazy loading in React?
Lazy loading **defers component loading** until it is needed, improving performance.

React provides `React.lazy()` and `Suspense` for lazy loading.

Example:
```jsx
const LazyComponent = React.lazy(() => import("./LazyComponent"));

function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <LazyComponent />
    </Suspense>
  );
}
```
🔹 Useful for **code splitting** to reduce initial load time.

---

## 24. What is reconciliation in React?
Reconciliation is the **process of updating the UI efficiently** using the Virtual DOM.

### How it works:
1. React creates a **new Virtual DOM tree**.
2. Compares it with the **previous Virtual DOM**.
3. Updates only the **changed elements** in the real DOM.

🚀 This **minimizes performance costs** and speeds up rendering.

---

## 25. What are React Fragments, and why use them?
React Fragments (`<></>`) allow grouping elements **without adding extra DOM nodes**.

Example:
```jsx
function MyComponent() {
  return (
    <>
      <h1>Hello</h1>
      <p>This is a React Fragment.</p>
    </>
  );
}
```
🔹 **Benefits:** Improves performance and avoids unnecessary HTML wrappers.

---

## 26. How do you optimize performance in React applications?
### Strategies:
1. **Use `React.memo()`** to avoid unnecessary re-renders.
2. **Use `useCallback` and `useMemo`** for function and value memoization.
3. **Lazy load components** using `React.lazy()`.
4. **Use the Context API efficiently** to avoid excessive re-renders.
5. **Optimize large lists** with `React.Virtualized`.

---

## 27. What is server-side rendering (SSR) in React?
Server-side rendering (SSR) **renders React components on the server** before sending them to the client.

🔹 **Benefits:**
- **Improves SEO**
- **Faster initial load**
- **Better performance for slow devices**

Example with **Next.js** (a React framework for SSR):
```jsx
export async function getServerSideProps() {
  return { props: { data: "Hello from server!" } };
}

export default function Home({ data }) {
  return <h1>{data}</h1>;
}
```

---

## 28. What is hydration in React?
Hydration is the process where React **attaches event listeners** to **server-rendered** content.

🔹 Happens when **Server-Side Rendering (SSR)** is used.

Example:
```jsx
ReactDOM.hydrate(<App />, document.getElementById("root"));
```
🚀 **Optimizes SSR performance** by keeping the UI interactive.

---

## 29. What are synthetic events in React?
Synthetic events **wrap native events** to ensure cross-browser compatibility.

Example:
```jsx
function Button() {
  return <button onClick={(event) => console.log(event)}>Click Me</button>;
}
```
🔹 **Benefits:** Provides a unified API for handling DOM events.

---

## 30. What is Concurrent Mode in React?
Concurrent Mode makes React **more responsive by rendering updates in chunks**.

🔹 **Key Features:**
- **Automatic batching** (reduces re-renders)
- **Prioritization of tasks** (user interactions first)
- **Suspense for Data Fetching** (preloading UI)

🚀 Helps improve the performance of complex applications.

---

### 🎯 Conclusion:
This document provides a total of **30 React.js interview questions** covering:
✅ React basics  
✅ Hooks (`useState`, `useEffect`, `useMemo`, etc.)  
✅ Advanced concepts (SSR, Hydration, Concurrent Mode)  
✅ Performance optimization  

Hope this helps you in your **React.js interviews! 🚀🔥**  
```

---

### 📌 **Key Features in this GitHub README Format**
✔ **Headings (`##`)** for readability  
✔ **Code blocks (` ```jsx `)** for clear examples  
✔ **Tables (`|`)** for comparisons  
✔ **Emoji highlights** to emphasize key points  

Would you like more **DSA-related questions** in a similar format? 😊🚀
