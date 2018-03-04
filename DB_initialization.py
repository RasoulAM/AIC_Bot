import sqlite3
from utilities.Texts import db_path

if __name__ == '__main__':
    try:
        connection = sqlite3.connect(db_path, check_same_thread=False)
        query = connection.cursor()
        query.execute("""create table states(
                        chat_ids int PRIMARY KEY,
                        first_name VARCHAR(50),
                        state int)""")
        connection.commit()
        connection = sqlite3.connect(db_path, check_same_thread=False)
        query = connection.cursor()
        query.execute("""create table Messages(
                        chat_id int,
                        first_name VARCHAR(50),
                        MessageID int,
                        Message text,
                        is_read int,
                        is_answered int)""")
        connection.commit()
        connection = sqlite3.connect(db_path, check_same_thread=False)
        query = connection.cursor()
        query.execute('' \
                               """
                               create table rates(
                               chat_id int,
                               rate int)
                               """)
        connection.commit()
        connection = sqlite3.connect(db_path, check_same_thread=False)
        query = connection.cursor()
        query.execute('' \
                        """
                        create table answers(
                        chat_id int,
                        answer_text text,
                        is_read int);
                        """)
        connection.commit()
    except:
            print("Error!")