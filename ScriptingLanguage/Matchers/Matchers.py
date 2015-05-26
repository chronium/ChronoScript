from ScriptingLanguage.Lexer.Matcher import MatcherBase
from ScriptingLanguage.Tokens import Whitespace, Identifier, Indent, NewLine

__author__ = 'chronium'

class MatchWhitespace(MatcherBase):
    def is_match_impl(self, tokenizer):
        found_white_space = False

        if ''.join(tokenizer.peek_multiple(4)) == '    ':
            tokenizer.index += 4
            return Indent()

        if tokenizer.current() == '\n':
            tokenizer.consume()
            return NewLine()

        while not tokenizer.end() and (not tokenizer.current().strip() or tokenizer.current() == '\r'):
            found_white_space = True
            tokenizer.consume()

        if found_white_space:
            return Whitespace()

        return None

class MatchIdentifier(MatcherBase):
    def __init__(self, symbols):
        self.symbols = symbols

    def is_match_impl(self, tokenizer):
        accum = ''
        read = tokenizer.read
        current = tokenizer.current

        if current() == '_':
            pass
        elif current() in self.symbols or current().isdigit():
            return None

        while not tokenizer.end() and current().strip() and current().strip() not in self.symbols:
            accum += read()

        if len(accum) > 0:
            return Identifier(accum)
        return None
