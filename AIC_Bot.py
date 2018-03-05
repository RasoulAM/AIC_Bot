import sqlite3
from pprint import *

import telepot
from telepot.delegate import *
from telepot.loop import MessageLoop

import dispatcher
from dispatcher import *
from utilities.Queries import *
from utilities.Texts import db_path

TOKEN = "547363442:AAE0A14extwZ4f2Nkt14SdOvfkvSeWR2Wfg"
# TOKEN = "514497589:AAFC24mg4F2nfv4C_2cvmtgR55chvaahcXc"

chat_ids = telepot.helper.SafeDict()


class StateHandler(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(StateHandler, self).__init__(*args, **kwargs)
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.query = self.connection.cursor()
        id_in_database = self.query.execute(fetch_user.format(self.chat_id)).fetchall()
        print(fetch_user.format(self.chat_id))
        print(id_in_database)
        self.connection.commit()
        self.existed_before = False
        self.answer_to = None
        self.first_name = None
        self.message_id_replied = None
        self.bott = bot
        if id_in_database:
            self.state = State(id_in_database[0][2])
            self.existed_before = True
        if not self.existed_before:
            self.state = State.MAIN
            self.sender.sendMessage(text="به بات رقابت هوش مصنوعی شریف خوش آمدید.", reply_markup=main_keyboard)
        else:
            self.state = State(id_in_database[0][2])
        print("Initialization of connection finished. State: " + str(self.state.value))

    def on_chat_message(self, msg):
        # with open("log.txt", "a") as f:
        #     f.write(str(msg) + '\n')
        pprint(msg)
        self.first_name = msg["from"]["first_name"]
        # By writing "state", the state will be shown
        if msg["text"] is None:
            return
        if msg["text"] == "state":
            self.sender.sendMessage(text=str(self.state))
            return

        dispatcher.dispatch(self, msg)

    def on_callback_query(self, msg):
        # with open("log.txt", "a") as f:
        #     f.write(str(msg) + '\n')
        pprint(msg)
        dispatcher.dispatch(self, msg)

    def on_close(self, msg):
        if self.existed_before:
            query = update_state.format(self.state.value, self.chat_id)
        else:
            query = insert_state.format(self.chat_id, self.first_name, self.state.value)
        self.query.execute(query)
        self.connection.commit()
        print("Timed out connection at state: " + str(self.state.value))


if __name__ == '__main__':
    bot = telepot.DelegatorBot(TOKEN, [
        include_callback_query_chat_id(
            pave_event_space())(
            per_chat_id(), create_open, StateHandler, timeout=400),
    ])

    MessageLoop(bot).run_forever()
