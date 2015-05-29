from ScriptingLanguage.Lexer.Tokenizer import Stack

__author__ = 'chronium'

class Scope:
    def __init__(self, name):
        self.name = name
        self.items = {}

class UndefinedVariable(Exception):
    pass

class Scoping:
    scopes = Stack()
    index = 0

    def add_scope_unindexed(self):
        self.scopes.push(Scope(self.get_full_name() + '_' + str(self.index)))
        self.index += 1

    def add_function(self, name, function):
        self.scopes.peek().items['__func__' + name] = function

    def add_variable(self, name, value):
        self.scopes.peek().items['__var__' + name] = value

    def get_full_name(self):
        result = ''
        for scope in self.scopes.items:
            result += scope.name
        return result

    def get_function(self, name):
        for scope in self.scopes.items:
            if '__func__' + name in scope.items:
                return scope.items['__func__' + name]
        return None

    def get_variable(self, name):
        for scope in self.scopes.items:
            if '__var__' + name in scope.items:
                return scope.items['__var__' + name]
        raise UndefinedVariable

class Interpreter:
    instance = None

    def __init__(self):
        if not Interpreter.instance:
            self.instance = self.__Interpreter()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    class __Interpreter:
        scoping = Scoping()

        def add_function(self, name, func):
            self.scoping.add_function(name, func)

        def get_function(self, name):
            return self.scoping.get_function(name)

        def add_variable(self, name, value):
            self.scoping.add_variable(name, value)

        def get_variable(self, name):
            return self.scoping.get_variable(name)
