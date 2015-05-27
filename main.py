from ScriptingLanguage.Interpreter import global_dict
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

def exit_func():
    print('Goodbye!')
    exit()
global_dict['__func__exit'] = exit_func

def return_five():
    return 5
global_dict['__func__ret5'] = return_five

if __name__ == '__main__':
    matchers = [MatchWhitespace(), MatchNumber(), MatchSymbol(symbols), MatchKeyword(keywords), MatchIdentifier(symbols)]
    parser = Parser()
    while True:
        code = input('>>>') + '\n'
        lexer = Lexer(code, matchers)
        node, indents = parser.parse_immediate(lexer)
        res = node.visit()
        if res is not None:
            print(res)
