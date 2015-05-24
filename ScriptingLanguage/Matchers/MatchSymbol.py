from ScriptingLanguage.Lexer.Matcher import MatcherBase
from ScriptingLanguage.Tokens import Symbol

__author__ = 'chronium'

class MatchSymbol(MatcherBase):
    def __init__(self, symbols):
        symbols.sort(key=len, reverse=True)
        self.symbols = symbols

    def is_match_impl(self, tokenizer):
        for symbol in self.symbols:
            tok = ''.join(tokenizer.peek_multiple(length=len(symbol)))
            if tok == symbol:
                tokenizer.index += len(symbol)
                return Symbol(tok)
        return None
