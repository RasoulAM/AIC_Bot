import sqlite3
import os


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()
query.execute("drop table Messages")
con.commit()


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()

query.execute("drop table answers")
con.commit()


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()

query.execute("drop table states")
con.commit()


con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()

query.execute("drop table rates")
con.commit()
