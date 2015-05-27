from ScriptingLanguage.Parser.AstNodes.ProgramNodes import Program
from ScriptingLanguage.Parser.ParsableTokenStream import ParsableTokenStream, DifferentTokenException, FailedCapture
from ScriptingLanguage.Parser.parsers.Assignment import assignment
from ScriptingLanguage.Parser.parsers.Expressions import muldiv, addsub, expression
from ScriptingLanguage.Parser.parsers.Functions import function_call, function_def
from ScriptingLanguage.Tokens import EOF, NumberLiteral, Symbol, Keyword

__author__ = 'chronium'

class Parser:
    def __init__(self, source):
        self.token_stream = ParsableTokenStream(source)

    def parse(self):
        program = Program()

        while not isinstance(self.token_stream.current(), EOF):
            '''
            try:
                value = expression(self)
            except FailedCapture:
                try:
                    value = function_call(self)
                except FailedCapture:
                    try:
                        value = assignment(self)
                    except FailedCapture:
                        try:
                            value = function_def(self)
                        except FailedCapture:
                            value = None
            '''
            program.add_node(self.parse_line())
        return program

    def parse_line(self):
        try:
            value = expression(self)
        except FailedCapture:
            try:
                value = assignment(self)
            except FailedCapture:
                value = None
        self.token_stream.read()
        return value

    def check_symbol(self, value):
        if self.token_stream.is_match(Symbol):
            if self.token_stream.current().value == value:
                return True
        return False

    def read_symbol(self, value):
        if self.check_symbol(value):
            return self.token_stream.read()
        return None

    def check_keyword(self, value):
        if self.token_stream.is_match(Keyword):
            if self.token_stream.current().value == value:
                return True
        return False

    def read_keyword(self, value):
        if self.check_keyword(value):
            return self.token_stream.read()
        raise DifferentTokenException
