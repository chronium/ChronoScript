from ScriptingLanguage.Visitors.AssignmentVisitor import visit_assignment
from ScriptingLanguage.Visitors.ExpressionVisitor import visit_expression, visit_number, visit_var

__author__ = 'chronium'

class Ast:
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def visit(self):
        pass

    def __str__(self):
        try:
            if isinstance(self.value, str):
                raise TypeError
            return '%s(%s)' % (self.name, ', '.join(map(str, self.value)))
        except TypeError:
            return '%s(%s)' % (self.name, str(self.value))

class NumberNode(Ast):
    def __init__(self, value):
        super(NumberNode, self).__init__(value, 'Number')

    def visit(self):
        return visit_number(self)

class ExpressionNode(Ast):
    def __init__(self, value):
        super(ExpressionNode, self).__init__(value, 'Expression')

    def visit(self):
        return visit_expression(self)

class FunctionDefNode(Ast):
    def __init__(self, value):
        super(FunctionDefNode, self).__init__(value, 'Function Def')

class AssignmentNode(Ast):
    def __init__(self, value):
        super(AssignmentNode, self).__init__(value, 'Assignment')

    def __str__(self):
        return "%s('%s', %s)" % (self.name, str(self.value[0]), str(self.value[1]))

    def visit(self):
        return visit_assignment(self)

class VariableNode(Ast):
    def __init__(self, value):
        super(VariableNode, self).__init__(value, 'Variable')

    def visit(self):
        return visit_var(self)
