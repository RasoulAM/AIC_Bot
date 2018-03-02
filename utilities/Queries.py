insert_state = "insert into states VALUES("


fetch_user = '' \
                """
                select * from states WHERE chat_ids=
                """

update_state1= '' \
              """
              update states set states = 
              """

update_state2 = '' \
                """
                where chat_ids = 
                """

messages_create_table = '' \
               """
               create table Messages(
                    chat_id int,
                    Message text,
                    is_read int,
                    is_answered int)
               """


send_message_text = '' \
               """
               insert into Messages
               VALUES (
               """

fetch_messages = '' \
                 """
                 select chat_id, Message from Messages where is_read = 0
                 """

create_answer_table_query = '' \
                            """
                            create table answers(
                            chat_id int,
                            answer_text text,
                            is_read int);
                            """

admin_insert_answer = '' \
                      """
                      insert into answers
                      values ({0}, {1}, 0)
                      """