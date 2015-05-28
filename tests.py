from ScriptingLanguage.Lexer.Lexer import Lexer
from ScriptingLanguage.Parser.Parser import Parser
from main import matchers

__author__ = 'chronium'

def parse_line_visit(line):
    lexer = Lexer(line, matchers)
    parser = Parser()
    node = parser.parse_immediate(lexer)
    return node.visit()

def parse_block(code):
    lexer = Lexer(code, matchers)
    parser = Parser()
    return parser.parse(lexer)

def test_simple_math():
    assert parse_line_visit('1 + 2\n') == 3
def test_order_operations():
    assert parse_line_visit('1 + 2 * 3\n') == 7
def test_variable_undefined():
    assert parse_line_visit('1 * 2 - x * 3\n') == 0
def test_variable():
    parse_line_visit('x = 1 + 2')
    assert parse_line_visit('1 * 2 - x * 3\n') == -7
def test_function():
    assert parse_line_visit('7 + ret5()') == 12
def test_function_def():
    code = "func test()\n" \
           "    x = 1 + 2"
    expected = "Program:[Body(Function(Function Def(test), " \
               "Body(Assignment('x', Expression(Number(1), +, Number(2))))))]"
    result = parse_block(code)
    assert str(result) == expected
