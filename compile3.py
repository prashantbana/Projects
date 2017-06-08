#Requries SQLite Database Manager to perform database actions

import sqlite3


db = sqlite3.connect('compile')
cursor = db.cursor()

newdict = {}
name = []
phone = []
email = []

cursor.execute('''CREATE TABLE information(name TEXT,phone INTEGER, email TEXT unique )''')

def make():
    
    count = int(raw_input('How many entries do you want?'))    
    for i in range(count):
        name1 = raw_input('Enter your name: ')
        phone1 = raw_input('Enter your phone number: ')
        email1 = raw_input('Enter your email: ')
        cursor.execute('''INSERT INTO information(name,phone,email)VALUES(?,?,?)''',(name1,phone1,email1))
    
        db.commit()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        
 
def search():
    
    count = int(raw_input('How many searches will you perform ?'))
    
    for i in range(count):
        name2 = raw_input('Enter name: ')
        cursor.execute('''SELECT name,phone,email FROM information WHERE name = ?''',(name2,))
        user1 = cursor.fetchall()
        for row in user1:
            print row
        db.commit()
    

def address_book():
    
    cursor.execute("SELECT * FROM information")
    print (cursor.fetchall())
    
def open_table():
    
    tabname = raw_input('Enter the file name: ')
    db1 = sqlite3.connect(tabnam)
    search1()
    def search1():
    
        count = int(raw_input('How many searches will you perform ?'))
    
        for i in range(count):
            name2 = raw_input('Enter name: ')
            cursor.execute('''SELECT name,phone,email FROM information WHERE name = ?''',(name2,))
            user1 = cursor.fetchall()
            for row in user1:
                print row
                db1.commit()
       
    
def display():

    print "-------------------ADDRESS BOOK-----------------------"

    print "1. Make an entry"
    print "2. Search"
    print "3. Print Address Book"
    print "4. Open Table"
    print "5. Exit"

    inp1 = raw_input(">")

    if(inp1 == '1'):  
        make()
        return display()   

    elif(inp1 == '2'):
        search()
        return display()
    
    elif(inp1 == '3'):
        address_book()
        return display()
        
    elif(inp1 == '4'):
        open_table()
        display()
    
    elif(inp1 == '5'):
        exit()
    
    
    
display()
db.close()
    
            
         
                
             
