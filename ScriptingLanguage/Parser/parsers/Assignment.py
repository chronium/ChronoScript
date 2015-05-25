from ScriptingLanguage.Parser.AstNode import AssignmentNode
from ScriptingLanguage.Parser.ParsableTokenStream import DifferentTokenException
from ScriptingLanguage.Parser.parsers.Expressions import expression
from ScriptingLanguage.Tokens import Identifier

__author__ = 'chronium'

def assignment(parser):
    def op():
        try:
            name = parser.token_stream.take(Identifier)
            if parser.check_symbol('='):
                parser.token_stream.read()
                value = expression(parser)
                return AssignmentNode((name.value, value))
        except DifferentTokenException:
            return None
    return parser.token_stream.capture(op)
