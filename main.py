from ScriptingLanguage.Lexer.Lexer import Lexer, UnknownTokenException
from ScriptingLanguage.Matchers.MatchKeyword import MatchKeyword
from ScriptingLanguage.Matchers.MatchNumber import MatchNumber
from ScriptingLanguage.Matchers.MatchSymbol import MatchSymbol
from ScriptingLanguage.Matchers.Matchers import MatchWhitespace, MatchIdentifier
from ScriptingLanguage.Parser.Parser import Parser

__author__ = 'chronium'

input_string = open('Examples/test.crs').read()

symbols = ['=', ' ', ':=', '-', '+', '.', '*', '/', '%', '(', ')', '->']
keywords = ['func']

if __name__ == '__main__':
    matchers = [MatchWhitespace(), MatchNumber(), MatchSymbol(symbols), MatchKeyword(keywords), MatchIdentifier(symbols)]
    lexer = Lexer(input_string, matchers)

    print("Input string:'{}' \nTokens:".format(input_string))
    try:
        for token in lexer.lex():
            print(token)
    except UnknownTokenException as e:
        print(e)

    print('\nAST:')
    parser = Parser(Lexer(input_string, matchers))
    print(parser.parse())
