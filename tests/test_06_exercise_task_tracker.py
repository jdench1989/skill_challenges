from lib._06_exercise_task_tracker import TaskTracker
import pytest

def test_add_given_TODO_task_adds_to_task_list():
    task_tracker = TaskTracker()
    task_tracker.add("#TODO: This is the first task.")
    assert task_tracker.list_tasks() == ["#TODO: This is the first task."]

def test_add_given_notTODO_task_it_is_ignored():
    task_tracker = TaskTracker()
    task_tracker.add("This is the first task.")
    assert task_tracker.list_tasks() == []

def test_add_given_two_tasks_both_are_added_and_first_is_preserved():
    task_tracker = TaskTracker()
    task_tracker.add('#TODO: This is the first task')
    task_tracker.add('#TODO: This is the second task')
    assert task_tracker.list_tasks() == [
    '#TODO: This is the first task', 
    '#TODO: This is the second task']

def test_add_given_empty_string_is_ignored():
    task_tracker = TaskTracker()
    task_tracker.add('')
    assert task_tracker.list_tasks() == []

def test_add_given_nonstring_input_returns_error():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.add(123)
    error_message = str(e.value)
    error_message == "Input must be a string"

def test_complete_removes_task_from_list_if_task_exists():
    task_tracker = TaskTracker()
    task_tracker.add('#TODO: This is the first task')
    task_tracker.add('#TODO: This is the second task')
    task_tracker.complete('#TODO: This is the first task')
    assert task_tracker.list_tasks() == ['#TODO: This is the second task']
