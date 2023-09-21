{{PROBLEM}} Function Design Recipe

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

