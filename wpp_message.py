from datetime import datetime

class message:

    def __init__(self, data, time, nameAuthor, text):
        self.date_time = datetime.strptime(data+' '+time, '%d/%m/%Y %H:%M')
        self.author = nameAuthor
        self.text = text

    def is_equal(self, msg):
        if self.date_time == msg.date_time and self.author == msg.author and self.text == msg.text:
            return True
        return False