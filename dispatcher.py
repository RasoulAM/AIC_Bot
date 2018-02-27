from utilities import Texts
import AIC_Bot
from functions import *
from enum import Enum


class State(Enum):
    MAIN = 0,

    # main menu
    LOCATION = 101,
    POLL = 102,
    SCHEDULE = 103,
    NEWS = 104,
    PHOTOGRAPHY_CONTEST = 105,
    CONTACT_US = 106,
    INBOX = 107,

    # LOCATION MENU
    LOCATION_CE_DP = 111,
    LOCATION_LUNCH = 112,
    LOCATION_JABER = 113,

    # schedules
    SCHEDULE_DAY1 = 121,
    SCHEDULE_DAY2 = 122,


dispatchers = {
    #main menu
    State.LOCATION: map_loader,
    State.POLL: poll,
    State.SCHEDULE: schedule,
    State.NEWS: news,
    State.PHOTOGRAPHY_CONTEST: photography_contest,

    State.LOCATION_JABER: location_jaber,
    State.LOCATION_LUNCH: location_lunch,
    State.LOCATION_CE_DP: location_ce_dp
}


def _dispatcher(delegate, msg):
    new_state = _transition(delegate.state, msg["text"])
    if new_state:
        dispatchers[new_state](delegate, msg)
    if msg["text"] in dispatchers:
        (dispatchers[msg["text"]])(delegate, msg)


transitions = {

    #main transitions
    (State.MAIN, main_menu_texts.get(State.LOCATION)): State.LOCATION ,
    (State.MAIN, main_menu_texts.get(State.POLL)): State.POLL,
    (State.MAIN, main_menu_texts.get(State.SCHEDULE)): State.SCHEDULE,
    (State.MAIN, main_menu_texts.get(State.NEWS)): State.NEWS,
    (State.MAIN, main_menu_texts.get(State.PHOTOGRAPHY_CONTEST)) : State.PHOTOGRAPHY_CONTEST,
    (State.MAIN, main_menu_texts.get(State.INBOX)): State.INBOX,
    (State.MAIN, main_menu_texts.get(State.LOCATION)): State.LOCATION ,
    (State.MAIN, main_menu_texts.get(State.CONTACT_US)): State.CONTACT_US,

    #Location transitions
    (State.LOCATION, main_menu_texts.get(State.LOCATION_JABER)): State.L,

}


def _transition(current_state, input):
    return transitions.get((current_state, input))
