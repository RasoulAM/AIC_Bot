import sqlite3
import os

con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()
# query.execute("create table states"
#               "(chat_ids int primary key, "
#               "states int)")
# query.execute("drop table answers")

# a = query.fetchall()
# print(a)
# query.execute("delete from Messages where 1=1")
# con.commit()
# con = sqlite3.connect(db_path1, check_same_thread=False)
# query = con.cursor()
# query.execute("delete from answers where 1=1")
query.execute("drop table Messages")
# a = query.fetchall()
# print(a)

# query.execute("delete from rates where 1=1")
con.commit()
con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()
query.execute("""create table Messages(
                        chat_id int,
                        first_name VARCHAR(50),
                        MessageID int,
                        Message text,
                        is_read int,
                        is_answered int)""")
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
con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()
query.execute("""drop table states""")
con.commit()
con = sqlite3.connect(os.getcwd() + '/database.db', check_same_thread=False)
query = con.cursor()
query.execute("""create table states(
                        chat_ids int PRIMARY KEY,
                        first_name VARCHAR(50),
                        state int)""")
con.commit()


