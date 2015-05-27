from ScriptingLanguage.Interpreter import global_dict

__author__ = 'chronium'

def visit_expression(expression):
    left = expression.value[0].visit()
    if expression.value[1]:
        right = expression.value[2].visit()
        try:
            return {
                '+': left + right,
                '-': left - right,
                '*': left * right,
                '/': left / right,
                '%': left % right
            }.get(expression.value[1], 0)
        except ZeroDivisionError:
            return 0
    return left

def visit_var(identifier):
    try:
        return global_dict[identifier.value]
    except KeyError:
        print('[{}] is undefined'.format(identifier.value))
        return 0

def visit_number(number):
    return number.value
