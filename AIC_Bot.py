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
        self.existed_before = False
        if id_in_database:
            self.state = State(id_in_database[0][1])
            self.existed_before = True
        if not self.existed_before:
            self.state = State.MAIN
            self.sender.sendMessage(text="First time user detected!!", reply_markup=main_keyboard)
        else:
            self.state = State(id_in_database[0][1])
        print("Initialization of connection finished. State: " + str(self.state.value))

    def on_chat_message(self, msg):
        pprint(msg)

        # By writing "state", the state will be shown
        if msg["text"] is None:
            return
        if msg["text"] == "state":
            self.sender.sendMessage(text=str(self.state))
            return

        dispatcher.dispatch(self, msg)

    def on_close(self, msg):
        if self.existed_before:
            query = (update_state1 + str(self.state.value) + update_state2 + str(self.chat_id))
        else:
            query = insert_state + str(self.chat_id) + "," + str(self.state.value) + ')'
        self.query.execute(query)
        self.connection.commit()
        print("Timed out connection at state: " + str(self.state.value))


if __name__ == '__main__':
    bot = telepot.DelegatorBot(TOKEN, {
        pave_event_space()(
            per_chat_id(), create_open, StateHandler, timeout=200),
    })

    MessageLoop(bot).run_forever()
