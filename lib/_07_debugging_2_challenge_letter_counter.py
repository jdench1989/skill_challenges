class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0 #Was initialized as 1 in original. Changed to initialize as 0.
        # for char in self.text:
        #     if not char.isalpha():
        #         continue
        #     counter[char] = counter.get(char, 1) + 1
        #     if counter[char] > most_common_count:
        #         most_common = char
        #         most_common_count += counter[char]
        # return [most_common_count, most_common]
        # Several problems with this for loop. firstly, char is entered into the counter dict with an initial value of 2 instead of 1. 
        # Then, teh second if statement causes most_common to be assigned the first char and most_common_count set to counter[char]+1.
        # This immediately sets the returned variables to 3 D despite "D" only appearing once in text.
        # As no other letter appears more than three times this inaccurate result is returned. 
        for char in self.text:
            if char.isalpha():
                if char in counter:
                    counter[char] +=1
                else:
                    counter[char] = 1
            if char in counter and counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]
        return [most_common_count, most_common]
        # Now counter[char] is set to 1 in first instance, incremented if char in counter. 
        # Then if counter[char] is more than most_common_count, most_common and most_common_count are set to char and counter[char].
        # most_common and most_common_count are then returned once all chars have been processed. 


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]