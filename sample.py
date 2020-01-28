# -*- coding: utf-8 -*-
from wppbot import WppApi
from datetime import datetime

wpp = WppApi(60)
# while True:
# wpp.send_message('WACAO', ':)')
# for i in range(0, 10):
groups = ["CRUZEIRO PORRA2020", "Zilma","Emerson", "A Grande Familia"]
wpp.watch_groups(groups, datetime.now())
# for message in messages:
#     print(message.text)
#wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w') 
# chats = wpp.chat_with_unseen_messages()
# print(len(chats))
# print(chats)
# chats = wpp.get_chat_names()
# print(len(chats))
# print(chats)
# wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w')

