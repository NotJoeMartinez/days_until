import sqlite3
import datetime
import sys
from io import StringIO




# print (diff.days)

conn = sqlite3.connect('daysuntil.db')

c = conn.cursor()
def add_event():
    event_name =  input('Name of event: ')
    event_date =  input('Date of event(Ex YYYY-MM-DD): ')
    c.execute("INSERT INTO dates VALUES ('{}', '{}' )".format(event_name, event_date))

def days_until():
    event_asked = input('Name of event requested: ')
    c.execute(" SELECT * FROM dates WHERE event ='{}'".format(event_asked))
    for a in c.fetchall():
        # print(a, a[1], type(a[1]))
        strdate = a[1]
        print(strdate)
        # yyyy-mm-dd
        year = strdate[0:4]
        month = strdate[5:7]
        day = strdate[8:10]

        future = datetime.date(int(year),int(month),int(day))
        today = datetime.date.today()
        diff = future - today
        print(diff)
    

