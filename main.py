from ScriptingLanguage.Lexer.Tokenizer import Tokenizer
from ScriptingLanguage.Matchers.MatchSymbol import MatchSymbol
from ScriptingLanguage.Matchers.Matchers import MatchWhitespace, MatchIdentifier

__author__ = 'chronium'

input_string = 'test :='

symbols = ['=', ' ', ':=']

if __name__ == '__main__':
    tokenizer = Tokenizer(input_string)
    matchers = [MatchWhitespace(), MatchSymbol(symbols), MatchIdentifier(symbols)]
    tokens = []
    while not tokenizer.eof(0):
        for matcher in matchers:
            match = matcher.is_match(tokenizer)

            if match and match.value is not ' ':
                tokens.append(match)

    print("Input string:'{}' \nTokens:".format(input_string))
    for token in tokens:
        print(token)
