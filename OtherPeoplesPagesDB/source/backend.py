import sqlite3

def connectDatabase():
    connection = sqlite3.connect("clientInfo.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY, name text, email text, resolution text, url text, price float)")
    connection.commit()
    connection.close()

def insert(name,email,resolution,url,price):
    connection = sqlite3.connect("clientInfo.db")
    cur = connection.cursor()   
    cur.execute("INSERT INTO info VALUES (NULL,?,?,?,?,?)",(name,email,resolution,url,price)) 
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("clientInfo.db")
    cur = connection.cursor()   
    cur.execute("SELECT * FROM info") 
    rows = cur.fetchall()
    connection.close()
    return rows

def search(name="",email="",resolution="",url="",price=0.0):
    connection = sqlite3.connect("clientInfo.db")
    cur = connection.cursor()   
    cur.execute("SELECT * FROM info WHERE name=? OR email=? OR resolution=? OR url=? OR price=?",(name,email,resolution,url,price)) 
    rows = cur.fetchall()
    connection.close()   
    return rows 

def delete(id):
    connection = sqlite3.connect("clientInfo.db")
    cur = connection.cursor()   
    cur.execute("DELETE FROM info WHERE id=?",(id,)) 
    connection.commit()
    connection.close()  

def update(id,name,email,resolution,url,price):
    connection = sqlite3.connect("clientInfo.db")
    cur = connection.cursor()   
    cur.execute("UPDATE info SET name=?, email=?, resolution=?, url=?, price=? WHERE id=?",(name,email,resolution,url,price,id)) 
    connection.commit()
    connection.close()     

connectDatabase()
#insert("Billy Joel","test","test","test",19.50)
#print(view())
#print(search(name = "Billy Joel"))
#update(4,"John Doe", "jd@gmail.com","good", "web.com", 20.00)
#print(view())
