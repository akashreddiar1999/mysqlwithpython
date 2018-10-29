import sqlite3 as sql

base=sql.connect('Python.db')
c=base.cursor()

def create_item():

    c.execute("CREATE TABLE IF NOT EXISTS Item(Itemno INT,Iname TEXT,Price INT,Quantity INT)")
    base.commit()



def insert_values():
    
    c.execute("INSERT INTO Item VALUES(101,'Geometry Box',50,100)")
    c.execute("INSERT INTO Item VALUES(102,'Soap',100,50)")
    c.execute("INSERT INTO Item VALUES(103,'Perfume',150,25)")
    c.execute("INSERT INTO Item VALUES(104,'Pen',50,200)")
    c.execute("INSERT INTO Item VALUES(105,'Pencil',20,100)")
    base.commit()





#a)Display all items information

def display_table():
    print("a)Display all items information")
    print("\n")
    c.execute("Select * from Item")
    print("%-10s"%("Itemno"),"%-15s"%("Iname"),"%-  15s"%("Price"),"Quantity")
    
    for row in c.fetchall():
        print("%-10s"%(row[0]),end=' ')
        print("%-15s"%(row[1]),end=' ')
        print("%-15s"%(row[2]),end=' ')
        print(row[3])


create_item()

#b)Display item name and price value

def dispay_iname_price():

    print("\n")
    print("b)Display item name and price value")
    print("\n")
    c.execute("Select Iname,Price from Item")
    print("%-15s"%("Iname"),"Price")

    for row in c.fetchall():
        print("%-15s"%(row[0]),end=' ')
        print(row[1])
