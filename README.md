# Test Task

No framework is used because of very simple requirements of the task.
Task is done by two different python scripts which uses the same database configuration file.

## Database:

Mysql database is used and configurations are in db.py
Run mysql database server on a host machine and create "data" and "logs" tables.
SQL for creating tables is in following files:
data.sql
logs.sql

Because of precision, values are not converted into numbers (e.g int, float, double). values are stored in form of string in the database and can be converted to numbers for calculation.


## Installation:

Python3 and pip3 are required to be installed already.
To install python3 mysql packages run following command:
```
pip3 install -r requirements.txt
```
It will install the packages written in requirements.txt

## Reading and inserting data:

to read from csv file and insert into database run following command from this directory:
```
python3 save_data.py
```
It will read the data from csv file and insert into the "data" table.

## Serve and Show data:

Python3 http.server is used to show data. It uses SimpleHTTPRequestHandler to return html.
Due to simplicity of the task no framework is used.

run following command from this directory to serve:
```
python3 serve.py
```
Webpage will be accessible on ```http://localhost:8080/``` which shows the data in a simple html table.
