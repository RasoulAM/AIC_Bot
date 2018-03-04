from enum import Enum


class State(Enum):
    MAIN = 1
    ADMIN_PANEL = 2
    ANSWER_OR_PASS = 3
    ANSWERING = 4
    PASS = 5
    POLL_RESULT = 6
    ANNOUNCEMENT = 7
    ANNOUNCING = 8

    # main menu
    INFORMATION = 101
    POLL = 102
    PHOTOGRAPHY_CONTEST = 103
    CONTACT_US = 104
    INBOX = 105
    ONLINE_RESULT = 106

    # information MENU
    LOCATION = 141
    SCHEDULE = 142
    SHARIF_ID = 143

    # LOCATION MENU
    LOCATION_CE_DP = 111
    LOCATION_LUNCH = 112
    LOCATION_JABER = 113
    LOCATION_MOSQUE = 114
    LOCATION_THEATER = 115

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
