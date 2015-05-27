from ScriptingLanguage.Lexer.Lexer import Lexer
from ScriptingLanguage.Parser.Parser import Parser
from main import matchers

__author__ = 'chronium'

def parse_line_visit(line):
    lexer = Lexer(line, matchers)
    parser = Parser()
    node, indents = parser.parse_immediate(lexer)
    return node.visit()

def parse_block(block):
    lexer = Lexer(block, matchers)
    parser = Parser()
    return parser.parse(lexer)

def test_simple_math():
    assert parse_line_visit('1 + 2\n') == 3
def test_order_operations():
    assert parse_line_visit('1 + 2 * 3\n') == 7
def test_variable():
    parse_line_visit('x = 1 + 2')
    assert parse_line_visit('1 * 2 - x * 3\n') == -7
