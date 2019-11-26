from wppbot import WppApi

wpp = WppApi(60)
# while True:
# wpp.send_message('WACAO', ':)')
messages = wpp.get_messages_chat("FIFA 🎮", 20)
# print(len(messages))
#wpp.join_group('https://chat.whatsapp.com/EbsTIzO3X6W7Svmqcx529w')
