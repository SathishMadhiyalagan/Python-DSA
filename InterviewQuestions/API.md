### **Top 15 API Interview Questions with Answers**  

#### **1. What is a REST API, and how does it work?**  
A REST (Representational State Transfer) API is a web service that allows communication between client and server using HTTP methods like GET, POST, PUT, and DELETE. It follows REST principles, such as statelessness, resource-based architecture, and a uniform interface. The API endpoints return data in formats like JSON or XML.  

---

#### **2. What are the differences between REST and SOAP APIs?**  
| Feature | REST API | SOAP API |
|---------|---------|---------|
| Protocol | Uses HTTP | Uses HTTP, SMTP, and more |
| Data Format | JSON, XML, etc. | Only XML |
| Performance | Faster and lightweight | Slower due to XML overhead |
| Security | Uses OAuth, JWT | Uses WS-Security |
| Usage | Web and mobile applications | Enterprise applications requiring high security |

---

#### **3. What is the difference between `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` methods?**  
- **GET**: Retrieves data from the server. Example: Fetching user details.  
- **POST**: Sends new data to the server. Example: Creating a new user.  
- **PUT**: Updates an entire resource. Example: Replacing user details.  
- **PATCH**: Updates part of a resource. Example: Changing a user’s email.  
- **DELETE**: Removes a resource. Example: Deleting a user.  

---

#### **4. What are status codes in APIs? Provide examples.**  
HTTP status codes indicate the response of an API request:  
- **200 OK** – Successful request  
- **201 Created** – Resource created successfully  
- **400 Bad Request** – Invalid request from client  
- **401 Unauthorized** – Authentication required  
- **403 Forbidden** – Access denied  
- **404 Not Found** – Resource not found  
- **500 Internal Server Error** – Server encountered an issue  

---

#### **5. What is the purpose of API authentication? Explain different authentication methods.**  
API authentication ensures only authorized users access the API. Common methods include:  
- **API Key** – A unique key sent in the request header.  
- **OAuth 2.0** – Token-based authentication for secure access.  
- **JWT (JSON Web Token)** – Self-contained tokens for authentication.  
- **Basic Authentication** – Uses a username and password in the request header.  

---

#### **6. What is the difference between `Bearer Token` and `API Key` authentication?**  
- **API Key**: A static key passed in the request header to identify the client.  
- **Bearer Token**: A temporary access token, usually issued via OAuth, passed in the `Authorization` header for secure authentication.  

---

#### **7. What is CORS, and how does it affect API requests?**  
CORS (Cross-Origin Resource Sharing) is a security feature in web browsers that restricts API calls from different domains. If an API does not allow cross-origin requests, the browser blocks them. It can be resolved by enabling CORS in the server's response headers (`Access-Control-Allow-Origin`).  

---

#### **8. What is JSON Web Token (JWT), and how does it work?**  
JWT is a compact, self-contained token used for secure API authentication. It consists of three parts:  
1. **Header** – Contains metadata about the token.  
2. **Payload** – Holds user information.  
3. **Signature** – A secret key used to verify authenticity.  

Example JWT:  
```eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2MzI4MzcwMDB9.V1lPpC5aN9S8dpIMF```  

---

#### **9. How can you handle API rate limiting?**  
API rate limiting prevents excessive requests from a single client to protect the server. Methods include:  
- Setting a request quota per user/IP.  
- Returning `429 Too Many Requests` status.  
- Using **API Gateway** to enforce limits.  
- Implementing exponential backoff (retrying after increasing wait times).  

---

#### **10. What is an API gateway, and why is it used?**  
An API Gateway is a server that manages API requests, acting as a single entry point. It helps with:  
- **Security** – Authentication and authorization.  
- **Rate Limiting** – Preventing excessive API calls.  
- **Load Balancing** – Distributing traffic among multiple servers.  
- **Logging & Monitoring** – Tracking API usage.  

Example: AWS API Gateway, Kong API Gateway.  

---

#### **11. How does pagination work in REST APIs?**  
Pagination is used to retrieve large amounts of data in smaller chunks. Common approaches:  
- **Limit & Offset**: `GET /users?limit=10&offset=20`  
- **Cursor-based pagination**: `GET /users?cursor=eyJpZCI6MTAw…`  
- **Page-based pagination**: `GET /users?page=2&size=10`  

---

#### **12. What are WebSockets, and how do they differ from REST APIs?**  
WebSockets enable real-time communication between client and server using a persistent connection, unlike REST, which follows a request-response model.  
- **REST** – Stateless, works well for fetching data.  
- **WebSockets** – Persistent, ideal for live updates (e.g., chat apps, stock prices).  

---

#### **13. What is GraphQL, and how is it different from REST APIs?**  
GraphQL is an alternative to REST APIs that allows clients to query exactly the data they need.  
| Feature | REST API | GraphQL |
|---------|---------|---------|
| Structure | Multiple endpoints | Single endpoint |
| Data Fetching | Fixed responses | Custom queries |
| Over-fetching | Possible | No over-fetching |
| Performance | Requires multiple requests | Fetches all in one request |

---

#### **14. How do you secure an API from attacks like CSRF, XSS, and SQL Injection?**  
- **CSRF (Cross-Site Request Forgery)** – Use CSRF tokens for request validation.  
- **XSS (Cross-Site Scripting)** – Sanitize user input and escape HTML in responses.  
- **SQL Injection** – Use parameterized queries and ORM frameworks to prevent malicious SQL queries.  

---

#### **15. What is API versioning, and why is it important?**  
API versioning allows different versions of an API to coexist, preventing breaking changes for users.  
Common methods:  
- **URL versioning**: `/api/v1/users`  
- **Header versioning**: `Accept: application/vnd.myapi.v1+json`  
- **Query parameter**: `/users?version=1`  

---

### **16. What is idempotency in APIs, and why is it important?**  
Idempotency means that making multiple identical requests results in the same outcome.  
- **GET** and **DELETE** requests are idempotent because calling them multiple times does not change the resource state.  
- **POST** is **not** idempotent as it creates a new resource with each request.  
- **PUT** is idempotent because updating a resource with the same data will not create duplicates.  

---

### **17. What are OpenAPI (Swagger) specifications?**  
OpenAPI (Swagger) is a standard for defining APIs, making them easy to document and test.  
- It provides a JSON/YAML-based structure to describe API endpoints, request/response formats, and authentication.  
- Example Swagger UI usage:  
  ```yaml
  openapi: 3.0.0
  info:
    title: My API
    version: 1.0.0
  paths:
    /users:
      get:
        summary: Get all users
        responses:
          '200':
            description: Successful response
  ```  

---

### **18. What are API Contracts?**  
An **API Contract** defines how an API behaves, including:  
- Request and response formats.  
- Allowed HTTP methods.  
- Status codes.  
- Authentication requirements.  

API contracts ensure consistency and help frontend and backend teams work efficiently.

---

### **19. What are webhooks, and how do they work?**  
Webhooks allow real-time notifications when specific events occur.  
- Instead of polling, the server sends data to a **callback URL** when an event happens.  
- Example: GitHub triggers a webhook when a repository is updated.  

Webhook example in Node.js:  
```js
app.post('/webhook', (req, res) => {
  console.log(req.body); // Process event
  res.status(200).send('Webhook received');
});
```

---

### **20. What is rate limiting, and how is it implemented?**  
Rate limiting prevents excessive API requests, improving performance and security.  
- Example techniques:  
  - **Token Bucket**: Users have a limited number of tokens.  
  - **Leaky Bucket**: Limits requests at a fixed rate.  
  - **Fixed Window**: Restricts requests per time window.  
- Implemented using API Gateways (e.g., AWS API Gateway, Nginx).  

---

### **21. How do you test APIs?**  
Common API testing tools:  
- **Postman**: Manual API testing and automation.  
- **cURL**: Command-line API requests.  
- **JMeter**: Performance testing.  
- **JUnit/PyTest**: Unit testing APIs.  

Example `cURL` request:  
```sh
curl -X GET "https://api.example.com/users" -H "Authorization: Bearer token"
```

---

### **22. How do you handle API errors gracefully?**  
Best practices for API error handling:  
- Use proper HTTP status codes (`400`, `401`, `500`).  
- Provide meaningful error messages.  
- Return structured JSON responses:  
  ```json
  {
    "error": "Invalid request",
    "message": "The 'email' field is required"
  }
  ```  
- Log errors for debugging.  

---

### **23. What is an API cache, and how does it improve performance?**  
API caching stores responses temporarily to reduce repeated database queries.  
Common caching strategies:  
- **Client-side caching** – Browsers store API responses.  
- **Server-side caching** – Responses are cached in Redis or Memcached.  
- **CDN caching** – APIs cache responses globally.  

Example: Enabling caching in Django  
```python
CACHE_MIDDLEWARE_SECONDS = 3600  # Cache API response for 1 hour
```

---

### **24. What is HATEOAS in REST APIs?**  
HATEOAS (Hypermedia as the Engine of Application State) allows clients to discover API actions dynamically via links.  
- Example response:  
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "links": [
      {"rel": "self", "href": "/users/1"},
      {"rel": "edit", "href": "/users/1/edit"},
      {"rel": "delete", "href": "/users/1/delete"}
    ]
  }
  ```  
- Helps clients navigate APIs without prior knowledge of endpoints.  

---

### **25. What is API load balancing?**  
Load balancing distributes API traffic across multiple servers for:  
- **High availability** – Prevents downtime.  
- **Scalability** – Handles increased traffic.  
- **Performance improvement** – Reduces latency.  

Tools for API load balancing:  
- **Nginx**, **HAProxy**, **AWS Load Balancer**.  

---

### **26. What is the difference between synchronous and asynchronous APIs?**  
| Feature | Synchronous API | Asynchronous API |
|---------|---------------|----------------|
| Request Handling | Waits for a response | Does not wait for response |
| Speed | Slower | Faster |
| Use Case | Payment processing | WebSockets, Notifications |

Example **Async API in Node.js**:  
```js
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

### **27. How do you prevent API abuse and DDoS attacks?**  
- **Rate Limiting** – Limit the number of requests per user.  
- **Authentication** – Require API keys, OAuth, JWT.  
- **Firewall & WAF** – Block malicious traffic (Cloudflare, AWS WAF).  
- **Bot Detection** – Use reCAPTCHA, AI-based filtering.  

---

### **28. How do you handle API version deprecation?**  
- **Deprecation Notices** – Inform users with warnings.  
- **Sunset Headers** – Include in API responses:  
  ```http
  Sunset: Wed, 01 Jan 2026 00:00:00 GMT
  ```  
- **Versioning** – Support multiple API versions (`v1`, `v2`).  
- **Feature Flags** – Gradually roll out changes.  

---

### **29. How do you implement authentication in APIs?**  
1. **API Keys** – Basic authentication with a static key.  
2. **JWT (JSON Web Tokens)** – Secure token-based authentication.  
3. **OAuth 2.0** – Third-party authentication (Google, Facebook).  
4. **Session-based authentication** – Uses cookies for authentication.  

Example JWT authentication in Python Flask:  
```python
@app.route('/protected')
@jwt_required()
def protected():
    return jsonify(message="Authenticated user")
```

---

### **30. What are the best practices for designing scalable APIs?**  
- **Use proper HTTP methods** (GET, POST, PUT, DELETE).  
- **Enable caching** to reduce database load.  
- **Implement rate limiting** to prevent abuse.  
- **Use pagination** for large datasets.  
- **Follow RESTful principles** for maintainability.  
- **Secure APIs** with OAuth, JWT, API Keys.  

---


### **1. How do you make an API request in React using `fetch()`?**  
You can use the built-in `fetch()` method to make an API request in React. Here's an example:  

```tsx
useEffect(() => {
  fetch("https://api.example.com/data")
    .then((response) => response.json()) // Convert response to JSON
    .then((data) => console.log(data)) // Handle the data
    .catch((error) => console.error("Error:", error)); // Handle errors
}, []);
```

---

### **2. How do you make an API request in React using `axios`?**  
Axios is a popular HTTP client that simplifies API requests. Example:  

```tsx
import axios from "axios";
import { useEffect } from "react";

useEffect(() => {
  axios.get("https://api.example.com/data")
    .then((response) => console.log(response.data)) // Handle response
    .catch((error) => console.error("Error:", error)); // Handle errors
}, []);
```

---

### **3. How can you handle errors while making an API request in React?**  
You can use `try...catch` in `async/await` or `.catch()` in Promises:  

**Using `fetch()`:**  
```tsx
const fetchData = async () => {
  try {
    const response = await fetch("https://api.example.com/data");
    if (!response.ok) throw new Error("Network error");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};
```

**Using `axios`:**  
```tsx
const fetchData = async () => {
  try {
    const response = await axios.get("https://api.example.com/data");
    console.log(response.data);
  } catch (error) {
    console.error("API request failed:", error);
  }
};
```

---

### **4. How do you send headers with an API request in React?**  
You can add custom headers using the `headers` option in `fetch()` or `axios`:  

**Using `fetch()`:**  
```tsx
fetch("https://api.example.com/data", {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_TOKEN",
  },
});
```

**Using `axios`:**  
```tsx
axios.get("https://api.example.com/data", {
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_TOKEN",
  },
});
```

---

### **5. How do you send a `POST` request with JSON data in React?**  
**Using `fetch()`:**  
```tsx
fetch("https://api.example.com/data", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ name: "John", age: 25 }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));
```

**Using `axios`:**  
```tsx
axios.post("https://api.example.com/data", { name: "John", age: 25 })
  .then((response) => console.log(response.data));
```

---

### **6. How can you handle API loading states in React?**  
Use a `useState` hook to track loading states:  

```tsx
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);

useEffect(() => {
  fetch("https://api.example.com/data")
    .then((response) => response.json())
    .then((data) => {
      setData(data);
      setLoading(false);
    })
    .catch((error) => console.error(error));
}, []);

return loading ? <p>Loading...</p> : <p>{JSON.stringify(data)}</p>;
```

---

### **7. How do you call an API inside `useEffect` in React?**  
Use the `useEffect` hook to call APIs when the component mounts:  

```tsx
useEffect(() => {
  fetch("https://api.example.com/data")
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
}, []); // Empty dependency array means it runs once on mount
```

---

### **8. How do you cancel an API request in React?**  
Use `AbortController` with `fetch()` or `axios.CancelToken`:  

**Using `fetch()`:**  
```tsx
useEffect(() => {
  const controller = new AbortController();
  fetch("https://api.example.com/data", { signal: controller.signal })
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((err) => {
      if (err.name !== "AbortError") console.error(err);
    });

  return () => controller.abort(); // Cleanup on unmount
}, []);
```

**Using `axios`:**  
```tsx
useEffect(() => {
  const source = axios.CancelToken.source();
  
  axios.get("https://api.example.com/data", { cancelToken: source.token })
    .then((res) => console.log(res.data))
    .catch((err) => {
      if (axios.isCancel(err)) console.log("Request canceled");
      else console.error(err);
    });

  return () => source.cancel(); // Cleanup on unmount
}, []);
```

---

### **9. How do you implement infinite scrolling with API requests in React?**  
Use `IntersectionObserver` to detect when the user reaches the bottom:  

```tsx
const [items, setItems] = useState([]);
const [page, setPage] = useState(1);
const observer = useRef(null);

useEffect(() => {
  fetch(`https://api.example.com/data?page=${page}`)
    .then((res) => res.json())
    .then((data) => setItems((prev) => [...prev, ...data]));
}, [page]);

const lastItemRef = useCallback((node) => {
  if (observer.current) observer.current.disconnect();
  observer.current = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) setPage((prev) => prev + 1);
  });
  if (node) observer.current.observe(node);
}, []);

return (
  <div>
    {items.map((item, index) => (
      <p key={index} ref={index === items.length - 1 ? lastItemRef : null}>
        {item.name}
      </p>
    ))}
  </div>
);
```

---

### **10. What is the difference between client-side and server-side API calls in React?**  

| Feature | Client-side API Calls | Server-side API Calls |
|---------|----------------------|----------------------|
| Execution | Runs in the browser | Runs on the backend |
| Performance | Can be slow for large data | Faster processing |
| SEO | Bad for SEO | Good for SEO |
| Security | Exposes API key if not secured | More secure |
| Example | Fetching data in `useEffect` | Fetching data in Next.js `getServerSideProps` |

**Example: Client-side fetch in React**  
```tsx
useEffect(() => {
  fetch("https://api.example.com/data")
    .then((res) => res.json())
    .then((data) => console.log(data));
}, []);
```

**Example: Server-side fetch in Next.js**  
```tsx
export async function getServerSideProps() {
  const res = await fetch("https://api.example.com/data");
  const data = await res.json();
  return { props: { data } };
}
```

---
