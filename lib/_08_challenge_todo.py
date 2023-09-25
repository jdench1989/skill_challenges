class Todo:

    def __init__(self, task):
        self.task = str(task)
        self.complete = False

    def mark_complete(self):
        self.complete = True