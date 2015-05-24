from ScriptingLanguage.Parser.AstNode import  NumberNode, Program
from ScriptingLanguage.Parser.ParsableTokenStream import ParsableTokenStream, DifferentTokenException, FailedCapture
from ScriptingLanguage.Parser.parsers.Expressions import muldiv, addsub
from ScriptingLanguage.Tokens import EOF, NumberLiteral, Symbol

__author__ = 'chronium'

class Parser(object):
    def __init__(self, source):
        self.token_stream = ParsableTokenStream(source)

    def parse(self):
        program = Program()

        while not isinstance(self.token_stream.current(), EOF):
            program.add_node(self.expression())
        return program

    def expression(self):
        def op():
            try:
                return addsub(self)
            except FailedCapture:
                return None
        return self.token_stream.capture(op)

    def number(self):
        def op():
            try:
                value = 1
                if self.read_symbol('-'):
                    value = -1
                return NumberNode(self.token_stream.take(NumberLiteral).value * value)
            except DifferentTokenException:
                return None
        return self.token_stream.capture(op)

    def check_symbol(self, value):
        if self.token_stream.is_match(Symbol):
            if self.token_stream.current().value == value:
                return True
        return False

    def read_symbol(self, value):
        if self.check_symbol(value):
            return self.token_stream.read()
        return None
