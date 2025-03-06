
# 🔥 SQL Interview Questions with Answers (Part 1)

## 1. What is SQL?
**SQL (Structured Query Language)** is a programming language used to **manage and manipulate relational databases**.  
It allows users to **insert, update, delete, and retrieve** data from a database.

✅ **Key Uses of SQL:**
- Creating and modifying database structures (**DDL**).
- Inserting, updating, and deleting data (**DML**).
- Controlling user permissions (**DCL**).
- Managing transactions (**TCL**).

---

## 2. What are the different types of SQL commands?
SQL commands are divided into **five categories**:

| Type | Commands | Purpose |
|------|---------|---------|
| **DDL (Data Definition Language)** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Defines or modifies database schema. |
| **DML (Data Manipulation Language)** | `INSERT`, `UPDATE`, `DELETE`, `SELECT` | Manipulates database records. |
| **DCL (Data Control Language)** | `GRANT`, `REVOKE` | Controls user access. |
| **TCL (Transaction Control Language)** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Manages transactions. |
| **DQL (Data Query Language)** | `SELECT` | Retrieves data from a database. |

---

## 3. What is the difference between DDL, DML, DCL, and TCL?
| Category | Description | Example Commands |
|----------|------------|-----------------|
| **DDL** | Defines database structure. | `CREATE`, `ALTER`, `DROP` |
| **DML** | Modifies data. | `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Manages permissions. | `GRANT`, `REVOKE` |
| **TCL** | Controls transactions. | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

🔹 **Example of DDL:**
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2)
);
```

---

## 4. What is a primary key?
A **primary key** is a **unique identifier** for each row in a table.

✅ **Characteristics:**
- Ensures **uniqueness** (no duplicates).
- Cannot contain **NULL** values.
- A table can have **only one primary key**.

🔹 **Example:**
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
```
Here, `student_id` uniquely identifies each student.

---

## 5. What is a foreign key?
A **foreign key** is a column that establishes a **relationship** between two tables.

✅ **Characteristics:**
- It **references** a primary key in another table.
- Ensures **referential integrity** (prevents orphan records).
- Can contain **duplicate** values.

🔹 **Example:**
```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```
Here, `customer_id` in `orders` refers to `customer_id` in the `customers` table.

---

## 6. What is the difference between CHAR and VARCHAR?
| Feature | CHAR | VARCHAR |
|---------|------|---------|
| **Storage Type** | Fixed-length | Variable-length |
| **Performance** | Faster for fixed-size data | Efficient for varying data sizes |
| **Padding** | Pads spaces for shorter values | Stores only actual characters |
| **Use Case** | Fixed-length fields like phone numbers | Varying-length fields like names |

🔹 **Example:**
```sql
CREATE TABLE users (
    username CHAR(10),  -- Always takes 10 bytes
    email VARCHAR(50)  -- Takes only required bytes
);
```

---

## 7. What is the difference between WHERE and HAVING?
Both **WHERE** and **HAVING** filter records, but they differ in usage:

| Clause | Used for | Works with |
|--------|---------|-----------|
| **WHERE** | Filters rows before aggregation | `SELECT`, `UPDATE`, `DELETE` |
| **HAVING** | Filters rows after aggregation | Aggregate functions (`SUM`, `COUNT`, etc.) |

🔹 **Example Using `WHERE`:**
```sql
SELECT * FROM employees WHERE salary > 50000;
```
🔹 **Example Using `HAVING`:**
```sql
SELECT department, AVG(salary) 
FROM employees 
GROUP BY department 
HAVING AVG(salary) > 50000;
```

---

## 8. What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN?
| Join Type | Description |
|-----------|------------|
| **INNER JOIN** | Returns only matching rows from both tables. |
| **LEFT JOIN** | Returns all rows from the left table and matching rows from the right. |
| **RIGHT JOIN** | Returns all rows from the right table and matching rows from the left. |
| **FULL JOIN** | Returns all rows from both tables. |

🔹 **Example Using `INNER JOIN`:**
```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.id;
```

✅ **Visual Representation:**
- **INNER JOIN** → 🎯 Only Matching Data
- **LEFT JOIN** → 🎯 All Left + Matching Right
- **RIGHT JOIN** → 🎯 All Right + Matching Left
- **FULL JOIN** → 🎯 Everything from Both Tables

---

## 9. What is the difference between UNION and UNION ALL?
| Feature | UNION | UNION ALL |
|---------|-------|-----------|
| **Duplicates** | Removes duplicates | Keeps duplicates |
| **Performance** | Slower (requires sorting) | Faster |
| **Use Case** | When duplicate rows should be removed | When all rows should be included |

🔹 **Example Using `UNION`:**
```sql
SELECT name FROM employees
UNION
SELECT name FROM customers;
```
🔹 **Example Using `UNION ALL`:**
```sql
SELECT name FROM employees
UNION ALL
SELECT name FROM customers;
```

---

## 10. What are constraints in SQL?
Constraints **enforce rules** on a table's data.

✅ **Types of Constraints:**
| Constraint | Description |
|------------|------------|
| **PRIMARY KEY** | Ensures uniqueness and non-null values. |
| **FOREIGN KEY** | Establishes a relationship between tables. |
| **UNIQUE** | Ensures all values in a column are unique. |
| **NOT NULL** | Prevents null values in a column. |
| **CHECK** | Enforces a specific condition on a column. |
| **DEFAULT** | Assigns a default value if no value is provided. |

🔹 **Example Using Constraints:**
```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) CHECK (salary > 0),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(dept_id)
);
```

---


## 11. What is a self join?
A **self join** is a join where a table is joined with itself.  
It is used to compare **rows within the same table**.

✅ **Example:** Finding employees and their managers (both stored in the same `employees` table).
```sql
SELECT e1.name AS Employee, e2.name AS Manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.emp_id;
```
Here, `e1` represents the employee, and `e2` represents their manager.

---

## 12. What is a cross join?
A **CROSS JOIN** returns the **Cartesian product** of two tables.  
Each row from the first table is **paired with every row** from the second table.

✅ **Example:**
```sql
SELECT product_name, category_name
FROM products
CROSS JOIN categories;
```
🔹 If `products` has 5 rows and `categories` has 3 rows, the result will have **5 × 3 = 15** rows.

---

## 13. What is a stored procedure?
A **stored procedure** is a precompiled SQL script that can be executed **multiple times**.  
It **reduces code duplication** and **improves performance**.

✅ **Example:**
```sql
CREATE PROCEDURE GetEmployeeDetails(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE id = emp_id;
END;
```
🔹 **Calling a stored procedure:**
```sql
CALL GetEmployeeDetails(101);
```

---

## 14. What is a trigger?
A **trigger** is an SQL script that automatically executes **before** or **after** specific database events.

✅ **Example: Logging changes in an `audit_log` table:**
```sql
CREATE TRIGGER after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
INSERT INTO audit_log (action, emp_id, timestamp)
VALUES ('INSERT', NEW.id, NOW());
```

🔹 This trigger **logs new employee insertions** automatically.

---

## 15. What is the difference between a stored procedure and a function?
| Feature | Stored Procedure | Function |
|---------|----------------|----------|
| **Return Value** | May or may not return a value | Always returns a value |
| **Use in Queries** | Cannot be used in `SELECT` | Can be used in `SELECT` |
| **Transaction Handling** | Supports transactions | No transaction support |
| **Example** | `CALL procedure_name();` | `SELECT function_name();` |

✅ **Example Function:**
```sql
CREATE FUNCTION GetTotalEmployees()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total FROM employees;
    RETURN total;
END;
```
🔹 **Usage:**  
```sql
SELECT GetTotalEmployees();
```

---

## 16. What is indexing in SQL?
An **index** is a data structure that **improves query performance** by allowing faster lookups.

✅ **Types of Indexes:**
1. **Primary Index** – Automatically created on the primary key.
2. **Unique Index** – Ensures unique values in a column.
3. **Composite Index** – Created on multiple columns.
4. **Clustered Index** – Physically arranges data in the table.
5. **Non-Clustered Index** – Stores pointers to the actual data.

✅ **Creating an Index:**
```sql
CREATE INDEX idx_employee_name ON employees (name);
```
🔹 This speeds up queries like:
```sql
SELECT * FROM employees WHERE name = 'John';
```

---

## 17. What are views in SQL?
A **view** is a **virtual table** that presents **query results** as a table.

✅ **Why use views?**
- **Security** – Restricts access to specific columns.
- **Simplification** – Hides complex queries.
- **Consistency** – Ensures data integrity.

✅ **Example:**
```sql
CREATE VIEW EmployeeSalary AS
SELECT name, salary FROM employees WHERE salary > 50000;
```
🔹 **Usage:**  
```sql
SELECT * FROM EmployeeSalary;
```

---

## 18. What is normalization? What are its types?
**Normalization** is the process of **organizing data** to **reduce redundancy** and improve integrity.

✅ **Types of Normalization:**
| Form | Purpose |
|------|---------|
| **1NF (First Normal Form)** | Removes duplicate columns & ensures atomicity. |
| **2NF (Second Normal Form)** | Removes partial dependencies. |
| **3NF (Third Normal Form)** | Removes transitive dependencies. |
| **BCNF (Boyce-Codd Normal Form)** | Stronger than 3NF, ensures strict dependency rules. |

✅ **Example of 1NF (Fixing Repeating Groups):**
**Before:**
| Student | Subjects |
|---------|---------|
| John | Math, Science |
| Alice | English, History |

**After Applying 1NF:**
| Student | Subject |
|---------|---------|
| John | Math |
| John | Science |
| Alice | English |
| Alice | History |

---

## 19. What is denormalization?
**Denormalization** is the **opposite of normalization** – it **adds redundancy** to improve query speed.

✅ **When to use?**
- When **performance is critical** (e.g., reporting databases).
- When **joins are slowing down queries**.

✅ **Example:**
Instead of having separate `orders` and `customers` tables, **denormalization** stores **customer details directly in `orders`**.

**Normalized (Separate Tables)**:
```sql
SELECT orders.id, customers.name 
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```

**Denormalized (Single Table)**:
```sql
SELECT id, customer_name FROM orders;
```

---

## 20. What is an ACID property in SQL?
**ACID** stands for **Atomicity, Consistency, Isolation, Durability** – ensuring reliable transactions.

✅ **ACID Breakdown:**
| Property | Description |
|----------|------------|
| **Atomicity** | A transaction is **all or nothing**. |
| **Consistency** | Database remains **valid** after transaction. |
| **Isolation** | Transactions are executed **independently**. |
| **Durability** | Changes are **permanent** after commit. |

✅ **Example: Banking Transaction**
```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;  -- Debit
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;  -- Credit
COMMIT;
```
🔹 **If an error occurs**, `ROLLBACK` ensures no money is lost!

---


## 21. What is a primary key?
A **primary key** is a column (or set of columns) that **uniquely identifies each row** in a table.

✅ **Characteristics of a Primary Key:**
- Must be **unique** for each row.
- Cannot contain **NULL** values.
- Each table **can have only one** primary key.

✅ **Example:**
```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);
```
🔹 Here, `emp_id` is the **primary key**.

---

## 22. What is a foreign key?
A **foreign key** is a column that **creates a relationship** between two tables by referring to a **primary key** in another table.

✅ **Example:**
```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```
🔹 `customer_id` in `orders` refers to `customer_id` in `customers`.

---

## 23. What is the difference between UNION and UNION ALL?
Both **UNION** and **UNION ALL** combine results from multiple `SELECT` queries.

| Feature | UNION | UNION ALL |
|---------|-------|-----------|
| **Removes Duplicates** | ✅ Yes | ❌ No |
| **Performance** | Slower | Faster |
| **Usage** | When duplicates are unnecessary | When all records are needed |

✅ **Example:**
```sql
SELECT city FROM customers
UNION
SELECT city FROM suppliers;
```
🔹 **Removes duplicates**  
```sql
SELECT city FROM customers
UNION ALL
SELECT city FROM suppliers;
```
🔹 **Keeps duplicates**

---

## 24. What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?
These **window functions** assign ranks to rows **based on a column's values**.

| Function | Duplicates? | Gaps in Rank? |
|----------|------------|--------------|
| **RANK()** | ✅ Allows | ✅ Yes |
| **DENSE_RANK()** | ✅ Allows | ❌ No |
| **ROW_NUMBER()** | ❌ No | ❌ No |

✅ **Example:**
```sql
SELECT name, department, salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_number
FROM employees;
```

---

## 25. What is a common table expression (CTE)?
A **CTE** is a temporary result set used in queries to **improve readability and reuse logic**.

✅ **Example:**
```sql
WITH TopSalaries AS (
    SELECT name, department, salary
    FROM employees
    WHERE salary > 50000
)
SELECT * FROM TopSalaries;
```
🔹 **Benefits of CTEs**:
- Improves readability
- Can be referenced multiple times
- Helps in **recursive queries**

---

## 26. What is the difference between DELETE, TRUNCATE, and DROP?
| Operation | Removes Data | Removes Structure | Speed |
|-----------|-------------|------------------|-------|
| **DELETE** | ✅ Rows | ❌ No | Slow (Logged) |
| **TRUNCATE** | ✅ All Rows | ❌ No | Faster |
| **DROP** | ✅ Entire Table | ✅ Yes | Fastest |

✅ **Example:**
```sql
DELETE FROM employees WHERE id = 10;  -- Removes a specific row
TRUNCATE TABLE employees;  -- Removes all rows but keeps structure
DROP TABLE employees;  -- Deletes table completely
```

---

## 27. What are window functions in SQL?
**Window functions** perform calculations **across a set of rows** but do **not group them** into a single output.

✅ **Common Window Functions:**
1. `RANK()` – Assigns a rank with gaps.
2. `DENSE_RANK()` – Assigns a continuous rank.
3. `ROW_NUMBER()` – Assigns a unique row number.
4. `SUM() OVER()` – Calculates a running sum.
5. `AVG() OVER()` – Calculates a moving average.

✅ **Example:**
```sql
SELECT name, department, salary,
    SUM(salary) OVER (PARTITION BY department) AS department_salary
FROM employees;
```
🔹 This calculates the **total salary** for each department **without grouping rows**.

---

## 28. What is a recursive CTE?
A **recursive CTE** allows a query to **call itself** until it reaches a stopping condition.

✅ **Use Case:** Finding a **hierarchical structure** (e.g., Employees & Managers).

✅ **Example:**
```sql
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT emp_id, name, manager_id
    FROM employees
    WHERE manager_id IS NULL  -- Start with top-level managers

    UNION ALL

    SELECT e.emp_id, e.name, e.manager_id
    FROM employees e
    JOIN EmployeeHierarchy eh ON e.manager_id = eh.emp_id
)
SELECT * FROM EmployeeHierarchy;
```
🔹 This query **retrieves the full employee hierarchy**.

---

## 29. What is an execution plan?
An **execution plan** shows **how SQL Server executes a query**.

✅ **Checking the Execution Plan:**
```sql
EXPLAIN SELECT * FROM employees WHERE salary > 50000;
```
🔹 **Common Execution Plan Terms:**
- **Seq Scan (Sequential Scan):** Scans the entire table.
- **Index Scan:** Uses an index to improve performance.
- **Index Seek:** Finds specific records quickly.
- **Nested Loop Join:** Joins small datasets efficiently.

---

## 30. How to optimize SQL queries?
**SQL optimization** improves query performance. Some best practices:

✅ **1. Use Indexes:**
```sql
CREATE INDEX idx_employee_name ON employees (name);
```

✅ **2. Avoid SELECT * (Specify Columns):**
```sql
SELECT name, salary FROM employees;
```

✅ **3. Use EXISTS Instead of IN:**
```sql
SELECT name FROM employees WHERE EXISTS (
    SELECT 1 FROM departments WHERE employees.dept_id = departments.id
);
```

✅ **4. Avoid Unnecessary Joins:**
```sql
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

✅ **5. Use Query Caching (if supported by DBMS).**

---
