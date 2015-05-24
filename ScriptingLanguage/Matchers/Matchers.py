from ScriptingLanguage.Lexer.Matcher import MatcherBase
from ScriptingLanguage.Tokens import Whitespace, Identifier

__author__ = 'chronium'

class MatchWhitespace(MatcherBase):
    def is_match_impl(self, tokenizer):
        found_white_space = False

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
        accum = ""

        if tokenizer.current() == "'":
            return None

        read = tokenizer.read

        while not tokenizer.end() and tokenizer.current().strip() and tokenizer.current().strip() not in self.symbols:
            accum += read()

        if len(accum) > 0:
            return Identifier(accum)
        return None
