from ScriptingLanguage.Parser.AstNode import ExpressionNode, NumberNode
from ScriptingLanguage.Parser.ParsableTokenStream import FailedCapture, DifferentTokenException
from ScriptingLanguage.Parser.parsers.Functions import function_call
from ScriptingLanguage.Tokens import NumberLiteral

__author__ = 'chronium'

def number(parser):
    def op():
        try:
            value = 1
            if parser.read_symbol('-'):
                value = -1
            return NumberNode(parser.token_stream.take(NumberLiteral).value * value)
        except DifferentTokenException:
            return None
    return parser.token_stream.capture(op)

def operand(parser):
    def op():
        try:
            return number(parser)
        except FailedCapture:
            try:
                return function_call(parser)
            except FailedCapture:
                return None
    return parser.token_stream.capture(op)

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
            left = operand(parser)
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
