def string_modifier(string):
    special_characters = ['.', '!', '?']
    if isinstance(string, str):
        if string[-1] in special_characters and string[0].isupper():
            return True
        else:
            return False
    else:
        raise Exception('Input must be a string!')
