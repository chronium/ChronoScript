from main import interpreter

__author__ = 'chronium'

def visit_assignment(assignment):
    interpreter.add_variable(assignment.value[0], assignment.value[1].visit())
    return '[{}] = {}'.format(assignment.value[0], interpreter.get_variable(assignment.value[0]))
