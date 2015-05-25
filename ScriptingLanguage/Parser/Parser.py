from ScriptingLanguage.Parser.AstNode import  NumberNode, Program
from ScriptingLanguage.Parser.ParsableTokenStream import ParsableTokenStream, DifferentTokenException, FailedCapture
from ScriptingLanguage.Parser.parsers.Expressions import muldiv, addsub, expression
from ScriptingLanguage.Parser.parsers.Functions import function_call
from ScriptingLanguage.Tokens import EOF, NumberLiteral, Symbol

__author__ = 'chronium'

class Parser:
    def __init__(self, source):
        self.token_stream = ParsableTokenStream(source)

    def parse(self):
        program = Program()

        while not isinstance(self.token_stream.current(), EOF):
            program.add_node(self.multiple(expression, function_call))
        return program

    def multiple(self, first, other):
        try:
            return first(self)
        except FailedCapture:
            val = other(self)
            return val

    def check_symbol(self, value):
        if self.token_stream.is_match(Symbol):
            if self.token_stream.current().value == value:
                return True
        return False

    def read_symbol(self, value):
        if self.check_symbol(value):
            return self.token_stream.read()
        return None
