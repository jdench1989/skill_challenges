class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.working_total_of_read_content = []

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        if isinstance(self.contents, str):
            words = self.contents.split()
            return len(words)

    def reading_time(self, wpm):
        word_list = self.contents.split()
        return len(word_list)/wpm

    def reading_chunk(self, wpm, minutes):
        total_words = wpm * minutes
        if len(self.contents.split()) <= total_words:
            return self.contents
        else:
            words = self.contents.split()
            result = f"{' '.join(words[len(self.working_total_of_read_content):len(self.working_total_of_read_content)+total_words])}"
            self.working_total_of_read_content += result.split()
            return result
        
# Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.