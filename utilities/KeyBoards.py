# coding: utf-8


from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from utilities.Texts import *


def _main_keyboard():
    temp = list(map(lambda text: KeyboardButton(text=text), main_menu_texts))
    btn_lst = [
        [
            temp[0], temp[1], temp[2]
        ],
        [
            temp[3], temp[4], temp[5]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _information_keyboard():
    temp = list(map(lambda text: KeyboardButton(text=text), information_menu_button_texts))
    btn_lst = [
        [
            temp[0]
        ],
        [
            temp[1]
        ],
        [
            temp[2]
        ],
        [
            temp[3]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _location_default_keyboard():
    loc_temp = list(map(lambda text: KeyboardButton(text=text), locations_buttons_texts))
    btn_lst = [
        [
            loc_temp[0], loc_temp[1], loc_temp[2]
        ],
        [
            loc_temp[3], loc_temp[4], loc_temp[5]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _contact_us_keyboard():
    btn_lst = [
        [
            locations_buttons_texts[5]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _admin_panel_keyboard():
    btn_lst = [
        [
            admin_panel_buttons_texts[0], admin_panel_buttons_texts[1], admin_panel_buttons_texts[2], admin_panel_buttons_texts[3]
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _day_selection_keyboard():
    btn_lst = [
        [
            day_selection_buttons_texts[0]
        ]
        ,
        [
            day_selection_buttons_texts[1]
        ]
        ,
        [
            day_selection_buttons_texts[2]
        ]
        
    ]
    return ReplyKeyboardMarkup(keyboard=btn_lst)


def _admin_read_message_keyboard():
    btn_lst = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=admin_read_messages_buttons_texts[0], callback_data='pass'),
        InlineKeyboardButton(text=admin_read_messages_buttons_texts[1], callback_data='answer'),
    ]])
    return btn_lst


def _polling_keyboard():
    btn_lst = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=polling_button_texts[0], callback_data='very happy'),
        InlineKeyboardButton(text=polling_button_texts[1], callback_data='happy'),
        InlineKeyboardButton(text=polling_button_texts[2], callback_data='poker'),
        InlineKeyboardButton(text=polling_button_texts[3], callback_data='angry'),
        InlineKeyboardButton(text=polling_button_texts[4], callback_data='very angry'),
    ]])
    return btn_lst


main_keyboard = _main_keyboard()
information_keyboard = _information_keyboard()
location_keyboard = _location_default_keyboard()
contact_us_keyboard = _contact_us_keyboard()
admin_panel_keyboard = _admin_panel_keyboard()
day_selection_keyboard = _day_selection_keyboard()
admin_read_message_keyboard = _admin_read_message_keyboard()
polling_keyboard = _polling_keyboard()