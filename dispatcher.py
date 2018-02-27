from utilities import Texts
import AIC_Bot
from functions import *


dispatchers = {
        Texts.main_menu_texts[0]: map_loader
    }


def _dispatcher(delegate, msg):
    if msg["text"] in dispatchers:
        (dispatchers[msg["text"]])(delegate, msg)
