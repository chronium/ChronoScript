__author__ = 'chronium'

class Ast:
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def visit(self, func):
        func(self)

    def __str__(self):
        try:
            if isinstance(self.value, str):
                raise TypeError
            return '%s(%s)' % (self.name, ', '.join(map(str, self.value)))
        except TypeError:
            return '%s(%s)' % (self.name, str(self.value))

class Program:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        return 'Program:[%s]' % ', '.join(map(str, self.nodes))

class NumberNode(Ast):
    def __init__(self, value):
        super(NumberNode, self).__init__(value, 'Number')

    def visit(self, func):
        super(NumberNode, self).visit(func)

class ExpressionNode(Ast):
    def __init__(self, value):
        super(ExpressionNode, self).__init__(value, 'Expression')

class FunctionCallNode(Ast):
    def __init__(self, value):
        super(FunctionCallNode, self).__init__(value, 'Function Call')

class FunctionDefNode(Ast):
    def __init__(self, value):
        super(FunctionDefNode, self).__init__(value, 'Function Def')

class AssignmentNode(Ast):
    def __init__(self, value):
        super(AssignmentNode, self).__init__(value, 'Assignment')

    def __str__(self):
        return "%s('%s', %s)" % (self.name, str(self.value[0]), str(self.value[1]))