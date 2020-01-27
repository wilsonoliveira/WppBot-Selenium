from wppbot import WppApi

wpp = WppApi(60)
# while True:
# wpp.send_message('WACAO', ':)')
# messages = wpp.get_messages_chat("FIFA 🎮", 20)
# print(len(messages))
#wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w') 
# for message in messages:
#     print(message.text)
# chats = wpp.chat_with_unseen_messages()
# print(len(chats))
# print(chats)
chats = wpp.get_chat_names()
print(len(chats))
print(chats)
# wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w')

