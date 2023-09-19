def make_snippet(string):
    if isinstance(string, str):
        if len(string.split()) < 5:
            return string
        else:
            words = string.split()
            result = f"{' '.join(words[0:5])} ..."
            return result
    else:
        return 'Not a string'