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
    "مسجد",
    "آمفی تئاتر مرکزی",
    "بازگشت",
]

admin_panel_buttons_texts = [
    "خواندن پیامها",
    "نتیجه نظر سنجی",
    "بازگشت",
]

day_selection_buttons_texts = [
    "روز اول",
    "روز دوم",
    "بازگشت",
]


admin_read_messages_buttons_texts = [
    "خواندم",
    "پاسخ"
]


polling_button_texts = [
    emojies.get("very happy"),
    emojies.get("happy"),
    emojies.get("poker"),
    emojies.get("angry"),
    emojies.get("very angry")
]



