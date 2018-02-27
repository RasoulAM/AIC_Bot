# coding: utf-8
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from utilities.Texts import *


def _main_keyboard():
    # return ReplyKeyboardMarkup(keyboard=[KeyboardButton(text=keyboard_text) for keyboard_text in
    # default_buttons_texts])
    temp = list(map(lambda text: KeyboardButton(text=text), main_menu_texts))
    btn_lst = [
        [
            temp[0], temp[1]
        ],
        [
            temp[2], temp[3], temp[4]
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
        ],
        [
            loc_temp[4]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


main_keyboard = _main_keyboard()
location_keyboard = _location_default_keyboard()




