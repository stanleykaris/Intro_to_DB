---We are going to create a database
USE alx_book_store;

--We shall start by creating a table for books
CREATE TABLE Books (
book_id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(130) NOT NULL,
author_id INT,
price DOUBLE NOT NULL,
publication_date DATE,
FOREIGN KEY (author_id) REFERENCES Authors (author_id) ON DELETE SET NULL
);

--We create table for Authors

CREATE TABLE Authors(
author_id INT AUTO_INCREMENT PRIMARY KEY,
author_name VARCHAR(215) NOT NULL
);

--We create table for Customers

CREATE TABLE Customers(
customer_id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(215) NOT NULL,
email VARCHAR(215) UNIQUE NOT NULL,
address TEXT    
);

--Create table for Orders
CREATE TABLE Orders(
order_id INT AUTO_INCREMENT PRIMARY KEY,
customer_id INT,
order_date DATE NOT NULL,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE   
);

--Create table for Order details

CREATE TABLE Order_Details(
orderdetail_id INT AUTO_INCREMENT PRIMARY KEY,
order_id INT,
book_id INT,
quantity DOUBLE  NOT NULL CHECK (quantity > 0),
FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE
);