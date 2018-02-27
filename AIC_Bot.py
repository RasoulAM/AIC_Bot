from pprint import *
import telepot
import sqlite3
from telepot.delegate import *
from telepot.loop import MessageLoop

import dispatcher
from utilities.Emojies_table import *
from utilities.KeyBoards import *
from utilities.Queries import *
from dispatcher import *

TOKEN = "514497589:AAFC24mg4F2nfv4C_2cvmtgR55chvaahcXc"

chat_ids = telepot.helper.SafeDict()


class StateHandler(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(StateHandler, self).__init__(*args, **kwargs)
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.query = self.connection.cursor()
        self.exists = False
        self.state = 0
        if not self._started():
            self.state = 1
            self._starter()
            self.sender.sendMessage(text="Hi You!")

    def _started(self):
        a = self.query.execute(fetch_chat_id + str(self.chat_id)).fetchall()
        self.connection.commit()
        if a:
            self.exists = True
            self.state = a[0][1]
        return self.exists

    def on_chat_message(self, msg):
        pprint(msg)
        if msg["text"] == "نظرسنجی" and self.state == 0:
            self.state = 1
        else:
            dispatcher._dispatcher(self, msg)
            # self.sender.sendMessage(text="تا همینجاش بیشتر نزدم!")

    def _starter(self):
        self.sender.sendMessage(text="Hello", reply_markup=main_keyboard)
        self.started = True

    def on_close(self, msg):
        if self.exists:
            query = (update_state1 + str(self.state) + update_state2 + str(self.chat_id))
        else:
            query = insert_state + str(self.chat_id) + "," + str(self.state) + ')'
        self.query.execute(query)
        self.connection.commit()

    def go_forward(self, i):
        self.state = self.state * 10 + i



if __name__ == '__main__':
    bot = telepot.DelegatorBot(TOKEN, {
        pave_event_space()(
            per_chat_id(), create_open, StateHandler, timeout=15),
    })

    MessageLoop(bot).run_forever()
