class Diary:
    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)

    def all(self):
        return self.entry_list

    def count_words(self):
        return sum([entry.count_words() for entry in self.entry_list])

    def reading_time(self, wpm):
        if self.entry_list == []:
            raise Exception("No entries added yet")
        total_reading_time = 0
        for entry in self.entry_list:
            total_reading_time += entry.reading_time(wpm)
        return total_reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        word_limit = wpm * minutes
        result = ['', '']
        if self.entry_list == []:
            raise Exception("No entries added yet")
        for entry in self.entry_list:
            if entry.count_words() <= word_limit and entry.count_words() > len(result[1].split()):
                result = [entry.title, entry.contents]
        return result