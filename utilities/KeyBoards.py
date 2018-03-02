# coding: utf-8


from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

from utilities.Texts import *


def _main_keyboard():
    # return ReplyKeyboardMarkup(keyboard=[KeyboardButton(text=keyboard_text) for keyboard_text in
    # default_buttons_texts])
    temp = list(map(lambda text: KeyboardButton(text=text), main_menu_texts))
    btn_lst = [
        [
            temp[0], temp[1], temp[2]
        ],
        [
            temp[3], temp[4], temp[5], temp[6]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _location_default_keyboard():
    loc_temp = list(map(lambda text: KeyboardButton(text=text), locations_buttons_texts))
    btn_lst = [
        [
            loc_temp[0], loc_temp[1]
        ],
        [
            loc_temp[2], loc_temp[3]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _contact_us_keyboard():
    btn_lst = [
        [
            locations_buttons_texts[3]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _admin_panel_keyboard():
    btn_lst = [
        [
            admin_panel_buttons_texts[0], admin_panel_buttons_texts[1]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _day_selection_keyboard():
    btn_lst = [
        [
            day_selection_buttons_texts[0], day_selection_buttons_texts[1],
            day_selection_buttons_texts[2]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


main_keyboard = _main_keyboard()
location_keyboard = _location_default_keyboard()
contact_us_keyboard = _contact_us_keyboard()
admin_panel_keyboard = _admin_panel_keyboard()
day_selection_keyboard = _day_selection_keyboard()