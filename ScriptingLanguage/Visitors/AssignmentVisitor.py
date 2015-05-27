from ScriptingLanguage.Interpreter import global_dict

__author__ = 'chronium'

def visit_assignment(assignment):
    global_dict[assignment.value[0]] = assignment.value[1].visit()
    return '[{}] = {}'.format(assignment.value[0], global_dict[assignment.value[0]])
