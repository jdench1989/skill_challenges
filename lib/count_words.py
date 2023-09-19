# Design
# A function called count_words that takes a string as an 
# argument and returns the number of words in that string.

def count_words(string):
    if isinstance(string, str):
        words = string.split()
        return len(words)
    else:
        raise Exception("Not a string! Please enter a string of words.")
