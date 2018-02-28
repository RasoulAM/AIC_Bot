import sqlite3
from pprint import *

import telepot
from telepot.delegate import *
from telepot.loop import MessageLoop

import dispatcher
from dispatcher import *
from utilities.Queries import *
from utilities.Texts import db_path

TOKEN = "514497589:AAFC24mg4F2nfv4C_2cvmtgR55chvaahcXc"

chat_ids = telepot.helper.SafeDict()


class StateHandler(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(StateHandler, self).__init__(*args, **kwargs)
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.query = self.connection.cursor()
        id_in_database = self.query.execute(fetch_user + str(self.chat_id)).fetchall()
        self.connection.commit()
        self.exists = False
        if id_in_database:
            self.state = State(id_in_database[0][1])
            self.exists = True
        if not self.exists:
            self.state = State.MAIN
            self._starter()
            self.sender.sendMessage(text="First time user detected!!")
        else:
            self.state = State(id_in_database[0][1])
        print("at the begin state: " + str(self.state.value))

    def on_chat_message(self, msg):
        pprint(msg)
        dispatcher.dispatch(self, msg)

    def _starter(self):
        self.sender.sendMessage(text="Hello", reply_markup=main_keyboard)
        self.started = True

    def on_close(self, msg):
        if self.exists:
            query = (update_state1 + str(self.state.value) + update_state2 + str(self.chat_id))
        else:
            query = insert_state + str(self.chat_id) + "," + str(self.state.value) + ')'
        self.query.execute(query)
        self.connection.commit()
        print("Timed out at state: " + str(self.state.value))


if __name__ == '__main__':
    bot = telepot.DelegatorBot(TOKEN, {
        pave_event_space()(
            per_chat_id(), create_open, StateHandler, timeout=15),
    })

    MessageLoop(bot).run_forever()
