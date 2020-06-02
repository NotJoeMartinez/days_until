import db
import sqlite3, os



# c.execute(''' CREATE TABLE dates (
#                 event text, 
#                 date text
#             ) ''')

def main():
    print('''1: Add event\n2: Days until \n3: All Events\n''')
    print("==================================")
    choice = input("")
    if int(choice) == 1: 
        os.system("clear")
        print("You selected Add Event")
        db.add_event()
    if int(choice)==2: 
        os.system("clear")
        print("You selected Days Until")
        db.days_until()
    if int(choice)==3:
        os.system("clear")
        print("Showing All events:")
        db.view_dates() 
    # return  



    

if __name__ == "__main__": 
    main()
    db.conn.commit()
    db.conn.close() 