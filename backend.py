import sqlite3
import os.path

datafile = 'shopdata.db'
datadir = os.path.dirname(__file__)
datafile = os.path.join(datadir, 'shopdata.db') 
conn = sqlite3.connect(datafile)
c = conn.cursor()

def connect():
    conn = sqlite3.connect(datafile)
    c = conn.cursor()
    c.execute("CREATE TABLE  book(id INTEGER PRIMARYKEY,title text,author text,year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
c.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year INTEGER, isbn INTEGER)")
    
    
def insert(title,author,year,isbn):
    conn = sqlite3.connect("shopdata.db")
    c = conn.cursor()
    c.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    

def view():
    conn=sqlite3.connect("shopdata.db")
    c = conn.cursor()
    c.execute("SELECT * FROM book")
    row = c.fetchall()
    conn.close()
    return row


def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("shpdata.db")
    c = conn.cursor()
    c.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or Isbn=?",(title,author,year,isbn))
    rows = c.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("shopdata.db")
    c = conn.cursor()
    c.execute("DELETE FROM book WHERE id?",(id,))
    conn.commite()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("shopdata.db")
    c = conn.cursor()
    c.execute("UPDATE book SET title=?,author=?,year=?,isbn=?,id=?",(title,author,year,isbn,id))
    conn.commite()
    conn.close()