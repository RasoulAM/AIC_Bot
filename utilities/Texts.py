import os

from utilities.Emojies_table import emojies

db_path = os.getcwd() + '/utilities' + '/database.db'
db_path1 = os.getcwd() + '/database.db'



main_menu_texts=[
    "مکانها" + emojies.get('location'),
    "نظرسنجی" + emojies.get('clipboard'),
    "برنامه زمان بندی" + emojies.get('calender'),
    "اطلاعات و اخبار" + emojies.get('information'),
    "مسابقه عکس " + emojies.get('camera'),
    "ارتباط با ما",
    "صندوق پیام",
]

locations_buttons_texts = [
    "غذاخوری" + emojies.get('dining_hall'),
    "سالن جابر",
    "دانشکده کامپیوتر",
    "بازگشت",
]

admin_panel_buttons_texts = [
    "خواندن پیامها",
    "بازگشت",
]

day_selection_buttons_texts = [
    "روز اول",
    "روز دوم",
    "بازگشت",
]




