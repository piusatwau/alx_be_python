Here's a **comprehensive SQL CRUD (Create, Read, Update, Delete) operations cheatsheet** that covers the most important commands for manipulating data in a relational database.

---

## **1. Create Operation (INSERT)**

### **Insert a New Record into a Table**
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

- **`table_name`**: The name of the table where you want to insert data.
- **`column1, column2, ...`**: The columns in which you want to insert data.
- **`value1, value2, ...`**: The actual data values to be inserted.

#### Example:
```sql
INSERT INTO employees (first_name, last_name, department, salary)
VALUES ('John', 'Doe', 'Marketing', 60000);
```

### **Insert Multiple Rows at Once**
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES
    (value1a, value2a, value3a, ...),
    (value1b, value2b, value3b, ...),
    (value1c, value2c, value3c, ...);
```

#### Example:
```sql
INSERT INTO employees (first_name, last_name, department, salary)
VALUES
    ('Alice', 'Smith', 'HR', 55000),
    ('Bob', 'Jones', 'IT', 75000),
    ('Carol', 'White', 'Sales', 67000);
```

---

## **2. Read Operation (SELECT)**

### **Select Specific Columns from a Table**
```sql
SELECT column1, column2, ...
FROM table_name;
```

#### Example:
```sql
SELECT first_name, last_name, department
FROM employees;
```

### **Select All Columns from a Table**
```sql
SELECT * FROM table_name;
```

#### Example:
```sql
SELECT * FROM employees;
```

### **Filtering with WHERE Clause**
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

#### Example:
```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'IT';
```

### **Sorting the Results with ORDER BY**
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC];
```

#### Example:
```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```

### **Limiting the Number of Results with LIMIT**
```sql
SELECT column1, column2, ...
FROM table_name
LIMIT number;
```

#### Example:
```sql
SELECT first_name, last_name
FROM employees
LIMIT 5;
```

---

## **3. Update Operation (UPDATE)**

### **Update Specific Records in a Table**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- **`SET column1 = value1`**: Specifies the columns and new values.
- **`WHERE condition`**: Filters the records to be updated. Without `WHERE`, all records will be updated!

#### Example:
```sql
UPDATE employees
SET salary = 65000
WHERE employee_id = 3;
```

### **Update Multiple Records**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

#### Example:
```sql
UPDATE employees
SET department = 'Operations'
WHERE department = 'HR';
```

---

## **4. Delete Operation (DELETE)**

### **Delete Specific Records from a Table**
```sql
DELETE FROM table_name
WHERE condition;
```

- **`WHERE condition`**: Filters the records to delete. Without `WHERE`, all records in the table will be deleted!

#### Example:
```sql
DELETE FROM employees
WHERE employee_id = 10;
```

### **Delete All Records from a Table**
```sql
DELETE FROM table_name;
```

#### Example:
```sql
DELETE FROM employees;
```

---

## **5. Creating and Modifying Tables**

### **Create a New Table**
```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    ...
);
```

#### Example:
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);
```

### **Add a New Column to a Table**
```sql
ALTER TABLE table_name
ADD column_name datatype constraint;
```

#### Example:
```sql
ALTER TABLE employees
ADD hire_date DATE;
```

### **Drop a Column from a Table**
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

#### Example:
```sql
ALTER TABLE employees
DROP COLUMN hire_date;
```

### **Delete a Table**
```sql
DROP TABLE table_name;
```

#### Example:
```sql
DROP TABLE employees;
```

---

## **6. Constraints**

### **Primary Key**
Ensures the column uniquely identifies each record in the table.
```sql
CREATE TABLE table_name (
    column_name datatype PRIMARY KEY
);
```

#### Example:
```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);
```

### **Foreign Key**
Links two tables together and enforces referential integrity.
```sql
ALTER TABLE table_name
ADD CONSTRAINT fk_name FOREIGN KEY (column_name) REFERENCES other_table (column_name);
```

#### Example:
```sql
ALTER TABLE orders
ADD CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers (customer_id);
```

### **Unique**
Ensures that all values in a column are unique.
```sql
CREATE TABLE table_name (
    column_name datatype UNIQUE
);
```

#### Example:
```sql
CREATE TABLE users (
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE
);
```

### **Not Null**
Ensures that a column cannot have a `NULL` value.
```sql
CREATE TABLE table_name (
    column_name datatype NOT NULL
);
```

#### Example:
```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL
);
```

---

## **7. Transactions**

### **Starting a Transaction**
```sql
START TRANSACTION;
```

### **Committing a Transaction**
```sql
COMMIT;
```

### **Rolling Back a Transaction**
```sql
ROLLBACK;
```

#### Example:
```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

COMMIT;
```

---

## **8. Indexing**

### **Create an Index**
```sql
CREATE INDEX index_name
ON table_name (column_name);
```

#### Example:
```sql
CREATE INDEX idx_last_name
ON employees (last_name);
```

### **Drop an Index**
```sql
DROP INDEX index_name;
```

#### Example:
```sql
DROP INDEX idx_last_name;
```

---