from utilities.Emojies_table import emojies
from utilities.Texts import *

def get_location(msg_text):  # latitude, longitude
    jaber = "جابر"
    halls = "تالار"
    canteen = "غذا"
    mosque = "مسجد"
    dorm = "خوابگاه"
    if canteen in msg_text:
        return 35.703028440307705, 51.351864427319924  # self
    elif halls in msg_text:
        return 35.704161912937366, 51.35213989017757  # halls
    elif jaber in msg_text:
        return 35.70461974064782, 51.34968727827072
    elif mosque in msg_text:
        return 35.700566283671904, 51.35151386260986
    elif dorm in msg_text:
        return 35.70372891258694, 51.343659162157564
    return None


locations = {
    locations_buttons_texts[0]: [35.703028440307705, 51.351864427319924],
    locations_buttons_texts[1]: [35.70461974064782, 51.34968727827072],
    locations_buttons_texts[2]: [35, 51],
    locations_buttons_texts[3]: [35, 51],
    locations_buttons_texts[4]: [35, 51],

}

