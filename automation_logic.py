
import sqlite3
import pandas as pd
import numpy as np
from uiautomation import WindowControl, MenuControl
from zhipuai import ZhipuAI

class AutomationLogic:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.zhipuai_client = ZhipuAI(apikey='your_api_key')

    def load_data(self):
        self.cursor.execute('SELECT * FROM replies')
        self.data = self.cursor.fetchall()

    def get_reply(self, message):
        for row in self.data:
            if row[0] in message:
                return row[1]
        return None

    def send_reply(self, message):
        reply = self.get_reply(message)
        if reply:
            print(f"Sending reply: {reply}")
        else:
            print("No reply found")

    def close_connection(self):
        self.conn.close()

# Example usage:
# logic = AutomationLogic()
# logic.load_data()
# logic.send_reply("Hello")
# logic.close_connection()
