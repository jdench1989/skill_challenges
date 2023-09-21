Reading Time Estimate Function Design Recipe

1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def reading_time(text):
    # Provides estimated reading time of the text base don reading speed of 200 words per minute

    Parameters: (list all parameters and their types)
        mixed_words: a long string of words

    Returns: (state the return value and its type)
        string in the format hh:mm:ss

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# given a string of 0 words it returns a result of 0 seconds
reading_time('0 words string) => 0

# given a string of 200 words it returns a result of 1 minute
reading_time('200 words string) => 1

# given a string of 2000 words it returns a result of 10 minutes
reading_time('2000 words string) => 10

# given a string of 100 words it returns a result of 30 seconds
reading_time('100 words string) => 0.5

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.



