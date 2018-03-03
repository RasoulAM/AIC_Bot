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
                      insert into answers(chat_id, answer_text, is_read)
                      values ({0}, {1}, {2})
                      """

update_message_is_answered_status1 = '' \
                        """
                        update Messages set is_answered = 1
                        WHERE chat_id = {0}
                        """

update_message_is_read_status = '' \
                         """
                         update Messages set is_read = 1
                         WHERE chat_id = {0}
                         """

fetch_answers = '' \
                """
                select answer_text from answers WHERE chat_id = {0} and is_read = 0
                """


update_answer_is_read_status = '' \
                               """
                               update answers set is_read = 1
                               where chat_id = {0}
                               """

insert_into_rates_query = '' \
                          """
                          insert into rates
                          VALUES ({0}, {1})
                          """


create_rates_table_query = '' \
                           """
                           create table rates(
                           chat_id int,
                           rate int)
                           """

check_update_or_insert_rate_query = '' \
                                    """
                                    select chat_id from rates
                                    where chat_id = {0}
                                    """


update_rates_query = '' \
                          """
                          update rates set rate = {0}
                          where chat_id = {1}
                          """

fetch_poll_result = '' \
                    """
                    select sum(rate) / count(*) from rates
                    """

