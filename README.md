cursor.execute("SELECT * FROM YourTableName")
columns_info = [column[0] for column in cursor.description]
column_types = {column: 'desired_type' for column in columns_info}data files

