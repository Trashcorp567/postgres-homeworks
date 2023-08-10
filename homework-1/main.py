"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

# Параметры подключения к базе данных
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='jj15mnbl'
)
cur = conn.cursor()

# Загрузка данных в таблицу employees
with open('north_data/employees_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропустить заголовок CSV-файла
    for row in reader:
        employee_id, first_name, last_name, title, birth_date, notes = row
        cur.execute(
            "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)",
            (employee_id, first_name, last_name, title, birth_date, notes)
        )

# Загрузка данных в таблицу customers
with open('north_data/customers_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропустить заголовок CSV-файла
    for row in reader:
        customer_id, company_name, contact_name = row
        cur.execute(
            "INSERT INTO customers VALUES (%s, %s, %s)",
            (customer_id, company_name, contact_name)
        )

# Загрузка данных в таблицу orders
with open('north_data/orders_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропустить заголовок CSV-файла
    for row in reader:
        order_id, customer_id, employee_id, order_date, ship_city = row
        cur.execute(
            "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
            (order_id, customer_id, employee_id, order_date, ship_city)
        )

conn.commit()
cur.close()
conn.close()