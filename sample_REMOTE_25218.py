from wppbot import WppApi

wpp = WppApi(60)
# while True:
# wpp.send_message('WACAO', ':)')
# messages = wpp.get_messages_chat("Delegação Universicopa 💚", 20)
# print(len(messages))
# for message in messages:
#     print(message.text)
chats = wpp.chat_with_unseen_messages()
print(len(chats))
print(chats)
# wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w')
