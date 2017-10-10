from datetime import datetime

class Chat:
    def __init__(self, message, sent_by):
        self.message = message
        self.time = datetime.now().strftime("%b %d %Y %H:%M:%S")
        self.sent_by = sent_by

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating =rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
