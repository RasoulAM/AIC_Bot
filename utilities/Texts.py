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
    "اضافه کردن عکس",
    "نتایج مسابقه عکس",
    "حذف عکس از مسابقه",
    "بازگشت",
]

day_selection_buttons_texts = [
    "روز اول",
    "روز دوم",
    "بازگشت",
]

platform_buttons_texts = [
    'Android',
    'Gnome',
    'iOS',
    'Mac',
    'KDE',
    'MS Windows',
    'Unity',
    'Windows 7',
    'بازگشت',
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
    25097866,
    71769373,
    105566991, #sajjad
    119495194,
    123375596, #rasoul
    183782606,
    147130888, #milad alikhani
]


questions = [

    "نظرت در مورد عملکرد کلی تیم اجرائی مسابقه چیه؟",
    "نظرت در مورد عملکرد کلی تیم فنی مسابقه چیه؟",
    "نظرت در مورد سیر تغییرات قسمت فنی(مثل توسعه سایت) چی بود؟",
    "نظرت در مورد بازی طراحی شده برای امسال چی بود؟",
    "نظرت در مورد زمان‌بندی مسابقه(غیرحضوری و حضوری) چیه؟",
    "نظرت در مورد پذیرایی‌ها و تدارکات مسابقه چی بود؟",
    "نظرت در مورد سخرانی‌های فنی امسال چی بود؟",
    "کلا خوش گذشت؟",
]


poll_result_text = '' \
"""
نتایج نظرسنجی تا این لحظه:
سوال اول: {0} تعداد افراد شرکت کننده: {1}
سوال دوم: {2} تعداد افراد شرکت کننده: {3}
سوال سوم: {4} تعداد افراد شرکت کننده: {5}
سوال چهارم: {6} تعداد افراد شرکت کننده: {7}
سوال پنجم: {8} تعداد افراد شرکت کننده: {9}
سوال ششم: {10} تعداد افراد شرکت کننده: {11}
سوال هفتم: {12} تعداد افراد شرکت کننده: {13}
سوال هشتم: {14} تعداد افراد شرکت کننده: {15}
"""

like_dislike_texts = [
    emojies.get("like"),
    emojies.get("dislike")
]


result_text1 = """
              نتایج مسابقه عکس تا این لحظه: 
              """

result_text2 = "likes: {0}\ndislikes: {1}"
