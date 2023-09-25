from lib._08_challenge_todo_list import *
from lib._08_challenge_todo import *

# Given a todo input, adds to list as incomplete
# and is returned by self.incomplete() method
def test_todo_item_added_to_list_and_returned():
    todo_list = TodoList()
    todo_list.add('A task to be completed')
    assert todo_list.incomplete() == ['A task to be completed']

# Given multiple todo inputs, adds all to list
# and all are returned in a list by self.incomplete() method
def test_MULTIPLE_todo_itemS_added_to_list_and_returned():
    todo_list = TodoList()
    todo_list.add('A task to be completed')
    todo_list.add('A second task')
    todo_list.add('A third task to be completed')
    assert todo_list.incomplete() == ['A task to be completed', 'A second task', 'A third task to be completed']

# With multiple complete and incomplete todos,
# incomplete() and complete() return the correct lists
def test_incomplete_and_complete_methods_return_correct():
    todo_list = TodoList()
    todo_list.add('A task to be completed')
    todo_list.add('A second task')
    todo_list.add('A third task to be completed')
    task_to_mark_complete = 'A second task'
    for todo in todo_list.list:
            if todo.task == task_to_mark_complete:
                todo.mark_complete()
    assert todo_list.incomplete() == ['A task to be completed', 'A third task to be completed']
    assert todo_list.complete() == ['A second task']

# give_up method marks all items in todo list as complete
# and all complete items are returned by complete() method
def test_give_up_marks_all_todos_complete():
    todo_list = TodoList()
    todo_list.add('A task to be completed')
    todo_list.add('A second task')
    todo_list.add('A third task to be completed')
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == ['A task to be completed', 'A second task', 'A third task to be completed']

