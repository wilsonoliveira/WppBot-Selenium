from wppbot import WppApi

wpp = WppApi(60)
# while True:
# wpp.send_message('WACAO', ':)')
messages = wpp.get_messages_chat("FIFA 🎮", 20)
# print(len(messages))
<<<<<<< HEAD
#wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w')
=======
# for message in messages:
#     print(message.text)
chats = wpp.chat_with_unseen_messages()
print(len(chats))
print(chats)
# wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w')
>>>>>>> e29651d3920b3685665779724324beb682f50c9e
