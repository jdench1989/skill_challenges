class TaskTracker():

    def __init__(self):
        self.task_list = []

    def add(self,task):
        if isinstance(task,str):
            if '#TODO' in task:
                self.task_list.append(task)
        else:
            raise Exception("Input must be a string")
        
    def complete(self,task):
        if task in self.task_list:
            self.task_list.remove(task)
        

    def list_tasks(self):
        return self.task_list
