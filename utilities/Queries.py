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