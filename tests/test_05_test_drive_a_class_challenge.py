from lib._05_test_drive_a_class_challenge import GrammarStats
import pytest

# self.check returns true if passed a string with capital letter 
# at the start and sentence ending punctuation at the end
def test_check_returns_true_if_correct_sentence():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("This is a correct sentence.") == True
    assert grammar_stats.check("Another correct sentence!") == True
    assert grammar_stats.check("Yet another correct sentence, or is it?") == True

# self.check return False if passed an incorrect sentence
def test_check_returns_false_if_incorrect_sentence():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('this is not a correct sentence.') == False
    assert grammar_stats.check("This sentence is also incorrect") == False
    assert grammar_stats.check("also an incorrect sentence!") == False

# self.check returns an error if text arg is int
def test_check_returns_error_message_if_passed_integer_arg():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(123)
    error_message = str(e.value)
    assert error_message == 'Input must be a string!'

# self.check returns an error if text arg is list
def test_check_returns_error_message_if_passed_list_arg():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(['A', 'list', 'of', 'words.'])
    error_message = str(e.value)
    assert error_message == 'Input must be a string!'

# self.percentage_good returns 100 if all self.checks have returned true
def test_percentage_good_returns_100_if_all_checks_true():
    grammar_stats = GrammarStats()
    grammar_stats.check('This is a valid sentence.')
    grammar_stats.check('So is this one!')
    grammar_stats.check('And this one.')
    grammar_stats.check("Finally, so is this one. Or is it?")
    assert grammar_stats.percentage_good() == 100

#  self.percentage_good returns 50 if half of the checks returned true
def test_percentage_good_returns_50_if_half_checks_true():
    grammar_stats = GrammarStats()
    grammar_stats.check('This is a valid sentence.')
    grammar_stats.check('This one is not')
    grammar_stats.check('nor is this!')
    grammar_stats.check("But this one is valid!")
    assert grammar_stats.percentage_good() == 50

#  self.percentage_good returns 25 if a quarter of the checks returned true
def test_percentage_good_returns_25_if_quarter_checks_true():
    grammar_stats = GrammarStats()
    grammar_stats.check('This is a valid sentence.')
    grammar_stats.check('This one is not')
    grammar_stats.check('nor is this!')
    grammar_stats.check("and neither is this one")
    assert grammar_stats.percentage_good() == 25