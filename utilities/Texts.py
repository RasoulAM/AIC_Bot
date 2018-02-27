from utilities.Emojies_table import *
import os
from dispatcher import State


db_path = os.getcwd() + '/utilities' + '/database.db'
db_path1 = os.getcwd() + '/database.db'

admin_main_menu_texts = {
    State.ADMIN_PANEL: "پنل ادمین",
    State.LOCATION: "نقشه دانشگاه" + emojies.get('location'),
    State.POLL: "نظرسنجی" + emojies.get('clipboard'),
    State.SCHEDULE: "برنامه زمان بندی" + emojies.get('calender'),
    State.NEWS: "اطلاعات و اخبار" + emojies.get('information'),
    State.PHOTOGRAPHY_CONTEST: "مسابقه عکس " + emojies.get('camera'),
    State.CONTACT_US: "ارتباط با ما",
    State.INBOX: "صندوق پیام",

}

main_menu_texts={
    State.LOCATION: "نقشه دانشگاه" + emojies.get('location'),
    State.POLL: "نظرسنجی" + emojies.get('clipboard'),
    State.SCHEDULE: "برنامه زمان بندی" + emojies.get('calender'),
    State.NEWS: "اطلاعات و اخبار" + emojies.get('information'),
    State.PHOTOGRAPHY_CONTEST: "مسابقه عکس " + emojies.get('camera'),
    State.CONTACT_US: "ارتباط با ما",
    State.INBOX: "صندوق پیام",

}


locations_buttons_texts = {
    State.LOCATION_LUNCH: "غذاخوری" + emojies.get('dining_hall'),
    State.LOCATION_JABER:  "سالن جابر",
    State.LOCATION_CE_DP: "دانشکده کامپیوتر"
}



