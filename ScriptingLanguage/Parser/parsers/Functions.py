from ScriptingLanguage.Parser.AstNode import FunctionCallNode
from ScriptingLanguage.Parser.ParsableTokenStream import DifferentTokenException
from ScriptingLanguage.Tokens import Identifier

__author__ = 'chronium'

def function_call(parser):
    def op():
        try:
            name = parser.token_stream.take(Identifier)
            if parser.read_symbol('(') is not None and parser.read_symbol(')') is not None:
                return FunctionCallNode(name.value)
        except DifferentTokenException:
            return None
        return None
    return parser.token_stream.capture(op)
