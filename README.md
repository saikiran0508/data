cursor.execute("SELECT * FROM YourTableName")
columns_info = [column[0] for column in cursor.description]
column_types = {column: 'desired_type' for column in columns_info}data files


import pandas as pd
from sqlalchemy import create_engine

# Read Excel file
excel_df = pd.read_excel("your_file.xlsx")

# Define SQLAlchemy connection string
conn_str = 'microsoft+pyodbc:///?odbc_connect=' + r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=your_database.accdb;'

# Create SQLAlchemy engine
engine = create_engine(conn_str)

# Append the Excel data to an existing table in Access
excel_df.to_sql('YourTableName', engine, if_exists='append', index=False, method='multi')

print("Data appended to Access database.")
