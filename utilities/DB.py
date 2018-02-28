import sqlite3
import os
from utilities.Texts import *

con = sqlite3.connect(db_path1, check_same_thread=False)
query = con.cursor()
# query.execute("create table states"
#               "(chat_ids int primary key, "
#               "states int)")
# query.execute("select * from states")
# a = query.fetchall()
# print(a)
query.execute("delete from states where 1=1")
con.commit()