__author__ = 'chronium'

class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "Token({}:'{}')".format(self.name, self.value)
