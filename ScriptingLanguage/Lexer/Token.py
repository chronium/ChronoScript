__author__ = 'chronium'

class Token(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "Token(%s:'%s')" % (self.name, self.value)
