from enum import Enum

from functions import *
from utilities.Emojies_table import emojies
from utilities.states import State

admin_main_menu_texts = {
    State.ADMIN_PANEL: "پنل ادمین",
    State.LOCATION: "مکانها" + emojies.get('location'),
    State.POLL: "نظرسنجی" + emojies.get('clipboard'),
    State.SCHEDULE: "برنامه زمان بندی" + emojies.get('calender'),
    State.NEWS: "اطلاعات و اخبار" + emojies.get('information'),
    State.PHOTOGRAPHY_CONTEST: "مسابقه عکس " + emojies.get('camera'),
    State.CONTACT_US: "ارتباط با ما",
    State.INBOX: "صندوق پیام",

}

main_menu_texts_mapping = {
    State.LOCATION: "مکانها" + emojies.get('location'),
    State.POLL: "نظرسنجی" + emojies.get('clipboard'),
    State.SCHEDULE: "برنامه زمان بندی" + emojies.get('calender'),
    State.NEWS: "اطلاعات و اخبار" + emojies.get('information'),
    State.PHOTOGRAPHY_CONTEST: "مسابقه عکس " + emojies.get('camera'),
    State.CONTACT_US: "ارتباط با ما",
    State.INBOX: "صندوق پیام",

}

locations_buttons_texts_mapping = {
    State.LOCATION_LUNCH: "غذاخوری" + emojies.get('dining_hall'),
    State.LOCATION_JABER: "سالن جابر",
    State.LOCATION_CE_DP: "دانشکده کامپیوتر"

}

dispatchers = {

    State.MAIN: main_menu,

    # main menu
    State.LOCATION: map_loader,
    State.POLL: poll,
    State.SCHEDULE: schedule,
    State.NEWS: news,
    State.PHOTOGRAPHY_CONTEST: photography_contest,

    State.LOCATION_JABER: location_jaber,
    State.LOCATION_LUNCH: location_lunch,
    State.LOCATION_CE_DP: location_ce_dp,




}


def dispatch(delegate, msg):
    new_state = _transition(delegate.state, msg["text"])
    if new_state: #transition
        delegate.state = new_state
        if dispatchers[delegate.state]:
            dispatchers[delegate.state](delegate, msg)
    else:
        delegate.sender.sendMessage(text="Going to None state!!")


transitions = {

    # main transitions
    (State.MAIN, main_menu_texts_mapping.get(State.LOCATION)): State.LOCATION,
    (State.MAIN, main_menu_texts_mapping.get(State.POLL)): State.POLL,
    (State.MAIN, main_menu_texts_mapping.get(State.SCHEDULE)): State.SCHEDULE,
    (State.MAIN, main_menu_texts_mapping.get(State.NEWS)): State.NEWS,
    (State.MAIN, main_menu_texts_mapping.get(State.PHOTOGRAPHY_CONTEST)): State.PHOTOGRAPHY_CONTEST,
    (State.MAIN, main_menu_texts_mapping.get(State.INBOX)): State.INBOX,
    (State.MAIN, main_menu_texts_mapping.get(State.LOCATION)): State.LOCATION,
    (State.MAIN, main_menu_texts_mapping.get(State.CONTACT_US)): State.CONTACT_US,

    # Location transitions
    (State.LOCATION, main_menu_texts_mapping.get(State.LOCATION_JABER)): State.LOCATION_JABER,
    (State.LOCATION, main_menu_texts_mapping.get(State.LOCATION_CE_DP)): State.LOCATION_CE_DP,
    (State.LOCATION, main_menu_texts_mapping.get(State.LOCATION_LUNCH)): State.LOCATION_LUNCH,
    (State.LOCATION, "بازگشت"): State.MAIN,

    #

}


def _transition(current_state, input):
    print(current_state)
    print(input)
    print(transitions.get((State.MAIN, input)))
    print(main_menu_texts_mapping.get(State.LOCATION))
    return transitions.get((current_state, input))
