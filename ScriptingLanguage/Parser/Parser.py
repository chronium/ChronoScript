from ScriptingLanguage.Lexer.Lexer import Lexer
from ScriptingLanguage.Parser.AstNodes.ProgramNodes import Program
from ScriptingLanguage.Parser.ParsableTokenStream import ParsableTokenStream, DifferentTokenException, FailedCapture
from ScriptingLanguage.Parser.parsers.Assignment import assignment
from ScriptingLanguage.Parser.parsers.Expressions import muldiv, addsub, expression
from ScriptingLanguage.Parser.parsers.Functions import function_call, function_def
from ScriptingLanguage.Tokens import EOF, NumberLiteral, Symbol, Keyword, Indent

__author__ = 'chronium'

class Parser:
    def __init__(self):
        self.token_stream = None

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

    def parse_immediate(self, line):
        self.token_stream = ParsableTokenStream(line)
        return self.parse_line()

    def parse_line(self):
        indents = 0
        while isinstance(self.token_stream.current(), Indent):
            self.token_stream.read()
            indents += 1
        try:
            value = expression(self)
        except FailedCapture:
            try:
                value = assignment(self)
            except FailedCapture:
                try:
                    value = function_call(self)
                except FailedCapture:
                    value = None
        self.token_stream.read()
        return value, indents

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
