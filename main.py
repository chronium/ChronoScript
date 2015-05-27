from ScriptingLanguage.Lexer.Lexer import Lexer, UnknownTokenException
from ScriptingLanguage.Matchers.MatchKeyword import MatchKeyword
from ScriptingLanguage.Matchers.MatchNumber import MatchNumber
from ScriptingLanguage.Matchers.MatchSymbol import MatchSymbol
from ScriptingLanguage.Matchers.Matchers import MatchWhitespace, MatchIdentifier
from ScriptingLanguage.Parser.AstNode import ExpressionNode
from ScriptingLanguage.Parser.Parser import Parser
from ScriptingLanguage.Visitors.ExpressionVisitor import visit_expression

__author__ = 'chronium'

input_string = open('Examples/test.crs').read()

symbols = ['=', ' ', ':=', '-', '+', '.', '*', '/', '%', '(', ')', '->']
keywords = ['func']

if __name__ == '__main__':
    matchers = [MatchWhitespace(), MatchNumber(), MatchSymbol(symbols), MatchKeyword(keywords), MatchIdentifier(symbols)]
    while True:
        code = input('>>>') + '\n'
        lexer = Lexer(code, matchers)
        parser = Parser(lexer)
        node = parser.parse_line()
        print(node.visit())
