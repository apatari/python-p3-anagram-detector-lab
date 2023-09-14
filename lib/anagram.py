# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        res = []
        for str in word_list:
            if set(str) == set(self.word):
                res.append(str)
        return res