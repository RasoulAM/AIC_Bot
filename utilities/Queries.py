insert_state = "insert into states VALUES({0}, \'{1}\', {2})"


fetch_user = '' \
                """
                select * from states WHERE chat_ids={0}
                """

update_state =  '' \
              """
              update states set state = {0}
              where chat_ids = {1}
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
               VALUES ({0}, \'{1}\', {2}, \'{3}\', {4}, {5})
               """

fetch_messages = '' \
                 """
                 select chat_id, first_name, Message, MessageID from Messages where is_read = 0
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
                      insert into answers(chat_id, answer_text, is_read, replied_to_message_id)
                      values ({0}, \'{1}\', {2}, {3})
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
                select answer_text, replied_to_message_id from answers WHERE chat_id = {0} and is_read = 0
                """


update_answer_is_read_status = '' \
                               """
                               update answers set is_read = 1
                               where chat_id = {0}
                               """

insert_into_rates_query = '' \
                          """
                          insert into rates
                          VALUES ({0}, {1}, {2})
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
                                    where chat_id = {0} and question_id = {1}
                                    """


update_rates_query = '' \
                          """
                          update rates set rate = {0}
                          where chat_id = {1} and question_id = {2}
                          """

fetch_poll_result = '' \
                    """
                    select sum(rate) / count(*) from rates
                    group BY question_id
                    """

fetch_users = '' \
              """
              select chat_ids from states
              """


fetch_rates_num = '' \
                  """
                  select count(*) from rates
                  GROUP BY question_id
                  """

insert_photo_id = '' \
                  """
                  insert into photo_ids
                  VALUES (\'{0}\')
                  """

fetch_photo_nums = '' \
                   """
                   select * from photo_ids
                   """


insert_photo_like = '' \
                    """
                    insert into photo_contest_result
                    VALUES (\'{0}\', {1}, {2}, {3})
                    """

update_photo_like1 = '' \
                    """
                    update photo_contest_result
                    set likes = {0}
                    where photo_id = \'{1}\'
                    and chat_id = {2}
                    """

update_photo_like2 = '' \
                    """
                    update photo_contest_result
                    set dislikes = {0}
                    where photo_id = \'{1}\'
                    and chat_id = {2}
                    """


check_update_or_insert_photo_rate = '' \
                                    """
                                    select * from photo_contest_result
                                    where photo_id = \'{0}\' and chat_id = {1}
                                    """


fetch_photography_contest_likes = '' \
                    """
                    select photo_id, sum(likes) from photo_contest_result
                    group BY photo_id
                    """

fetch_photography_contest_dislikes = '' \
                    """
                    select photo_id, sum(dislikes) from photo_contest_result
                    group BY photo_id
                    """


delete_photo_query_from_result = '' \
                     """
                     delete from photo_contest_result
                     WHERE photo_id = \'{0}\'
                     """

delete_photo_query_from_photos = '' \
                                 """
                                 delete from photo_ids
                                 WHERE photo_id = \'{0}\'
                                 """