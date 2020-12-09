# Passport class that holds the fields
class Passport(object):
    def __init__(self, fields):
        self.fields = fields

    def getFields(self):
        return self.fields

    def getValueFor(self, key):
        return self.fields[key]