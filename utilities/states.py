from enum import Enum


class State(Enum):
    MAIN = 1
    ADMIN_PANEL = 2
    ANSWER_OR_PASS = 3
    ANSWERING = 4
    PASS = 5
    POLL_RESULT = 6

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

    # poll
    POLL_very_happy = 131
    POLL_happy = 132
    POLL_poker = 133
    POLL_angry = 134
    POLL_very_angry = 135




class Action(Enum):
    RETURN = 1
