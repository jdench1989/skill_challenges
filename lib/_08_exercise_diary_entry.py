class DiaryEntry:
    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents

    def count_words(self):
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        word_list = self.contents.split()
        return len(word_list)/wpm