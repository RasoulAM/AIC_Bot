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


def photography_contest(delegate, msg):
    delegate.sender.sendMessage(text="Coming soon...")


def inbox(delegate, msg):
    pass


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
    answering_message = messages[0]
    # delegate.sender.sendMessage(text=answering_message[1])
    # delegate.sender.sendMessage(text="پاسخ خود را بنویسید")
    return State.ANSWER_MESSAGES


def answer_message(delegate, msg):
    messages = delegate.query.execute(fetch_messages).fetchall()
    delegate.connection.commit()
    answering_message_chat_id = messages[0][0]

    delegate.sender.sendMessage(text="Your answer will be written in the database...")

    return State.ADMIN_PANEL
