from lib._03_challenge_todo_checker import todo_checker
import pytest

#Given an empty string test returns False
def test_empty_string_returns_false():
    assert todo_checker('') == False

#Given a string not containing '#TODO' returns False
def test_given_string_not_contianing_todo_returns_false():
    assert todo_checker('This is a string') == False

# Given a string containing '#TODO' returns True
def test_given_string_containing_todo_at_start_returns_true():
    assert todo_checker('#TODO This is an item being added to my schedule') == True

#Given a string including '#TODO' not at the start returns True
def test_string_containing_todo_at_end_returns_true():
    assert todo_checker("This is a string #TODO") == True

# Given a string including '#TODO' somewhere in the middle of the string returns True
def test_string_containing_todo_not_at_start_or_end_returns_true():
    assert todo_checker("This string contains #TODO but not at the start or end") == True

# Given a non-string input returns a suitable error message
def test_nonstring_input_returns_error():
    with pytest.raises(Exception) as e:
        todo_checker(123)
    error_message = str(e.value)
    assert  error_message == "Input must be a string"