from ScriptingLanguage.Interpreter import global_dict

__author__ = 'chronium'

def visit_func_call(function_call):
    try:
        return global_dict['__func__' + function_call.value]()
    except KeyError:
        print('Function [{}] undefined'.format(function_call.value))
