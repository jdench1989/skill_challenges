from lib._08_exercise_diary import *
import pytest

# Initially returns empty entry list
def test_initially_returns_empty_list():
    diary = Diary()
    assert diary.all() == []

# Initially word_count is 0
def test_initial_word_count_is_0():
    diary = Diary()
    assert diary.count_words() == 0

#Initially reading_time should raise an error
def test_initially_reading_count_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(3)
    assert str(e.value) == "No entries added yet"

# Initially find_best_entry_for_reading_time raises error
def test_initially_find_best_entry_for_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(3, 5)
    assert str(e.value) == "No entries added yet"