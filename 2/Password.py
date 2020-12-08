# Password class that holds the password
class Password(object):
    def __init__(self, password):
        self.password = password

    def getPassword(self):
        return self.password