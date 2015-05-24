from ScriptingLanguage.Lexer.Lexer import Lexer
from ScriptingLanguage.Matchers.MatchSymbol import MatchSymbol
from ScriptingLanguage.Matchers.Matchers import MatchWhitespace, MatchIdentifier
from ScriptingLanguage.Parser.Parser import Parser

__author__ = 'chronium'

input_string = ':=:='

symbols = ['=', ' ', ':=']

if __name__ == '__main__':
    matchers = [MatchWhitespace(), MatchSymbol(symbols), MatchIdentifier(symbols)]
    lexer = Lexer(input_string, matchers)
    parser = Parser(lexer)

    print("Input string:'{}' \nTokens:".format(input_string))
    for token in parser.parse():
        print(token)
