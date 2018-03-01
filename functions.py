from utilities.KeyBoards import *
from utilities.Locations import *
from utilities.states import *


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
    pass


def get_location(delegate, msg):
    delegate.sender.sendLocation(latitude=locations.get(msg["text"])[0], longitude=locations.get(msg["text"])[1])
    return False
