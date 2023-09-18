from lib.make_snippet import make_snippet


# A function called make_snippet that takes a string as an 
# argument and returns the first five words and then a '...' 
# if there are more than that.

def test_given_empty_string_returns_empty_string():
    assert make_snippet('') == ''

def test_returns_string_less_than_5_words():
    assert make_snippet('short string') == 'short string'

def test_returns_truncated_if_longer_than_5_words():
    assert make_snippet('This is a much longer string than the one before') == "This is a much longer ..."

def test_if_input_is_not_a_string():
    assert make_snippet(12345678) == 'Not a string'