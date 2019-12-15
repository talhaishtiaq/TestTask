import mysql.connector


username = 'test_task'
password = 'Test_Task1@'
database = 'test_task'

try:
    conn = mysql.connector.connect(host = "localhost",
              user = username,
              password = password,
              database = database,
              auth_plugin='mysql_native_password')
except Exception as e:
    print(e)
    print("cannot connect to database")
