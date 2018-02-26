from pprint import *
import telepot
import sqlite3
from telepot.delegate import *
from telepot.loop import MessageLoop
from utilities.Emojies_table import *
from utilities.KeyBoards import *
from utilities.Queries import *

TOKEN = ""

chat_ids = telepot.helper.SafeDict()


class StateHandler(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(StateHandler, self).__init__(*args, **kwargs)
        self.con = sqlite3.connect(db_path, check_same_thread=False)
        self.query = self.con.cursor()
        print("Reply")
        if self._started():
            self.state = chat_ids[self.chat_id]
            self.started = True
        else:
            self.state = 1
            self.started = False
        self.chat_ids = None
        self.sender.sendMessage(text="Wow!")

    def _started(self):
        a = self.query.execute(fetch_chat_id).fetchall()
        b = [item for item in a if item[0] == self.chat_id]
        self.chat_ids = [item[0] for item in a]
        for i in self.chat_ids:
            print(i,)
        if len(b) != 0:
            return True
        return False

    def on_chat_message(self, msg):
        pprint(msg)
        if not self._started:
            self._starter()
        elif msg["text"] == "نظرسنجی" and self.state == 0:
            self.state = 1
        else:
            self.sender.sendMessage(text="تا همینجاش بیشتر نزدم!")


    @staticmethod
    def map_loader(self, msg):
        self.sender.sendMessage(text="Salam")

    def _starter(self, msg):
        self.sender.sendMessage(text="Hello", reply_markup=main_keyboard)
        self.started = True

    def on_close(self, msg):
        self.sender.sendMessage(text=emojies.get('camera'))
        chat_ids[self.chat_id] = self.state
        # try:
        print(insert_state, self.chat_id, self.state)
        state = [(self.chat_id), (self.state)]
        self.query.execute(insert_state, state)
        # except:
        #     print("sajjad")
        # finally:
        #     self.con.commit()


    def go_forward(self, i):
        self.state = self.state * 10 + i


if __name__ == '__main__':
    bot = telepot.DelegatorBot(TOKEN, {
        pave_event_space()(
            per_chat_id(), create_open, StateHandler, timeout=1),
    })

    MessageLoop(bot).run_forever()


