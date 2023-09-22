class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        vowels_removed = "" #Created after fixing the bug
        # while i < len(self.text):
        #     if self.text[i].lower() in self.vowels:
        #         self.text = self.text[:i] + self.text[i+1:]
        #     i += 1
        while i < len(self.text):
            if self.text[i].lower() not in self.vowels:
                vowels_removed += self.text[i]
            i += 1
        return vowels_removed
