from utilities.KeyBoards import *
from utilities.Locations import *
from utilities.states import *
from utilities.Queries import *


def main_menu(delegate, msg):
    # It won't work without the text!!
    delegate.sender.sendMessage(text="Main Menu!", reply_markup=main_keyboard)
    return State.MAIN


def map_loader(delegate, msg):
    delegate.sender.sendMessage(text="مکان مورد نظر خود را انتخاب کنید!", reply_markup=location_keyboard)
    return State.LOCATION


def poll(delegate, msg):
    pass


def news(delegate, msg):
    pass


def schedule(delegate, msg):
    pass


def photography_contest(delegate, msg):
    pass


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
    return State.ADMIN_PANEL