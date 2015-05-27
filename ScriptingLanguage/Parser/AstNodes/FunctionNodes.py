from ScriptingLanguage.Parser.AstNode import Ast
from ScriptingLanguage.Visitors.FunctionVisitor import visit_func_call

__author__ = 'chronium'

class FunctionCallNode(Ast):
    def __init__(self, value):
        super(FunctionCallNode, self).__init__(value, 'Function Call')

    def visit(self):
        return visit_func_call(self)
