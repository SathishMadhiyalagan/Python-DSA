

### **Basic SQL Interview Questions**
1. **What is SQL?**
2. What are the different types of SQL commands? (DDL, DML, DCL, TCL)
3. Explain the difference between `WHERE` and `HAVING` clauses.
4. How do you fetch all the rows from a table?
5. What is the difference between `CHAR` and `VARCHAR`?
6. Explain primary key, foreign key, and unique key.
7. What are constraints in SQL? Name a few types.
8. What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?
9. How do you create a table in SQL?
10. What is a NULL value? How is it different from zero or an empty string?

---

### **Intermediate SQL Interview Questions**
1. Write a query to find the second highest salary in a table.
2. How can you fetch only unique records from a table?
3. Explain the difference between `JOIN` and `UNION`.
4. What are the different types of JOINs? Provide examples for each.
5. Write a query to find employees who earn more than the average salary.
6. How do you use subqueries in SQL?
7. Explain the difference between correlated and non-correlated subqueries.
8. What is an index in SQL? Why is it used?
9. What are views in SQL? How do you create and use them?
10. Explain the concept of normalization and its various forms.

---

### **Advanced SQL Interview Questions**
1. Write a query to find duplicate rows in a table.
2. How do you optimize a SQL query for better performance?
3. Explain window functions and their applications.
4. What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`?
5. How do transactions work in SQL? What are ACID properties?
6. Explain the difference between clustered and non-clustered indexes.
7. Write a query to fetch the top N rows by a specific column.
8. What is a stored procedure? How is it different from a function?
9. How do you handle deadlocks in a database?
10. Explain CTE (Common Table Expressions) and its benefits.

---

### **Scenario-Based SQL Questions**
1. Write a query to find the department with the highest number of employees.
2. Given a table with columns `employee_id`, `manager_id`, and `salary`, write a query to find the manager who manages the most employees.
3. Write a query to find all employees who joined in the last 6 months.
4. Given a sales table, write a query to find the top 3 products by revenue.
5. How do you write a recursive query to find a hierarchy (e.g., employees under a specific manager)?

---

### **Miscellaneous SQL Questions**
1. What are stored functions? How are they different from stored procedures?
2. What is the difference between OLTP and OLAP?
3. What are triggers? Provide an example use case.
4. Explain the concept of foreign key constraints with cascading actions (`ON DELETE CASCADE`, `ON UPDATE CASCADE`).
5. How do you enforce referential integrity in SQL?

---

---

### **Basic SQL Interview Questions and Answers**

1. **What is SQL?**  
   SQL (Structured Query Language) is a standardized programming language used to manage and manipulate relational databases. It is used to perform tasks such as querying, updating, inserting, and deleting data.

2. **What are the different types of SQL commands?**
   - **DDL (Data Definition Language):** `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.
   - **DML (Data Manipulation Language):** `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
   - **DCL (Data Control Language):** `GRANT`, `REVOKE`.
   - **TCL (Transaction Control Language):** `COMMIT`, `ROLLBACK`, `SAVEPOINT`.

3. **Explain the difference between `WHERE` and `HAVING` clauses.**  
   - `WHERE` filters rows **before aggregation**.  
   - `HAVING` filters rows **after aggregation**.  
   Example:  
   ```sql
   SELECT department, COUNT(*) 
   FROM employees 
   WHERE salary > 3000 
   GROUP BY department 
   HAVING COUNT(*) > 5;
   ```

4. **How do you fetch all the rows from a table?**  
   Use the `SELECT` statement:  
   ```sql
   SELECT * FROM table_name;
   ```

5. **What is the difference between `CHAR` and `VARCHAR`?**  
   - **`CHAR`:** Fixed-length storage. Always uses the defined length, padding with spaces if necessary.  
   - **`VARCHAR`:** Variable-length storage. Only uses space for the actual content.  

6. **Explain primary key, foreign key, and unique key.**  
   - **Primary Key:** Uniquely identifies a row. Cannot have `NULL` values.  
   - **Foreign Key:** Establishes a relationship between two tables. References a column in another table.  
   - **Unique Key:** Ensures all values in the column are unique. Can have one `NULL` value.

7. **What are constraints in SQL? Name a few types.**  
   Constraints are rules applied to table columns to enforce data integrity.  
   Types:  
   - `NOT NULL`  
   - `UNIQUE`  
   - `PRIMARY KEY`  
   - `FOREIGN KEY`  
   - `CHECK`  
   - `DEFAULT`

8. **What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?**  
   - **`DELETE`:** Removes specific rows. Can use `WHERE`. Rows can be rolled back.  
   - **`TRUNCATE`:** Removes all rows. Cannot use `WHERE`. Faster than `DELETE`. Cannot be rolled back.  
   - **`DROP`:** Removes the table or database entirely. Cannot be rolled back.  

9. **How do you create a table in SQL?**  
   ```sql
   CREATE TABLE employees (
       id INT PRIMARY KEY,
       name VARCHAR(50),
       age INT,
       salary DECIMAL(10, 2)
   );
   ```

10. **What is a NULL value? How is it different from zero or an empty string?**  
    - **NULL:** Represents missing or undefined data.  
    - **Zero (0):** A numeric value.  
    - **Empty string (''):** A string with no characters.  
    Example:  
    ```sql
    SELECT * FROM table_name WHERE column_name IS NULL;
    ```

---

### **Intermediate SQL Interview Questions and Answers**

---

1. **Write a query to find the second highest salary in a table.**  
   ```sql
   SELECT MAX(salary) AS second_highest_salary
   FROM employees
   WHERE salary < (SELECT MAX(salary) FROM employees);
   ```

2. **How can you fetch only unique records from a table?**  
   Use the `DISTINCT` keyword:  
   ```sql
   SELECT DISTINCT column_name FROM table_name;
   ```

3. **Explain the difference between `JOIN` and `UNION`.**  
   - **JOIN:** Combines rows from multiple tables based on a related column.  
   - **UNION:** Combines the results of two or more `SELECT` queries into a single result set.  
   Example for UNION:  
   ```sql
   SELECT name FROM employees 
   UNION 
   SELECT name FROM managers;
   ```

4. **What are the different types of JOINs? Provide examples for each.**  
   - **INNER JOIN:** Returns matching rows from both tables.  
     ```sql
     SELECT e.name, d.department_name
     FROM employees e
     INNER JOIN departments d
     ON e.department_id = d.id;
     ```
   - **LEFT JOIN:** Returns all rows from the left table and matching rows from the right.  
   - **RIGHT JOIN:** Returns all rows from the right table and matching rows from the left.  
   - **FULL OUTER JOIN:** Returns rows when there’s a match in either table.  
   - **CROSS JOIN:** Produces a Cartesian product of two tables.

5. **Write a query to find employees who earn more than the average salary.**  
   ```sql
   SELECT name, salary 
   FROM employees 
   WHERE salary > (SELECT AVG(salary) FROM employees);
   ```

6. **How do you use subqueries in SQL?**  
   A subquery is a query inside another query.  
   Example:  
   ```sql
   SELECT name 
   FROM employees 
   WHERE department_id = (SELECT id FROM departments WHERE name = 'IT');
   ```

7. **Explain the difference between correlated and non-correlated subqueries.**  
   - **Correlated Subquery:** Depends on the outer query for execution.  
   - **Non-Correlated Subquery:** Can execute independently of the outer query.  

8. **What is an index in SQL? Why is it used?**  
   An index is a database object that improves query performance by allowing faster retrieval of rows. It is like a pointer to data.  
   Example:  
   ```sql
   CREATE INDEX idx_name ON employees(name);
   ```

9. **What are views in SQL? How do you create and use them?**  
   Views are virtual tables based on SQL queries.  
   Example:  
   ```sql
   CREATE VIEW employee_view AS 
   SELECT name, department 
   FROM employees 
   WHERE salary > 5000;
   ```

10. **Explain the concept of normalization and its various forms.**  
    - **Normalization:** Process of organizing data to reduce redundancy.  
      Forms:  
      - **1NF (First Normal Form):** Ensures each column has atomic values.  
      - **2NF (Second Normal Form):** Ensures no partial dependencies.  
      - **3NF (Third Normal Form):** Removes transitive dependencies.  
      - **BCNF (Boyce-Codd Normal Form):** More stringent than 3NF.

---

### **Advanced SQL Interview Questions and Answers**

---

1. **Write a query to find duplicate rows in a table.**  
   ```sql
   SELECT column1, column2, COUNT(*) 
   FROM table_name 
   GROUP BY column1, column2 
   HAVING COUNT(*) > 1;
   ```

2. **How do you optimize a SQL query for better performance?**  
   - Use proper indexing on frequently searched columns.  
   - Avoid `SELECT *` and query only required columns.  
   - Use joins instead of subqueries wherever possible.  
   - Use `EXPLAIN` or `EXPLAIN PLAN` to analyze query performance.  
   - Avoid unnecessary use of `DISTINCT`, `ORDER BY`, and `GROUP BY`.

3. **Explain window functions and their applications.**  
   Window functions perform calculations across a set of rows related to the current row. Common functions include `ROW_NUMBER()`, `RANK()`, and `SUM()`.  
   Example:  
   ```sql
   SELECT name, department, salary, 
          RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
   FROM employees;
   ```

4. **What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`?**  
   - **`ROW_NUMBER()`**: Assigns a unique sequential number to rows.  
   - **`RANK()`**: Assigns ranks to rows, with gaps for ties.  
   - **`DENSE_RANK()`**: Assigns ranks without gaps for ties.

5. **How do transactions work in SQL? What are ACID properties?**  
   - A transaction is a unit of work executed as a whole.  
   - **ACID properties:**  
     - **Atomicity:** All or nothing.  
     - **Consistency:** Maintains database integrity.  
     - **Isolation:** Ensures transactions don’t interfere with each other.  
     - **Durability:** Changes are permanent once committed.

6. **Explain the difference between clustered and non-clustered indexes.**  
   - **Clustered Index:** Sorts and stores rows physically in order. Only one per table.  
   - **Non-Clustered Index:** Stores pointers to the physical rows. Multiple can exist.

7. **Write a query to fetch the top N rows by a specific column.**  
   - **MySQL:**  
     ```sql
     SELECT * FROM employees ORDER BY salary DESC LIMIT N;
     ```
   - **SQL Server:**  
     ```sql
     SELECT TOP N * FROM employees ORDER BY salary DESC;
     ```

8. **What is a stored procedure? How is it different from a function?**  
   - **Stored Procedure:** Precompiled SQL code executed with optional parameters. Can perform multiple actions and return zero or more results.  
   - **Function:** Returns a single value or table. Used mainly for calculations.  
   Example Stored Procedure:  
   ```sql
   CREATE PROCEDURE GetEmployeesByDepartment(@dept_id INT) 
   AS 
   BEGIN 
       SELECT * FROM employees WHERE department_id = @dept_id; 
   END;
   ```

9. **How do you handle deadlocks in a database?**  
   - Use transaction timeouts.  
   - Access resources in the same order in all transactions.  
   - Use shorter transactions to reduce lock duration.  
   - Avoid user interaction during transactions.

10. **Explain CTE (Common Table Expressions) and its benefits.**  
    CTE is a temporary result set defined within a `WITH` clause, used for better readability and reusability.  
    Example:  
    ```sql
    WITH EmployeeCTE AS (
        SELECT department_id, AVG(salary) AS avg_salary
        FROM employees
        GROUP BY department_id
    )
    SELECT * 
    FROM EmployeeCTE 
    WHERE avg_salary > 5000;
    ```

---

### **Scenario-Based SQL Questions with Answers**

---

#### **1. Write a query to find the department with the highest number of employees.**
```sql
SELECT department_id, COUNT(*) AS employee_count 
FROM employees 
GROUP BY department_id 
ORDER BY employee_count DESC 
LIMIT 1;
```
This query groups employees by `department_id`, counts them, and sorts by the count in descending order, returning the top row.

---

#### **2. Given a table with columns `employee_id`, `manager_id`, and `salary`, write a query to find the manager who manages the most employees.**
```sql
SELECT manager_id, COUNT(*) AS employee_count 
FROM employees 
GROUP BY manager_id 
ORDER BY employee_count DESC 
LIMIT 1;
```
This groups employees by `manager_id`, counts the employees under each manager, and selects the manager with the highest count.

---

#### **3. Write a query to find all employees who joined in the last 6 months.**
```sql
SELECT * 
FROM employees 
WHERE join_date >= DATE_ADD(CURDATE(), INTERVAL -6 MONTH);
```
This query uses `DATE_ADD` to calculate the date 6 months before the current date (`CURDATE`) and filters employees who joined on or after that date.

---

#### **4. Given a sales table, write a query to find the top 3 products by revenue.**
```sql
SELECT product_id, SUM(revenue) AS total_revenue 
FROM sales 
GROUP BY product_id 
ORDER BY total_revenue DESC 
LIMIT 3;
```
This calculates the total revenue for each product, sorts them by revenue in descending order, and returns the top 3 products.

---

#### **5. How do you write a recursive query to find a hierarchy (e.g., employees under a specific manager)?**
```sql
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT employee_id, manager_id, name 
    FROM employees 
    WHERE manager_id IS NULL  -- Start with the top-level manager
    UNION ALL
    SELECT e.employee_id, e.manager_id, e.name 
    FROM employees e
    INNER JOIN EmployeeHierarchy eh 
    ON e.manager_id = eh.employee_id
)
SELECT * FROM EmployeeHierarchy;
```

---

### **Miscellaneous SQL Questions with Answers**

---

#### **1. What are stored functions? How are they different from stored procedures?**
- **Stored Functions:**  
  Functions return a single value and are used in SQL expressions.  
  Example:  
  ```sql
  CREATE FUNCTION GetTotalRevenue() RETURNS DECIMAL(10, 2)
  BEGIN
      RETURN (SELECT SUM(revenue) FROM sales);
  END;
  ```

- **Stored Procedures:**  
  Procedures perform multiple operations and can return multiple results but are invoked independently, not within a query.  
  Example:  
  ```sql
  CREATE PROCEDURE GetEmployeeCount()
  BEGIN
      SELECT COUNT(*) FROM employees;
  END;
  ```

---

#### **2. What is the difference between OLTP and OLAP?**
- **OLTP (Online Transaction Processing):**  
  Used for real-time transactional systems (e.g., banking, e-commerce). Focuses on CRUD operations.  
  Example: Inserting a new order in an e-commerce database.
  
- **OLAP (Online Analytical Processing):**  
  Used for analysis and reporting on historical data (e.g., data warehouses). Focuses on queries and aggregations.  
  Example: Generating a sales report by region over a year.

---

#### **3. What are triggers? Provide an example use case.**
- **Triggers:**  
  Automatically executed SQL code in response to events (`INSERT`, `UPDATE`, `DELETE`) on a table.  
  Example:  
  ```sql
  CREATE TRIGGER UpdateStock AFTER INSERT ON sales
  FOR EACH ROW
  BEGIN
      UPDATE products 
      SET stock = stock - NEW.quantity 
      WHERE id = NEW.product_id;
  END;
  ```
  **Use Case:** Deduct stock automatically after a sale is recorded.

---

#### **4. Explain the concept of foreign key constraints with cascading actions (`ON DELETE CASCADE`, `ON UPDATE CASCADE`).**
- A **foreign key** enforces referential integrity between tables.  
- **`ON DELETE CASCADE`**: Automatically deletes rows in the child table when the parent row is deleted.  
- **`ON UPDATE CASCADE`**: Updates foreign key values in the child table when the parent key is updated.  
  Example:  
  ```sql
  CREATE TABLE orders (
      order_id INT PRIMARY KEY,
      customer_id INT,
      FOREIGN KEY (customer_id) REFERENCES customers(id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
  );
  ```

---

#### **5. How do you enforce referential integrity in SQL?**
- Use **foreign keys** to link tables.  
- Define constraints to prevent orphaned or inconsistent data.  
  Example:  
  ```sql
  ALTER TABLE orders 
  ADD CONSTRAINT fk_customer 
  FOREIGN KEY (customer_id) 
  REFERENCES customers(id);
  ```

---
