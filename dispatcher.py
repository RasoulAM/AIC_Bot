from enum import Enum

from functions import *
from utilities.Emojies_table import emojies
from utilities.states import State, Action

state_texts_mapping = {
    State.ADMIN_PANEL: "پنل ادمین",

    State.ANSWER_OR_PASS: "خواندن پیامها",
    State.POLL_RESULT: "نتیجه نظر سنجی",
    State.ANNOUNCEMENT: "ارسال اطلاعیه",

    State.ANSWERING: "answer",
    State.PASS: "pass",


    State.POLL_very_happy: "very happy",
    State.POLL_happy: "happy",
    State.POLL_very_angry: "very angry",
    State.POLL_angry: "angry",
    State.POLL_poker: "poker",




    State.POLL: "نظرسنجی" + emojies.get('clipboard'),
    State.INFORMATION: "اطلاعات و راهنمایی ها" + emojies.get('information'),
    State.PHOTOGRAPHY_CONTEST: "مسابقه عکس " + emojies.get('camera'),
    State.CONTACT_US: "ارتباط با ما",
    State.INBOX: "صندوق پیام",
    State.ONLINE_RESULT: "نتایج آنلاین",

    State.SCHEDULE: "برنامه زمان بندی" + emojies.get('calender'),
    State.LOCATION: "مکانها" + emojies.get('location'),
    State.SHARIF_ID: "راهنمای اتصال به VPN شریف",

    State.LOCATION_LUNCH: "غذاخوری" + emojies.get('dining_hall'),
    State.LOCATION_JABER: "سالن جابر",
    State.LOCATION_CE_DP: "دانشکده کامپیوتر",
    State.LOCATION_MOSQUE: "مسجد",
    State.LOCATION_THEATER: "آمفی تئاتر مرکزی",



}

action_texts_mapping = {
    Action.RETURN: "بازگشت"
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
    (State.MAIN, state_texts_mapping.get(State.INFORMATION)): information,
    (State.MAIN, state_texts_mapping.get(State.POLL)): poll,
    (State.MAIN, state_texts_mapping.get(State.PHOTOGRAPHY_CONTEST)): photography_contest,
    (State.MAIN, state_texts_mapping.get(State.INBOX)): inbox,
    (State.MAIN, state_texts_mapping.get(State.CONTACT_US)): contact_us,


    # main transitions for admin
    (State.MAIN, "admin"): admin_panel,

    # admin panel transitions
    (State.ADMIN_PANEL, action_texts_mapping.get(Action.RETURN)): main_menu,
    (State.ADMIN_PANEL, state_texts_mapping.get(State.ANSWER_OR_PASS)): show_unanswered_messages,
    (State.ADMIN_PANEL, state_texts_mapping.get(State.POLL_RESULT)): poll_result,
    (State.ADMIN_PANEL, state_texts_mapping.get(State.ANNOUNCEMENT)): announcement,

    # admin announcement
    (State.ANNOUNCEMENT, None): announcing,
    (State.ANNOUNCEMENT, action_texts_mapping.get(Action.RETURN)):admin_panel,


    # (State.ANSWER_MESSAGES, ""): show_unanswered_messages,
    (State.ANSWER_OR_PASS, action_texts_mapping.get(Action.RETURN)): admin_panel,
    (State.ANSWER_OR_PASS, state_texts_mapping.get(State.ANSWERING)): to_answer,
    (State.ANSWER_OR_PASS, state_texts_mapping.get(State.PASS)): pass_message,
    (State.ANSWERING, None): answer_message,
    (State.ANSWERING, action_texts_mapping.get(Action.RETURN)): main_menu,

    # information transitions
    (State.INFORMATION, state_texts_mapping.get(State.LOCATION)): map_loader,
    (State.INFORMATION, state_texts_mapping.get(State.SHARIF_ID)): sharif_id,
    (State.INFORMATION, state_texts_mapping.get(State.SCHEDULE)): schedule,
    (State.INFORMATION, action_texts_mapping.get(Action.RETURN)): information,

    (State.PLATFORM_SHARIF_ID, state_texts_mapping.get(State.PLATFORM_ANDROID)): sharif_id_manual,
    (State.PLATFORM_SHARIF_ID, state_texts_mapping.get(Action.RETURN)): information,


    # Location transitions
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_JABER)): get_location,
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_CE_DP)): get_location,
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_LUNCH)): get_location,
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_MOSQUE)): get_location,
    (State.LOCATION, state_texts_mapping.get(State.LOCATION_THEATER)): get_location,
    (State.LOCATION, action_texts_mapping.get(Action.RETURN)): information,

    (State.CONTACT_US, None): send_message_to_admin,
    (State.CONTACT_US, action_texts_mapping.get(Action.RETURN)): main_menu,

    # Schedule state
    (State.SCHEDULE, None): show_schedule,
    (State.SCHEDULE, action_texts_mapping.get(Action.RETURN)): main_menu,

    # Poll state
    (State.POLL, state_texts_mapping.get(State.POLL_very_happy)): polling,
    (State.POLL, state_texts_mapping.get(State.POLL_happy)): polling,
    (State.POLL, state_texts_mapping.get(State.POLL_poker)): polling,
    (State.POLL, state_texts_mapping.get(State.POLL_angry)): polling,
    (State.POLL, state_texts_mapping.get(State.POLL_very_angry)): polling,
    (State.POLL, action_texts_mapping.get(Action.RETURN)):main_menu,

}
