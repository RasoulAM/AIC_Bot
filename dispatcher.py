from utilities import Texts
import AIC_Bot


dispatchers = {
        Texts.main_menu_texts[0]: AIC_Bot.StateHandler.map_loader
    }


def _dispatcher(msg):
    if msg["text"] in dispatchers:
        AIC_Bot.dispatchers[msg["text"]](msg)
