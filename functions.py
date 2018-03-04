from utilities.KeyBoards import *
from utilities.Locations import *
from utilities.states import *
from utilities.Queries import *
from utilities.media import *


def main_menu(delegate, msg):
    # It won't work without the text!!
    delegate.sender.sendMessage(text="Main Menu!", reply_markup=main_keyboard)
    return State.MAIN


def information(delegate, msg):
    delegate.sender.sendMessage(text="اطلاعات و راهنمایی ها:", reply_markup=information_keyboard)
    return State.INFORMATION


def sharif_id(delegate, msg):
    delegate.sender.sendMessage(text="coming soon...!")
    return State.INFORMATION


def map_loader(delegate, msg):
    delegate.sender.sendMessage(text="مکان مورد نظر خود را انتخاب کنید!", reply_markup=location_keyboard)
    return State.LOCATION


def poll(delegate, msg):
    delegate.sender.sendMessage(text="نظر سنجی:", reply_markup=contact_us_keyboard)
    delegate.sender.sendMessage(text="نظر خود درباره برگزاری رویداد را انتخاب کنید!", reply_markup=polling_keyboard)

    return State.POLL


def schedule(delegate, msg):
    delegate.sender.sendMessage(text="روز مورد نظر را انتخاب کنید", reply_markup=day_selection_keyboard)
    return State.SCHEDULE


def show_schedule(delegate, msg):
    delegate.sender.sendPhoto(schedule_images[msg["text"]])
    return State.SCHEDULE


def photography_contest(delegate, msg):
    delegate.sender.sendMessage(text="Coming soon...")
    return State.MAIN


def inbox(delegate, msg):
    answers = delegate.query.execute(fetch_answers.format(delegate.chat_id)).fetchall()
    for i in answers:
        delegate.sender.sendMessage(text=i[0])
    if len(answers) == 0:
        delegate.sender.sendMessage(text="پیام جدیدی برای شما نیست !")
    delegate.query.execute(update_answer_is_read_status.format(delegate.chat_id))
    delegate.connection.commit()
    return State.MAIN


def contact_us(delegate, msg):
    delegate.sender.sendMessage(text="پیام خود را بنویسید و ارسال کنید", reply_markup=contact_us_keyboard)
    return State.CONTACT_US


def send_message_to_admin(delegate, msg):
    query_text = send_message_text.format(delegate.chat_id, msg["from"]["first_name"], msg["message_id"], msg["text"], 0, 0)
    print(query_text)
    delegate.query.execute(query_text)

    delegate.connection.commit()
    delegate.sender.sendMessage(text="پیام شما ارسال شد!", reply_markup=main_keyboard)
    return State.MAIN


def get_location(delegate, msg):
    delegate.sender.sendLocation(latitude=locations.get(msg["text"])[0], longitude=locations.get(msg["text"])[1])
    return False


def admin_panel(delegate, msg):
    if delegate.chat_id in admin_chat_id:
        delegate.sender.sendMessage(text="Access Granted!\nWelcome to the admin panel", reply_markup=admin_panel_keyboard)
        return State.ADMIN_PANEL
    else:
        delegate.sender.sendMessage(text="Unauthorized Access!")
        return State.MAIN



def show_unanswered_messages(delegate, msg):
    messages = delegate.query.execute(fetch_messages).fetchall()
    delegate.connection.commit()
    if messages is None:
        delegate.sender.sendMessage(text="No unread messages!")
        return State.ADMIN_PANEL
    else:
        delegate.sender.sendMessage('{0} says:\n{1}'.format(messages[0][1], messages[0][2]), reply_markup=admin_read_message_keyboard)
        delegate.answer_to = messages[0][0]
    answering_message = messages[0]
    # delegate.sender.sendMessage(text=answering_message[1])
    # delegate.sender.sendMessage(text="پاسخ خود را بنویسید")
    return State.ANSWER_OR_PASS


def to_answer(delegate, msg):
    delegate.sender.sendMessage("پاسخ خود را بنویسید")
    return State.ANSWERING


def answer_message(delegate, msg):
    delegate.query.execute(admin_insert_answer.format(delegate.answer_to, '\'' + msg['text'] + '\'', 0))
    delegate.connection.commit()
    delegate.query.execute(update_message_is_answered_status1.format(delegate.answer_to))
    delegate.connection.commit()
    delegate.query.execute(update_message_is_read_status.format(delegate.answer_to))
    delegate.connection.commit()
    print(delegate.answer_to)
    delegate.bott.sendMessage(chat_id=delegate.answer_to, text="پاسخی برای شما ارسال شده")
    delegate.sender.sendMessage(text="Done!", reply_markup=admin_panel_keyboard)

    return State.ADMIN_PANEL


def pass_message(delegate, msg):
    delegate.query.execute(update_message_is_read_status.format(delegate.answer_to))
    delegate.connection.commit()
    delegate.sender.sendMessage(text="پنل ادمین", reply_markup=admin_panel_keyboard)
    return State.ADMIN_PANEL


def polling(delegate, msg):
    rate = 0
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
    is_there = delegate.query.execute(check_update_or_insert_rate_query.format(delegate.chat_id)).fetchall()
    print(is_there)
    delegate.connection.commit()
    if len(is_there) == 0:
        delegate.query.execute(insert_into_rates_query.format(delegate.chat_id, rate))
    else:
        delegate.query.execute(update_rates_query.format(rate, delegate.chat_id))
    delegate.connection.commit()
    delegate.sender.sendMessage(text="با تشکر! نظر شما ثبت شد", reply_markup=main_keyboard)
    return State.MAIN


def poll_result(delegate, msg):
    result = delegate.query.execute(fetch_poll_result).fetchall()
    delegate.sender.sendMessage(text="نتیجه نظرسنجی تا این لحظه = {0}".format(result[0][0]))
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
