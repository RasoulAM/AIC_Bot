from utilities import Texts
import AIC_Bot


dispatcher = {
    Texts.main_menu_texts[0]: AIC_Bot.StateHandler.starter
}
