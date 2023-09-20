def todo_checker(text):
    if isinstance(text, str):
        if '#TODO' in text:
            return True
        else:
            return False
    else:
        raise Exception("Input must be a string")