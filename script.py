import requests
import json
import mysql.connector
import os

hdhomerun = os.environ['HDHOMERUN']
dbhost = os.environ['DBHOST']
database = os.environ['DATABASE']
dbuser = os.environ['DBUSER']
dbpass = os.environ['DBPASS']

r = requests.get('http://{}/lineup.json?show=found'.format(hdhomerun))

data = r.json()

mydb = mysql.connector.connect(
  host=dbhost,
  database=database,
  user=dbuser,
  password=dbpass
)

mycursor = mydb.cursor()

print("Setting every channel in table to visible=0!")
sql = "UPDATE channel set visible = 0;"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

for key in data:
  if key.get('HD'):
    if not key.get('DRM'):
      print("{} {}".format(key['GuideNumber'], key['GuideName']))
      sql = "UPDATE channel set visible = 1 WHERE channum = {};".format(key['GuideNumber'])
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) affected")

print("All done! Stay safe out there boys and girls.")
