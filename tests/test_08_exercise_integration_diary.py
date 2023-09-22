from lib._08_exercise_diary import *
from lib._08_exercise_diary_entry import *

# Given a diary entry to add
# Adds entry to list and returns the entry
def test_given_one_entry_adds_and_returns_entry_list():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'Contents1')
    diary.add(entry_1)
    assert diary.all() == [entry_1]

# With multiple entries added
# Returns a list including all diary entries
def test_given_multiple_entries_adds_and_returns_entry_list():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'Contents1')
    entry_2 = DiaryEntry('Title2', 'Contents2')
    entry_3 = DiaryEntry('Title3', 'Contents3')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.all() == [entry_1, entry_2, entry_3]

# With multiple entries added
# Returns integer representing number of words in all diary entries
def test_returns_number_of_words_in_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'These are the contents of entry one')
    entry_2 = DiaryEntry('Title2', 'These are the contents of entry two')
    entry_3 = DiaryEntry('Title3', 'These are the contents of entry three')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.count_words() == 21

# With multiple entries added and given a wpm value
# Correctly calculates and returns the reading time for all entries
def test_given_wpm_returns_minutes_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'These are the contents of entry one')
    entry_2 = DiaryEntry('Title2', 'These are the contents of entry two')
    entry_3 = DiaryEntry('Title3', 'These are the contents of entry three')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.reading_time(7) == 3

# With multiple entries added and given a wpm value and a minutes value
# Returns the DiaryEntry instance that the user could read without going over
# the number of minutes
def test_returns_best_entry_to_read_given_wpm_and_minutes():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'These are the contents of entry one') #7
    entry_2 = DiaryEntry('Title2', 'These are the contents of entry two which are slightly longer than entry one')#14
    entry_3 = DiaryEntry('Title3', 'These are the contents of entry three which are even longer still compared to both entry one and two')#19
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(7,1) == ['Title1', 'These are the contents of entry one']
    assert diary.find_best_entry_for_reading_time(7,2) == ['Title2', 'These are the contents of entry two which are slightly longer than entry one']
    assert diary.find_best_entry_for_reading_time(7,3) == ['Title3', 'These are the contents of entry three which are even longer still compared to both entry one and two']