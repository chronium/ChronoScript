from ScriptingLanguage.Lexer.Tokenizer import TokenizableBaseStream

__author__ = 'chronium'

class Memo:
    def __init__(self, ast, next_index):
        self.ast = ast
        self.next_index = next_index

class ParsableTokenStream(TokenizableBaseStream):
    cached_ast = {}

    def __init__(self, source):
        super(ParsableTokenStream, self).__init__(list(source.lex()))

    def take(self):
        raise StandardError()

    def alt(self, func):
        self.take_snapshot()
        found = False

        try:
            current_index = self.index
            ast = func()

            if ast is not None:
                found = True
                self.cached_ast[current_index] = Memo(ast, self.index)
        except StandardError:
            pass

        self.rollback_snapshot()

        return found

    def capture(self, func):
        if self.alt(func):
            return self.get(func)
        return None

    def get(self, func):
        try:
            memo = self.cached_ast[self.index]
        except KeyError:
            memo = func()

        self.index = memo.next_index

        return memo.ast
