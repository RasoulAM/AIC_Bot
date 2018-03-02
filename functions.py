from utilities.KeyBoards import *
from utilities.Locations import *
from utilities.states import *
from utilities.Queries import *
from utilities.media import *


def main_menu(delegate, msg):
    # It won't work without the text!!
    delegate.sender.sendMessage(text="Main Menu!", reply_markup=main_keyboard)
    return State.MAIN


def map_loader(delegate, msg):
    delegate.sender.sendMessage(text="مکان مورد نظر خود را انتخاب کنید!", reply_markup=location_keyboard)
    return State.LOCATION


def poll(delegate, msg):
    delegate.sender.sendMessage(text="Coming soon...")


def news(delegate, msg):
    delegate.sender.sendMessage(text="Coming soon...")


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
    query_text = send_message_text + str(delegate.chat_id) + ',\'' + msg["text"] + '\',' + str(0) + ',' + str(0) + ")"
    print(query_text)
    delegate.query.execute(query_text)

    delegate.connection.commit()
    delegate.sender.sendMessage(text="پیام شما ارسال شد!", reply_markup=main_keyboard)
    return State.MAIN


def get_location(delegate, msg):
    delegate.sender.sendLocation(latitude=locations.get(msg["text"])[0], longitude=locations.get(msg["text"])[1])
    return False


def admin_panel(delegate, msg):
    delegate.sender.sendMessage(text="Welcome to the admin panel!", reply_markup=admin_panel_keyboard)
    return State.ADMIN_PANEL


def show_unanswered_messages(delegate, msg):
    messages = delegate.query.execute(fetch_messages).fetchall()
    delegate.connection.commit()
    if messages is None:
        delegate.sender.sendMessage(text="No unread messages!")
        return State.ADMIN_PANEL
    else:
        delegate.sender.sendMessage('{0}'.format(messages[0][1]), reply_markup=admin_read_message_keyboard)
        delegate.answer_to = messages[0][0]
    answering_message = messages[0]
    # delegate.sender.sendMessage(text=answering_message[1])
    # delegate.sender.sendMessage(text="پاسخ خود را بنویسید")
    return State.ANSWER_OR_PASS


def to_answer(delegate, msg):
    delegate.sender.sendMessage("پاسخ خود را بنویسید")
    return State.ANSWERING


def answer_message(delegate, msg):
    # print(admin_insert_answer.format(delegate.answer_to, '\'' + msg['text'] + '\'', 0))
    delegate.query.execute(admin_insert_answer.format(delegate.answer_to, '\'' + msg['text'] + '\'', 0))
    # delegate.query.execute("insert into answers values(123, 'سلام', 0)")
    delegate.connection.commit()
    delegate.query.execute(update_message_is_answered_status1.format(delegate.answer_to))
    delegate.connection.commit()
    delegate.query.execute(update_message_is_read_status.format(delegate.answer_to))
    delegate.connection.commit()
    print(delegate.answer_to)
    delegate.bott.sendMessage(chat_id=delegate.answer_to, text="پاسخی برای شما ارسال شده")
    delegate.sender.sendMessage(text="Your answer will be written in the database...", reply_markup=admin_panel_keyboard)

    return State.ADMIN_PANEL


def pass_message(delegate, msg):
    delegate.query.execute(update_message_is_read_status.format(delegate.answer_to))
    delegate.connection.commit()
    delegate.sender.sendMessage(text="پنل ادمین", reply_markup=admin_panel_keyboard)
    return State.ADMIN_PANEL