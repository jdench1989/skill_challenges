from lib._07_debugging_2_exercise_vowel_remover import *

# A colleague has done a code review and has advised that the tests should cover all the vowels.
# Add a new unit test to check that the program can remove all the vowels from "aeiou", 
# returning an empty string, "". If there are any problems reported by pytest after adding this new test, 
# use the debugger to look into vowel_remover.py to discover where the problem is and make any necessary changes.

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_removes_all_vowels():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "" #On testing returns 'eo'. Time to run the code through the debugger.

#Bug fixed. see code for explanation