from lib._08_challenge_todo import *

# Initializes with correct task and complete properties
def test_initializes_with_correct_properties():
    todo = Todo("Here is a task")
    assert todo.task == "Here is a task"
    assert todo.complete == False

# Mark complete method correctly changes self.complete value
def test_mark_complete_sets_complete_to_True():
    todo = Todo("Some task.")
    todo.mark_complete()
    assert todo.complete == True