from ScriptingLanguage.Lexer.Tokenizer import Tokenizer
from ScriptingLanguage.Tokens import EOF, Whitespace

__author__ = 'chronium'

class UnknownTokenException(Exception):
    pass

class Lexer(object):
    def __init__(self, source, matchers):
        self.tokenizer = Tokenizer(source)
        self.matchers = matchers

    def lex(self):
        current = self.next()

        while current and not isinstance(current, EOF):
            if not isinstance(current, Whitespace):
                yield current
            current = self.next()
        yield EOF()

    def next(self):
        if self.tokenizer.end():
            return EOF()

        for match in self.matchers:
            token = match.is_match(self.tokenizer)
            if token:
                return token

        raise UnknownTokenException("Unexpected character:'%s'" % self.tokenizer.current())
