import sqlite3
import os


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()
query.execute("delete from Messages where 1=1")
con.commit()


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()

query.execute("delete from answers where 1=1")
con.commit()


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()

query.execute("delete from states where 1=1")
con.commit()


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()

query.execute("delete from rates where 1=1")
con.commit()
