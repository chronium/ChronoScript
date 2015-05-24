from ScriptingLanguage.Parser.AstNode import ExpressionNode
from ScriptingLanguage.Parser.ParsableTokenStream import FailedCapture
__author__ = 'chronium'

def muldiv(parser):
    def op():
        try:
            left = parser.number()
            if parser.check_symbol('*') or parser.check_symbol('/'):
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
