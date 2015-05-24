from ScriptingLanguage.Lexer.Token import Token

__author__ = 'chronium'

class EOF(Token):
    def __init__(self):
        super(EOF, self).__init__(name='EOF', value='EOF')

class Whitespace(Token):
    def __init__(self):
        super(Whitespace, self).__init__(name='Space', value=' ')

class Identifier(Token):
    def __init__(self, value):
        super(Identifier, self).__init__(name='Identifier', value=value)

class Symbol(Token):
    def __init__(self, value):
        super(Symbol, self).__init__(name='Symbol', value=value)
