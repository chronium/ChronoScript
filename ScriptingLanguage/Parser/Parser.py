from ScriptingLanguage.Parser.AstNodes.FunctionNodes import FunctionNode
from ScriptingLanguage.Parser.AstNodes.ProgramNodes import Program, BodyNode
from ScriptingLanguage.Parser.ParsableTokenStream import ParsableTokenStream, DifferentTokenException, FailedCapture
from ScriptingLanguage.Parser.parsers.Assignment import assignment
from ScriptingLanguage.Parser.parsers.Expressions import muldiv, addsub, expression
from ScriptingLanguage.Parser.parsers.Functions import function_call, function_def
from ScriptingLanguage.Tokens import EOF, NumberLiteral, Symbol, Keyword, Indent

__author__ = 'chronium'

class Parser:
    def __init__(self):
        self.token_stream = None

    def parse(self, line):
        self.token_stream = ParsableTokenStream(line)
        program = Program()

        while not isinstance(self.token_stream.current(), EOF) and self.token_stream.current():
            program.add_node(self.parse_body())
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
        return program

    def parse_body(self):
        lines = []
        init_indent = self.get_indentation()
        lines.append(self.parse_line())
        while self.token_stream.current() and self.get_indentation() == init_indent \
                and not isinstance(self.token_stream.current(), EOF):
            lines.append(self.parse_line())
        return BodyNode(lines)

    def parse_function(self):
        def op():
            try:
                func = function_def(self)
                body = self.parse_body()
                return FunctionNode((func, body))
            except FailedCapture:
                return None
        return self.token_stream.capture(op)

    def get_indentation(self):
        indents = 0
        while isinstance(self.token_stream.peek(indents), Indent):
            indents += 1
        return indents

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
                    value = self.parse_function()
                except FailedCapture:
                    try:
                        value = function_call(self)
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
