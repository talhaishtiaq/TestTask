import csv
from db import conn


db = conn
cursor = db.cursor()

with open('task_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    try:
        for row in csv_reader:
            if (line != 0):
                id = row[0]
                timestamp = row[1]
                temperature = row[2]
                duration = row[3]
                sql = "Insert into data(id, timestamp, temperature, duration) Values('"+id+"', '"+timestamp+"','"+temperature+"','"+duration+"');"
                cursor.execute(sql)
            line = line+1
        db.commit()
        print("data inserted into database")
    except Exception as e:
        print(e)
        db.rollback()
    cursor.close()
