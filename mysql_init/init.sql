CREATE TABLE IF NOT EXISTS customers (
    customerNumber INT PRIMARY KEY,
    customerName VARCHAR(255),
    contactLastName VARCHAR(255),
    contactFirstName VARCHAR(255),
    phone VARCHAR(50),
    city VARCHAR(100),
    country VARCHAR(100),
    creditLimit DECIMAL(10, 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS orders (
    orderNumber INT PRIMARY KEY,
    customerNumber INT,
    orderDate DATE,
    status VARCHAR(50),
    comments TEXT,
);