class GrammarStats:
    def __init__(self):
        self.check_results = {"True":0, "False":0}
        pass
  
    def check(self, text):
        special_characters = ['.', '!', '?']
        if isinstance(text, str):
            if text[-1] in special_characters and text[0].isupper():
                self.check_results["True"] += 1
                return True
            else:
                self.check_results["False"] += 1
                return False
        else:
            raise Exception('Input must be a string!')
  
    def percentage_good(self):
        total_number_of_checks = self.check_results["True"] + self.check_results["False"]
        return (self.check_results["True"]/total_number_of_checks) * 100