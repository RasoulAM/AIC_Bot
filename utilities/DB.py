import sqlite3
import os
from utilities.Texts import *
from utilities.Queries import *

con = sqlite3.connect(db_path1, check_same_thread=False)
query = con.cursor()
# query.execute("create table states"
#               "(chat_ids int primary key, "
#               "states int)")
# query.execute("select * from Messages")
# a = query.fetchall()
# print(a)
# query.execute("delete from Messages where 1=1")
# con.commit()
# con = sqlite3.connect(db_path1, check_same_thread=False)
# query = con.cursor()
# query.execute("delete from answers where 1=1")
# query.execute("select * from Messages")
# a = query.fetchall()
# print(a)

query.execute("delete from rates where 1=1")
con.commit()
# query.execute(messages_create_table)

# query.execute("""
#                            create table rates(
#                            chat_id int,
#                            rate int)
#                            """)
#
# query.execute("""
#                             create table answers(
#                             chat_id int,
#                             answer_text text,
#                             is_read int);
#                             """)
# con.commit()