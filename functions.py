from utilities.KeyBoards import *
from utilities.Locations import *


def main_menu(delegate, msg):
    # It won't work without the text!!
    delegate.sender.sendMessage(text="Main Menu!", reply_markup=main_keyboard)


def map_loader(delegate, msg):
    delegate.sender.sendMessage(text="مکان مورد نظر خود را انتخاب کنید!", reply_markup=location_keyboard)
    # delegate.state = stateEnum.locations


def poll(delegate, msg):
    pass


def news(delegate, msg):
    pass


def schedule(delegate, msg):
    pass


def photography_contest(delegate, msg):
    pass


def location_jaber(delegate, msg):
    delegate.sender.sendLocation(latitude=locations.get(msg["text"])[0], longitude=locations.get(msg["text"])[1])


def location_ce_dp(delegate, msg):
    pass


def location_lunch(delegate, msg):
    pass
