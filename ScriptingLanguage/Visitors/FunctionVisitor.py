from ScriptingLanguage.Interpreter import Interpreter

__author__ = 'chronium'

def visit_func_call(function_call):
    try:
        return Interpreter().get_function(function_call.value)()
    except KeyError:
        print('Function [{}] undefined'.format(function_call.value))
