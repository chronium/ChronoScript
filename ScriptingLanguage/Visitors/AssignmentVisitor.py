from ScriptingLanguage import Interpreter

__author__ = 'chronium'

def visit_assignment(assignment):
    Interpreter.add_variable(assignment.value[0], assignment.value[1].visit())
    return '[{}] = {}'.format(assignment.value[0], Interpreter.get_variable(assignment.value[0]))
