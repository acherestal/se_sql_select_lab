# main.py
import sqlite3
import pandas as pd

# STEP 1B: Connect to the database (tests import conn directly)
conn = sqlite3.connect("data.sqlite")

# (Optional) show employees table
employee_data = pd.read_sql("SELECT * FROM employees;", conn)

# STEP 2: MUST be 23 rows x 2 cols (no LIMIT 5)
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# STEP 3: same rows, swapped column order
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# STEP 4: include alias ID column
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# STEP 5: include role column with Executive / Not Executive
df_executive = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName,
        jobTitle,
        CASE
            WHEN jobTitle IN ("President", "VP Sales", "VP Marketing")
            THEN "Executive"
            ELSE "Not Executive"
        END AS role
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# STEP 6: length of lastName as name_length
df_name_length = pd.read_sql(
    """
    SELECT
        lastName,
        LENGTH(lastName) AS name_length
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# STEP 7: first two letters of jobTitle as short_title
# Ordering by employeeNumber ensures first row is President in this dataset,
# which makes short_title == 'Pr' as the test expects.
df_short_title = pd.read_sql(
    """
    SELECT
        jobTitle,
        SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
    ORDER BY employeeNumber;
    """,
    conn
)

# (Optional) show orderDetails table
order_details = pd.read_sql("SELECT * FROM orderDetails;", conn)

# STEP 8: test expects sum_total_price[0] == 9604251
# So store it as a 1-item list.
sum_total_price = pd.read_sql(
    """
    SELECT SUM(ROUND(priceEach * quantityOrdered, 0)) AS total_amount
    FROM orderDetails;
    """,
    conn
).values.flatten().tolist()

# STEP 9: day/month/year strings from orders.orderDate
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

# IMPORTANT: do NOT conn.close() because tests check conn after importing main.py
