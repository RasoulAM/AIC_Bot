from enum import Enum


class State(Enum):
    MAIN = 1
    ADMIN_PANEL = 2
    ANSWER_MESSAGES = 3
    ANSWERING = 4

    # main menu
    LOCATION = 101
    POLL = 102
    SCHEDULE = 103
    NEWS = 104
    PHOTOGRAPHY_CONTEST = 105
    CONTACT_US = 106
    INBOX = 107

    # LOCATION MENU
    LOCATION_CE_DP = 111
    LOCATION_LUNCH = 112
    LOCATION_JABER = 113

    # schedules
    SCHEDULE_DAY1 = 121
    SCHEDULE_DAY2 = 122


class Action(Enum):
    RETURN = 1
