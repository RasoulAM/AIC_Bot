from enum import Enum

from functions import *
from utilities.Emojies_table import emojies
from utilities.states import State, Action

state_texts_mapping = {
    State.ADMIN_PANEL: "پنل ادمین",

    State.ANSWER_OR_PASS: "خواندن پیامها",

    State.ANSWERING: "answer",
    State.PASS: "pass",


    State.LOCATION: "مکانها" + emojies.get('location'),
    State.POLL: "نظرسنجی" + emojies.get('clipboard'),
    State.SCHEDULE: "برنامه زمان بندی" + emojies.get('calender'),
    State.NEWS: "اطلاعات و اخبار" + emojies.get('information'),
    State.PHOTOGRAPHY_CONTEST: "مسابقه عکس " + emojies.get('camera'),
    State.CONTACT_US: "ارتباط با ما",
    State.INBOX: "صندوق پیام",

    State.LOCATION_LUNCH: "غذاخوری" + emojies.get('dining_hall'),
    State.LOCATION_JABER: "سالن جابر",
    State.LOCATION_CE_DP: "دانشکده کامپیوتر",



}

action_texts_mapping = {
    Action.RETURN: "بازگشت"
}

dispatchers = {

    State.MAIN: main_menu,

    # main menu
    State.LOCATION: map_loader,
    State.POLL: poll,
    State.SCHEDULE: schedule,
    State.NEWS: news,
    State.PHOTOGRAPHY_CONTEST: photography_contest,

    # State.LOCATION_JABER: location_jaber,
    # State.LOCATION_LUNCH: location_lunch,
    # State.LOCATION_CE_DP: location_ce_dp,

}


def dispatch(delegate, msg):
    if "data" in msg.keys():
        print(msg["data"])
        new_state = transitions.get((delegate.state, msg["data"]))(delegate, msg)
        if new_state:
            delegate.state = new_state
    elif "text" in msg.keys():
        if transitions.get((delegate.state, msg["text"])) is None and transitions.get((delegate.state, None)) is None:
            return
        elif transitions.get((delegate.state, msg["text"])) is None and transitions.get((delegate.state, None)) is not None:
            print(delegate.state)
            new_state = transitions.get((delegate.state, None))(delegate, msg)
            print(new_state)

        else:
            new_state = transitions.get((delegate.state, msg["text"]))(delegate, msg)
        if new_state:
            delegate.state = new_state


transitions = {

    # main transitions
    (State.MAIN, state_texts_mapping.get(State.LOCATION)): map_loader,
    (State.MAIN, state_texts_mapping.get(State.POLL)): poll,
    (State.MAIN, state_texts_mapping.get(State.SCHEDULE)): schedule,
    (State.MAIN, state_texts_mapping.get(State.NEWS)): news,
    (State.MAIN, state_texts_mapping.get(State.PHOTOGRAPHY_CONTEST)): photography_contest,
    (State.MAIN, state_texts_mapping.get(State.INBOX)): inbox,
    (State.MAIN, state_texts_mapping.get(State.CONTACT_US)): contact_us,

    # main transitions for admin
    (State.MAIN, "abrakadabra"): admin_panel,

    # admin panel transitions
    (State.ADMIN_PANEL, action_texts_mapping.get(Action.RETURN)): main_menu,
    (State.ADMIN_PANEL, state_texts_mapping.get(State.ANSWER_OR_PASS)): show_unanswered_messages,

    # (State.ANSWER_MESSAGES, ""): show_unanswered_messages,
    (State.ANSWER_OR_PASS, action_texts_mapping.get(Action.RETURN)): admin_panel,
    (State.ANSWER_OR_PASS, state_texts_mapping.get(State.ANSWERING)): to_answer,
    (State.ANSWER_OR_PASS, state_texts_mapping.get(State.PASS)): pass_message,
    (State.ANSWERING, None): answer_message,
    (State.ANSWERING, action_texts_mapping.get(Action.RETURN)): main_menu,

    # Location transitions
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_JABER)): get_location,
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_CE_DP)): get_location,
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_LUNCH)): get_location,
    (State.LOCATION, action_texts_mapping.get(Action.RETURN)): main_menu,

    (State.CONTACT_US, None): send_message_to_admin,
    (State.CONTACT_US, action_texts_mapping.get(Action.RETURN)): main_menu,

    # Schedule state
    (State.SCHEDULE, None): show_schedule,
    (State.SCHEDULE, action_texts_mapping.get(Action.RETURN)): main_menu,

}
