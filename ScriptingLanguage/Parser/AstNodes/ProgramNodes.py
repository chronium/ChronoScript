from ScriptingLanguage.Parser.AstNode import Ast

__author__ = 'chronium'

class Program:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        return 'Program:[%s]' % ', '.join(map(str, self.nodes))

class LineNode(Ast):
    def __init__(self, value):
        super(LineNode, self).__init__(value, 'Line')
