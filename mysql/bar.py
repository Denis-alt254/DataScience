import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your MySQLHosting credentials
host = "db4free.net"
database = "georgew"
user = "georgew"
password = "12345george"
port = 3306

# Connect to the MySQL database
conn = mysql.connector.connect(
host=host,
user=user,
password=password,
database=database,
port=port
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Example query to retrieve all rows from the student table
query = "SELECT * FROM STUDENT"
wainaina = pd.read_sql(query, conn)

# Display the retrieved data
print(wainaina)

# Example: Bar chart of grades with y-axis starting from 0
plt.bar(wainaina['NAME'], wainaina['POINTS'], color='skyblue')  # Change the color as needed
plt.title('Student Performance')
plt.xlabel('Student Name')
plt.ylabel('Points')

# Rotate x-axis labels vertically
#plt.xticks(rotation='vertical')
plt.xticks(rotation=45)

# Set the y-axis limit to start from 0
plt.ylim(0, max(wainaina['POINTS']) + 10)  # You can adjust the additional value as needed

# Show grid
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Close the cursor and connection
cursor.close()
conn.close()