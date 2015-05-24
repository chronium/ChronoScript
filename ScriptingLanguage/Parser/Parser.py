from ScriptingLanguage.Parser.AstNode import Test
from ScriptingLanguage.Parser.ParsableTokenStream import ParsableTokenStream
from ScriptingLanguage.Tokens import EOF

__author__ = 'chronium'

class Parser(object):
    def __init__(self, source):
        self.token_stream = ParsableTokenStream(source)

    def parse(self):
        statement = []

        while not isinstance(self.token_stream.current(), EOF):
            statement.append(self.test())
        return statement

    def test(self):
        def op():
            if self.token_stream.current().value == ':=':
                self.token_stream.read()
                return Test()
            return None
        return self.token_stream.capture(op)
