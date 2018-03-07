from utilities.KeyBoards import *
from utilities.Locations import *
from utilities.states import *
from utilities.Queries import *
from utilities.media import *
from utilities.Texts import *


def main_menu(delegate, msg):
    # It won't work without the text!!
    delegate.sender.sendMessage(text="Main Menu!", reply_markup=main_keyboard)
    delegate.photonum = 0
    delegate.question_id = 0
    return State.MAIN


def information(delegate, msg):
    delegate.sender.sendMessage(text="اطلاعات و راهنمایی ها:", reply_markup=information_keyboard)
    return State.INFORMATION


def sharif_id_manual(delegate, msg):
    delegate.sender.sendDocument(sharif_id_file[msg["text"]])


def sharif_id(delegate, msg):
    delegate.sender.sendMessage(text="پلتفرم مورد نظر خود را انتخاب کنید", reply_markup=platform_keyboard)
    return State.PLATFORM_SHARIF_ID


def map_loader(delegate, msg):
    delegate.sender.sendMessage(text="مکان مورد نظر خود را انتخاب کنید!", reply_markup=location_keyboard)
    return State.LOCATION


def poll(delegate, msg):
    delegate.question_id = 0
    delegate.sender.sendMessage(text="نظر سنجی:", reply_markup=contact_us_keyboard)
    delegate.sender.sendMessage(text=questions[delegate.question_id], reply_markup=polling_keyboard)
    delegate.question_id += 1
    return State.POLL


def schedule(delegate, msg):
    delegate.sender.sendMessage(text="روز مورد نظر را انتخاب کنید", reply_markup=day_selection_keyboard)
    return State.SCHEDULE


def show_schedule(delegate, msg):
    delegate.sender.sendPhoto(schedule_images[msg["text"]])
    return State.SCHEDULE


def photography_contest(delegate, msg):
    photos = delegate.query.execute(fetch_photo_nums).fetchall()
    delegate.photonum = 0
    if len(photos) == 0:
        delegate.sender.sendMessage("به زودی...!")
        return State.MAIN
    else:
        delegate.sender.sendMessage(text="مسابقه عکس:", reply_markup=only_return_keyboard)
        delegate.sender.sendPhoto(photo=photos[delegate.photonum][0], reply_markup=like_dislike_keyboard)
    return State.PHOTOGRAPHY_CONTEST


def photography_contesting(delegate, msg):
    photos = delegate.query.execute(fetch_photo_nums).fetchall()
    if delegate.photonum >= len(photos) - 1:
        if msg["data"] == "like":
            is_there = delegate.query.execute(check_update_or_insert_photo_rate.format(photos[delegate.photonum][0], delegate.chat_id)).fetchall()
            if len(is_there) == 0:
                delegate.query.execute(insert_photo_like.format(photos[delegate.photonum][0], 1, 0, delegate.chat_id))
            else:
                delegate.query.execute(update_photo_like1.format(1, photos[delegate.photonum][0], delegate.chat_id))
                delegate.query.execute(update_photo_like2.format(0, photos[delegate.photonum][0], delegate.chat_id))
        elif msg["data"] == "dislike":
            is_there = delegate.query.execute(
                check_update_or_insert_photo_rate.format(photos[delegate.photonum][0], delegate.chat_id)).fetchall()
            if len(is_there) == 0:
                delegate.query.execute(insert_photo_like.format(photos[delegate.photonum][0], 0, 1, delegate.chat_id))
            else:
                delegate.query.execute(update_photo_like1.format(0, photos[delegate.photonum][0], delegate.chat_id))
                delegate.query.execute(update_photo_like2.format(1, photos[delegate.photonum][0], delegate.chat_id))
        delegate.connection.commit()
        delegate.photonum += 1
        delegate.sender.sendMessage(text="با تشکر نظر شما ثبت شد.", reply_markup=main_keyboard)
        return State.MAIN
    elif delegate.photonum < len(photos) - 1:
        if msg["data"] == "like":
            is_there = delegate.query.execute(check_update_or_insert_photo_rate.format(photos[delegate.photonum][0], delegate.chat_id)).fetchall()
            if len(is_there) == 0:
                delegate.query.execute(insert_photo_like.format(photos[delegate.photonum][0], 1, 0, delegate.chat_id))
            else:
                delegate.query.execute(update_photo_like1.format(1, photos[delegate.photonum][0], delegate.chat_id))
                delegate.query.execute(update_photo_like2.format(0, photos[delegate.photonum][0], delegate.chat_id))
        elif msg["data"] == "dislike":
            is_there = delegate.query.execute(
                check_update_or_insert_photo_rate.format(photos[delegate.photonum][0], delegate.chat_id)).fetchall()
            if len(is_there) == 0:
                delegate.query.execute(insert_photo_like.format(photos[delegate.photonum][0], 0, 1, delegate.chat_id))
            else:
                delegate.query.execute(update_photo_like1.format(0, photos[delegate.photonum][0], delegate.chat_id))
                delegate.query.execute(update_photo_like2.format(1, photos[delegate.photonum][0], delegate.chat_id))
        delegate.connection.commit()
        delegate.photonum += 1
        # delegate.helper.
        delegate.sender.sendMessage(text="عکس {0}:".format(delegate.photonum + 1), reply_markup=only_return_keyboard)
        delegate.sender.sendPhoto(photo=photos[delegate.photonum][0], reply_markup=like_dislike_keyboard)
        return State.PHOTOGRAPHY_CONTEST


def inbox(delegate, msg):
    answers = delegate.query.execute(fetch_answers.format(delegate.chat_id)).fetchall()
    for answer in answers:
        delegate.sender.sendMessage(text=answer[0], reply_to_message_id=answer[1])
    if len(answers) == 0:
        delegate.sender.sendMessage(text="پیام جدیدی برای شما نیست !")
    delegate.query.execute(update_answer_is_read_status.format(delegate.chat_id))
    delegate.connection.commit()
    return State.MAIN


def contact_us(delegate, msg):
    delegate.sender.sendMessage(text="پیام خود را بنویسید و ارسال کنید", reply_markup=contact_us_keyboard)
    return State.CONTACT_US

def online_results(delegate, msg):
    delegate.sender.sendMessage(text="به زودی...")
    return State.MAIN


def send_message_to_admin(delegate, msg):
    query_text = send_message_text.format(delegate.chat_id, msg["from"]["first_name"], msg["message_id"], msg["text"],
                                          0, 0)
    delegate.query.execute(query_text)

    delegate.connection.commit()
    delegate.sender.sendMessage(text="پیام شما ارسال شد!", reply_markup=main_keyboard)
    return State.MAIN


def get_location(delegate, msg):
    delegate.sender.sendLocation(latitude=locations.get(msg["text"])[0], longitude=locations.get(msg["text"])[1])


def admin_panel(delegate, msg):
    if delegate.chat_id in admin_chat_id:
        delegate.sender.sendMessage(text="Access Granted!\nWelcome to the admin panel",
                                    reply_markup=admin_panel_keyboard)
        return State.ADMIN_PANEL
    else:
        delegate.sender.sendMessage(text="Unauthorized Access!")
        return State.MAIN


def show_unanswered_messages(delegate, msg):
    messages = delegate.query.execute(fetch_messages).fetchall()
    delegate.connection.commit()
    if len(messages) == 0:
        delegate.sender.sendMessage(text="پیام خوانده نشده وجود ندارد!")
        return State.ADMIN_PANEL
    else:
        delegate.sender.sendMessage(text="پیام خوانده نشده:", reply_markup=only_return_keyboard)
        delegate.sender.sendMessage('{0} says:\n{1}'.format(messages[0][1], messages[0][2]),
                                    reply_markup=admin_read_message_keyboard)
        delegate.answer_to = messages[0][0]
        delegate.message_id_replied = messages[0][3]
    answering_message = messages[0]
    return State.ANSWER_OR_PASS


def to_answer(delegate, msg):
    delegate.sender.sendMessage("پاسخ خود را بنویسید")
    return State.ANSWERING


def answer_message(delegate, msg):
    delegate.query.execute(
        admin_insert_answer.format(delegate.answer_to, msg['text'], 0, delegate.message_id_replied))
    delegate.connection.commit()
    delegate.query.execute(update_message_is_answered_status1.format(delegate.answer_to))
    delegate.connection.commit()
    delegate.query.execute(update_message_is_read_status.format(delegate.answer_to))
    delegate.connection.commit()
    delegate.bott.sendMessage(chat_id=delegate.answer_to, text="پاسخی برای شما ارسال شده")
    delegate.sender.sendMessage(text="Done!", reply_markup=admin_panel_keyboard)
    return State.ADMIN_PANEL


def pass_message(delegate, msg):
    delegate.query.execute(update_message_is_read_status.format(delegate.answer_to))
    delegate.connection.commit()
    delegate.sender.sendMessage(text="پنل ادمین", reply_markup=admin_panel_keyboard)
    return State.ADMIN_PANEL


def polling(delegate, msg):
    if delegate.question_id > 7:
        if msg["data"] == "very happy":
            rate = 5
        elif msg["data"] == "happy":
            rate = 4
        elif msg["data"] == "poker":
            rate = 3
        elif msg["data"] == "angry":
            rate = 2
        elif msg["data"] == "very angry":
            rate = 1
        is_there = delegate.query.execute(check_update_or_insert_rate_query.format(delegate.chat_id, delegate.question_id)).fetchall()
        delegate.connection.commit()
        if len(is_there) == 0:
            delegate.query.execute(insert_into_rates_query.format(delegate.chat_id, rate, delegate.question_id))
        else:
            delegate.query.execute(update_rates_query.format(rate, delegate.chat_id, delegate.question_id))
        delegate.connection.commit()
        delegate.sender.sendMessage(text="با تشکر! نظر شما ثبت شد", reply_markup=main_keyboard)
        return State.MAIN
    else:
        if msg["data"] == "very happy":
            rate = 5
        elif msg["data"] == "happy":
            rate = 4
        elif msg["data"] == "poker":
            rate = 3
        elif msg["data"] == "angry":
            rate = 2
        elif msg["data"] == "very angry":
            rate = 1
        is_there = delegate.query.execute(check_update_or_insert_rate_query.format(delegate.chat_id, delegate.question_id)).fetchall()
        delegate.connection.commit()
        if len(is_there) == 0:
            delegate.query.execute(insert_into_rates_query.format(delegate.chat_id, rate, delegate.question_id))
        else:
            delegate.query.execute(update_rates_query.format(rate, delegate.chat_id, delegate.question_id))
        delegate.connection.commit()
        delegate.sender.sendMessage(text=questions[delegate.question_id], reply_markup=polling_keyboard)
        delegate.question_id += 1
        return State.POLL


def poll_result(delegate, msg):
    result = delegate.query.execute(fetch_poll_result).fetchall()
    count = delegate.query.execute(fetch_rates_num).fetchall()
    delegate.sender.sendMessage(text=poll_result_text.format(result[0][0], count[0][0],
                                                             result[1][0], count[1][0],
                                                             result[2][0], count[2][0],
                                                             result[3][0], count[3][0],
                                                             result[4][0], count[4][0],
                                                             result[5][0], count[5][0],
                                                             result[6][0], count[6][0],
                                                             result[7][0], count[7][0],
                                                             # result[8][0], count[8][0],
                                                             # result[9][0], count[9][0],
                                                             ))
    return State.ADMIN_PANEL


def announcement(delegate, msg):
    delegate.sender.sendMessage(text="متن اطلاعیه را بنویسید وارسال کنید.")
    return State.ANNOUNCEMENT


def announcing(delegate, msg):
    users = delegate.query.execute(fetch_users).fetchall()
    delegate.connection.commit()
    for i in users:
        delegate.bott.sendMessage(chat_id=i[0], text=msg["text"])
    return State.ADMIN_PANEL


def add_photo(delegate, msg):
    delegate.sender.sendMessage(text="عکس مورد نظر را بفرستید!", reply_markup=only_return_keyboard)
    return State.ADDING_PHOTO


def adding_photo(delegate, msg):
    delegate.query.execute(insert_photo_id.format(msg["photo"][0]["file_id"]))
    delegate.connection.commit()
    delegate.sender.sendMessage("عکس با موفقیت اضافه شد!", reply_markup=admin_panel_keyboard)
    return State.ADMIN_PANEL


def photography_contest_result(delegate, msg):
    likes_result = delegate.query.execute(fetch_photography_contest_likes).fetchall()
    dislikes_result = delegate.query.execute(fetch_photography_contest_dislikes).fetchall()
    delegate.connection.commit()
    for i in range(len(likes_result)):
        text = result_text2.format(likes_result[i][1], dislikes_result[i][1])
        delegate.sender.sendPhoto(caption=text, photo=likes_result[i][0])
    return State.ADMIN_PANEL


def delete_photo(delegate, msg):
    delegate.sender.sendMessage(text="عکس مورد نظر را اینجا فوروارد کنید تا حذف شود:")
    return State.DELETING_PHOTO


def deleting_photo(delegate, msg):
    try:
        delegate.query.execute(delete_photo_query_from_result.format(msg["photo"][0]["file_id"]))
        delegate.query.execute(delete_photo_query_from_photos.format(msg["photo"][0]["file_id"]))
        delegate.connection.commit()
        delegate.sender.sendMessage(text="عکس مورد نظر با موفقیت حذف شد!")
    except:
        delegate.sender.sendMessage(text="عکس مورد نظر وجود ندارد!")
    finally:
        return State.ADMIN_PANEL
