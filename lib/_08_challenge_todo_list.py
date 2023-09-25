from lib._08_challenge_todo import *

class TodoList:
    def __init__(self):
        self.list = []

    def add(self, todo):
        self.list.append(Todo(todo))

    def incomplete(self):
        if self.list == []:
            raise Exception("There are no entries in list.")
        return [item.task for item in self.list if item.complete == False]

    def complete(self):
        if self.list == []:
            raise Exception("There are no entries in list.")
        return [item.task for item in self.list if item.complete == True]

    def give_up(self):
        for todo in self.list:
            todo.mark_complete()