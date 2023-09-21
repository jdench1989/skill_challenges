Task TrackerClass Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class TaskTracker():

    def __init__(self):
        # ToDo list 

    def add(self, task):
        #Add task to ToDO list if it contains the phrase "TODO:"

    def complete(self, task):
        #remove task from ToDo list

    def list_tasks(self):
        #return currently active tasks

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# given a task including the phrase "TODO:"
# adds the task to the ToDo list 

task_tracker = TaskTracker()
task_tracker.add('TODO: This is the first task')
task_tracker.list_tasks() ==> ['TODO: This is the first task']

# given a string that does not include the phrase "TODO:"
# string is ignored

task_tracker = TaskTracker()
task_tracker.add('This is the first task')
task_tracker.list_tasks() ==> []

# given a second task 
# task as appended to todo list without removing first entry

task_tracker = TaskTracker()
task_tracker.add('#TODO: This is the first task')
task_tracker.add('#TODO: This is the second task')
task_tracker.list_tasks() ==> [
    '#TODO: This is the first task', 
    '#TODO: This is the second task']

# empty string is ignored

task_tracker = TaskTracker()
task_tracker.add('')
task_tracker.list_tasks() ==> []

# non-string input returns error message

task_tracker = TaskTracker()
task_tracker.add(123)
task_tracker.list_tasks() ==> "Input must be a string"

# given an existing task
# self.complete removes the task from the list

task_tracker = TaskTracker()
task_tracker.add('#TODO: This is the first task')
task_tracker.add('#TODO: This is the second task')
task_tracker.complete('#TODO: This is the first task')
task_tracker.list_tasks() ==> ['#TODO: This is the second task']

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

