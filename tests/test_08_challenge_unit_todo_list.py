from lib._08_challenge_todo_list import *
import pytest

# Initially incomplete() method returns an error
def test_incomplete_returns_error_if_list_empty():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.incomplete()
    assert str(e.value) == "There are no entries in list."

# Initially complete() method returns an error
def test_omplete_returns_error_if_list_empty():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.complete()
    assert str(e.value) == "There are no entries in list."