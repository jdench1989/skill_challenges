TODO Checker Function Design Recipe

1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def todo_checker(text):
    Checks if the string contains the string "#TODO"

    Parameters: (list all parameters and their types)
        text: a string of words

    Returns: (state the return value and its type)
        Boolean: True if "#TODO" in text, false otherwise

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects

    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

# Given an empty string test returns False
def test_empty_string_returns_false() ==> False

# Given a string not containing '#TODO' returns False
def test_string_not_containing_todo_returns_false() ==> False

# Given a string containing '#TODO' returns True
def test_string_containing_todo_returns_true() ==> True

# Given a non-string input returns a suitable error message
def test_nonstring_input_returns_error

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
Ensure all test function names are unique, otherwise pytest will ignore them!

