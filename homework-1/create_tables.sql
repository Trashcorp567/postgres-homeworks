-- SQL-команды для создания таблиц
-- Таблица customers
CREATE TABLE customers
(
    customer_id text PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name text
);

-- Таблица employee
CREATE TABLE employee
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);

-- Таблица orders
CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id text REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employee(employee_id) NOT NULL,
	order_date date,
	ship_city text
);