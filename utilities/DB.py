import sqlite3
import os
from utilities.Texts import *

con = sqlite3.connect(db_path, check_same_thread=False)
query = con.cursor()
# query.execute("create table states"
#               "(chat_ids int primary key, "
#               "states int)")
a = query.execute("select * from states").fetchall()
print(a)
con.commit()