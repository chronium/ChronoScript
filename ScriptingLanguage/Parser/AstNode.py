__author__ = 'chronium'

class Ast(object):
    def visit(self, func):
        func(self)

class Test(Ast):
    def visit(self, func):
        super(Test, self).visit(func)
