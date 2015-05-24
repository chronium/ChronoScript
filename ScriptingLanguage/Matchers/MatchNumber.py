from ScriptingLanguage.Lexer.Matcher import MatcherBase
from ScriptingLanguage.Tokens import NumberLiteral

__author__ = 'chronium'

class MatchNumber(MatcherBase):
    def is_match_impl(self, tokenizer):
        accum = ''
        current = tokenizer.current
        read = tokenizer.read

        accum += self.numbers(current, read)

        if current() == '.':
            accum += read()
            accum += self.numbers(current, read)

        if len(accum) > 0 and accum != '.':
            try:
                return NumberLiteral(int(accum))
            except ValueError:
                return NumberLiteral(float(accum))
        return None

    def numbers(self, current, read):
        accum = ''
        while current() is not None and current() != '.' and current().isdigit():
            accum += read()
        return accum
