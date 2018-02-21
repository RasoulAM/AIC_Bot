from pprint import *

import telepot
from telepot.delegate import *
from telepot.loop import MessageLoop

TOKEN = "FODONG"


class StateHandler(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(StateHandler, self).__init__(*args, **kwargs)
        self.Reply = "Reply"

    def on_chat_message(self, msg):
        pprint(msg)

    def on_close(self, msg):
        self.sender.sendMessage(text="OOPS!")


bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, StateHandler, timeout= 5),
])
MessageLoop(bot).run_forever()
