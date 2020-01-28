from datetime import datetime

class message:

    def __init__(self, location, data, time, nameAuthor, text):
        self.date_time = datetime.strptime(data+' '+time, '%d/%m/%Y %H:%M')
        self.author = nameAuthor
        self.text = text
        self.location = location

    def set_message(self, location, date_time, nameAuthor, text):
        self.date_time = datetime.strptime(date_time, '%d/%m/%Y %H:%M')
        self.author = nameAuthor
        self.text = text
        self.location = location


    def is_equal(self, msg):
        if self.date_time == msg.date_time and self.author == msg.author and self.text == msg.text:
            return True
        return False

    def compare_time(self, time):
        if self.date_time > time:
            return 1
        elif self.date_time == time:
            return 0
        else:
            return -1
