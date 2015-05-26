from ScriptingLanguage.Lexer.Matcher import MatcherBase
from ScriptingLanguage.Tokens import Keyword

__author__ = 'chronium'

class MatchKeyword(MatcherBase):
    def __init__(self, keywords):
        keywords.sort(key=len, reverse=True)
        self.symbols = keywords

    def is_match_impl(self, tokenizer):
        for symbol in self.symbols:
            tok = ''.join(tokenizer.peek_multiple(length=len(symbol)))
            if tok == symbol:
                tokenizer.index += len(symbol)
                return Keyword(tok)
        return None
