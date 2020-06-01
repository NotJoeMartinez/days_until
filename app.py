import db
import sqlite3



# c.execute(''' CREATE TABLE dates (
#                 event text, 
#                 date text
#             ) ''')

def main():
    print('''1: Add event\n2: Days until ''')
    print("==================================")
    choice = input("")
    if int(choice) == 1: 
        print("You select Add Event")
        db.add_event()
    if int(choice)==2: 
        print("You select Days Until")
        db.days_until()
    # return  



    

if __name__ == "__main__": 
    main()
    db.conn.commit()
    db.conn.close() 