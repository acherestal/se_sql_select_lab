# main.py

# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Add code below and run file to see data from employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# employee number and last name (first 5 rows)
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees
    ORDER BY employeeNumber
    LIMIT 5;
    """,
    conn
)

# STEP 3
# same, but last name first
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees
    ORDER BY employeeNumber
    LIMIT 5;
    """,
    conn
)

# STEP 4
# alias employeeNumber as ID
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees
    ORDER BY employeeNumber
    LIMIT 5;
    """,
    conn
)

# STEP 5
# CASE role Executive vs Not Executive
df_executive = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName,
        jobTitle,
        CASE
            WHEN jobTitle = "President"
              OR jobTitle = "VP Sales"
              OR jobTitle = "VP Marketing"
            THEN "Executive"
            ELSE "Not Executive"
        END AS role
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# STEP 6
# length of last name only
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# STEP 7
# first two letters of job title only
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# Add the code below and run the file to see order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# total amount = sum of rounded (priceEach * quantityOrdered)
sum_total_price = pd.read_sql(
    """
    SELECT SUM(ROUND(priceEach * quantityOrdered, 0)) AS total_amount
    FROM orderDetails;
    """,
    conn
).iloc[0, 0]

# STEP 9
# day/month/year columns from orders.orderDate
df_day_month_year = pd.read_sql(
    """
    SELECT
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders
    ORDER BY orderDate;
    """,
    conn
)

# Close the connection
conn.close()
