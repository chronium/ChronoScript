__author__ = 'chronium'

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class TokenizableBaseStream(object):
    def __init__(self, source):
        self.index = 0
        self.items = source
        self.snapshot_indices = Stack()

    def eof(self, lookahead):
        if self.index + lookahead >= len(self.items):
            return True
        return False

    def end(self):
        return self.eof(0)

    def current(self):
        if self.eof(0):
            return None
        return self.items[self.index]

    def consume(self):
        self.index += 1

    def peek(self, lookahead):
        if self.eof(lookahead):
            return None
        return self.items[self.index + lookahead]

    def read(self):
        tok = self.peek(0)
        self.consume()
        return tok

    def take_snapshot(self):
        self.snapshot_indices.push(self.index)

    def rollback_snapshot(self):
        self.index = self.snapshot_indices.pop()

    def commit_snapshot(self):
        self.snapshot_indices.pop()

class Tokenizer(TokenizableBaseStream):
    def __init__(self, source):
        super(Tokenizer, self).__init__(list(source))
