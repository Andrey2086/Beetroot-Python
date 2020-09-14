# Task 2
#
# Write a program that reads in a sequence of characters, and determines
# whether it's parentheses, braces, and curly brackets are "balanced."

class Stack():
    def __init__(self):
        self.__stek_list = []

    def get_show(self): #Проверка списка
        return self.__stek_list[-1] if self.__stek_list else None

    def get_pop(self): # Удаляет
        if self.get_show() is not None:
            return self.__stek_list.pop()
        else:
            return None

    def push(self, object):  # Добавляет
        self.__stek_list.append(object)

def check_balanced(val: str) ->bool:
    item_stack = Stack()
    for char in val:
        if char == '(' or char == '[' or char == '{':
            item_stack.push(char)
        elif char == ')' or char == ']' or char == '}':
            if item_stack.get_show() == None:
                return False
            item_stack.get_pop()
    if item_stack.get_show() == None:
        return True
    return False




print(check_balanced("{[()]}"))
print(check_balanced("[({}]"))



