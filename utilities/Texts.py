import os

from utilities.Emojies_table import emojies

db_path = os.getcwd() + '/utilities' + '/database.db'
db_path1 = os.getcwd() + '/database.db'



main_menu_texts = [
    "نظرسنجی" + emojies.get('clipboard'),
    "اطلاعات و راهنمایی ها" + emojies.get('information'),
    "مسابقه عکس " + emojies.get('camera'),
    "ارتباط با ما",
    "نتایج آنلاین",
    "صندوق پیام",
]

information_menu_button_texts = [
    "برنامه زمان بندی" + emojies.get('calender'),
    "مکانها" + emojies.get('location'),
    "راهنمای اتصال به VPN شریف",
    "بازگشت"
]

locations_buttons_texts = [
    "غذاخوری" + emojies.get('dining_hall'),
    "دانشکده کامپیوتر",
    "مسجد",
    "آمفی تئاتر مرکزی",
    "بازگشت",
]

admin_panel_buttons_texts = [
    "خواندن پیامها",
    "نتیجه نظر سنجی",
    "ارسال اطلاعیه",
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

admin_chat_id = [
    105566991,
    123375596,
]



