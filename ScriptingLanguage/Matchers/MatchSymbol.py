from ScriptingLanguage.Lexer.Matcher import MatcherBase
from ScriptingLanguage.Tokens import Symbol

__author__ = 'chronium'

class MatchSymbol(MatcherBase):
    def __init__(self, symbols):
        symbols.sort(key=len, reverse=True)
        self.symbols = symbols

    def is_match_impl(self, tokenizer):
        val = ""
        for symbol in self.symbols:
            for c in list(symbol):
                if tokenizer.current() == c:
                    val += tokenizer.read()
            if val and (val in self.symbols):
                return Symbol(val)
        return None
