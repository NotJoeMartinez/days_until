import sqlite3
import datetime
import os
import sys
from io import StringIO


conn = sqlite3.connect('daysuntil.db')
c = conn.cursor()

# turns result of fetchall object to datetime stuff
def format_dates(foo):
    # turn event[1] into readable date object to check if it is in the past
    year = foo[0:4]
    month = foo[5:7]
    day = foo[8:10]
    formated_date = datetime.date(int(year),int(month),int(day))
    return formated_date

# Prints all future dates
def view_dates():
    c.execute("SELECT * FROM dates WHERE date >= date('now')")
    c.fetchall
    for i in c.fetchall():
        print("{} ---> {}".format(i[0],i[1]))
    
# Adds even to database
def add_event():
    event_name =  input('Name of event: ')
    ##TODO: Input Validation
    event_date =  input('Date of event(Ex YYYY-MM-DD): ')
    c.execute("INSERT INTO dates VALUES ('{}', '{}' )".format(event_name, event_date))

# Prints days until next event along with events to chose from 
def days_until():
    # clear console 
    os.system("clear")
    print("Avalable events: ")
    view_dates()
    print("======================")
    event_asked = input('Name of event requested: ')
    c.execute(" SELECT * FROM dates WHERE event ='{}'".format(event_asked))
    # collect everything from previous statment and apply arithmetic to it
    for a in c.fetchall():
        strdate = a[1]
        # yyyy-mm-dd
        today = datetime.date.today()
        diff = format_dates(strdate) - today
        print(str(diff.days) + " Days until {}".format(event_asked))
    

