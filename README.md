# mysqlwithpython
you will find the source code to establish the connection between mysql and python and modify the database
import sqlite3 as sql
base=sql.connect(&#39;Python.db&#39;)
c=base.cursor()

def create_item():
c.execute(&quot;CREATE TABLE IF NOT EXISTS Item(Itemno INT,Iname
TEXT,Price INT,Quantity INT)&quot;)
base.commit()

def insert_values():
c.execute(&quot;INSERT INTO Item VALUES(101,&#39;Geometry Box&#39;,50,100)&quot;)
c.execute(&quot;INSERT INTO Item VALUES(102,&#39;Soap&#39;,100,50)&quot;)
c.execute(&quot;INSERT INTO Item VALUES(103,&#39;Perfume&#39;,150,25)&quot;)
c.execute(&quot;INSERT INTO Item VALUES(104,&#39;Pen&#39;,50,200)&quot;)
c.execute(&quot;INSERT INTO Item VALUES(105,&#39;Pencil&#39;,20,100)&quot;)
base.commit()

#a)Display all items information
def display_table():
print(&quot;a)Display all items information&quot;)
print(&quot;\n&quot;)
c.execute(&quot;Select * from Item&quot;)
print(&quot;%-10s&quot;%(&quot;Itemno&quot;),&quot;%-15s&quot;%(&quot;Iname&quot;),&quot;%-
15s&quot;%(&quot;Price&quot;),&quot;Quantity&quot;)
for row in c.fetchall():
print(&quot;%-10s&quot;%(row[0]),end=&#39; &#39;)
print(&quot;%-15s&quot;%(row[1]),end=&#39; &#39;)

print(&quot;%-15s&quot;%(row[2]),end=&#39; &#39;)
print(row[3])

create_item()
