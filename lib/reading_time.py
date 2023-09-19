def reading_time(string):
    if type(string) == str:
        word_list = string.split()
        return len(word_list)/200
    else: 
        raise Exception("This is not a string")