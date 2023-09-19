from lib.count_words import *
import pytest

def test_empty_string():
    assert count_words('') == 0

def test_one_word_string():
    assert count_words('one') == 1

def test_two_word_string():
    assert count_words('two words') == 2

def test_longer_string():
    assert count_words ('this is a longer string') == 5

def test_error_if_number_entered():
    with pytest.raises(Exception) as e:
        count_words(12345)
    error_message = str(e.value)
    assert error_message == "Not a string! Please enter a string of words."
    
def test_error_if_list_entered():
    with pytest.raises(Exception) as e:
        count_words(['a', 'list', 'of', 'strings'])
    error_message = str(e.value)
    assert error_message == "Not a string! Please enter a string of words."