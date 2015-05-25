from ScriptingLanguage.Parser.AstNode import ExpressionNode, NumberNode
from ScriptingLanguage.Parser.ParsableTokenStream import FailedCapture, DifferentTokenException
from ScriptingLanguage.Tokens import NumberLiteral

__author__ = 'chronium'

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

def expression(parser):
    def op():
        try:
            return addsub(parser)
        except FailedCapture:
            return None
    return parser.token_stream.capture(op)

def muldiv(parser):
    def op():
        try:
            left = number(parser)
            if parser.check_symbol('*') or parser.check_symbol('/') or parser.check_symbol('%'):
                symbol = parser.token_stream.read()
                right = muldiv(parser)
                return ExpressionNode((left, symbol.value, right))
            return left
        except FailedCapture:
            return None
    return parser.token_stream.capture(op)

def addsub(parser):
    def op():
        try:
            left = muldiv(parser)
            if parser.check_symbol('+') or parser.check_symbol('-'):
                symbol = parser.token_stream.read()
                right = muldiv(parser)
                return ExpressionNode((left, symbol.value, right))
            return left
        except FailedCapture:
            return None
    return parser.token_stream.capture(op)
