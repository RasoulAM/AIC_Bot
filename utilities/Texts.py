from utilities.Emojies_table import *
import os

db_path = os.getcwd() + '/utilities' + '/database.db'
db_path1 = os.getcwd() + '/database.db'

main_menu_texts = [
    "نقشه دانشگاه" + emojies.get('location'),
    "نظرسنجی" + emojies.get('clipboard'),
    "برنامه زمان بندی" + emojies.get('calender'),
    "اطلاعات و اخبار" + emojies.get('information'),
    "مسابقه عکس " + emojies.get('camera')
]

location_texts = [
    ""
]