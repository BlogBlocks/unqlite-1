import sqlite3
conn = sqlite3.connect("snippet.db")
c = conn.cursor()
SEARCH = raw_input("SEARCH : ")
for row in c.execute("SELECT rowid,* FROM snippet WHERE snippet MATCH ?",(SEARCH,)):
    print row[2]