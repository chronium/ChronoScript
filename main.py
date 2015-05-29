from ScriptingLanguage.Lexer.Lexer import Lexer
from ScriptingLanguage.Matchers.MatchKeyword import MatchKeyword
from ScriptingLanguage.Matchers.MatchNumber import MatchNumber
from ScriptingLanguage.Matchers.MatchSymbol import MatchSymbol
from ScriptingLanguage.Matchers.Matchers import MatchWhitespace, MatchIdentifier
from ScriptingLanguage.Interpreter import Scoping, Interpreter

import sys
from ScriptingLanguage.Parser.Parser import Parser

__author__ = 'chronium'

input_string = open('Examples/test.crs').read()

symbols = ['=', ' ', ':=', '-', '+', '.', '*', '/', '%', '(', ')', '->']
keywords = ['func']
matchers = [MatchWhitespace(), MatchNumber(), MatchSymbol(symbols), MatchKeyword(keywords), MatchIdentifier(symbols)]
scoping = Scoping()
scoping.add_scope_unindexed()
parser = Parser()

def exit_func():
    print('Goodbye!')
    exit()
Interpreter().add_function('exit', exit_func)

def return_five():
    return 5
Interpreter().add_function('ret5', return_five)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        lexer = Lexer(input_string, matchers)
        program = parser.parse(lexer)
        print(program)
    else:
        while True:
            code = input('>>>') + '\n'
            if code.startswith('func'):
                temp = input('...')
                while temp.strip():
                    code += temp + '\n'
                    temp = input('...')
                lexer = Lexer(code, matchers)
                program = parser.parse(lexer)
                print(program)
            else:
                lexer = Lexer(code, matchers)
                node = parser.parse_immediate(lexer)
                res = node.visit()
                if res is not None:
                    print(res)
