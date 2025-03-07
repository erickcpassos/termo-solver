from collections.abc import Callable
import copy
alphabet = 'abcdefghijklmnopqrstuvxwyz'

class Knowledge:

    def __init__(self, id: int, word_list: list[str], sort_func: Callable[[str], float]):
        self.reset(id, word_list, sort_func)

    def reset(self, id: int, word_list: list[str], sort_func: Callable[[str], float]):
        
        self.id = id
        self.solved = False
        self.word_list = sorted(word_list, key=sort_func)
        initial_space_knowledge = dict()

        for c in alphabet:
            initial_space_knowledge[c] = True

        self.knowledge = [copy.deepcopy(initial_space_knowledge) for i in range(5)]

        self.needed_letters = set()
        return

    def is_coherent(self, word:str) -> bool:
        
        for letter in self.needed_letters:
            if letter not in word: return False
        
        for pos in range(5):
            letter_in_pos = word[pos]
            if not self.knowledge[pos][letter_in_pos]:
                return False

        return True
    
    def add_hint(self, guess: str, response: str) -> None:
        if response == "N": 
            self.word_list.remove(guess)

        if response == "GGGGG":
            self.solved = True
            return

        for pos, val in enumerate(response):
            if val == "G" or val == "Y":
                self.needed_letters.add(guess[pos])

        for pos, val in enumerate(response):
            if val == "B":
                if guess[pos] in self.needed_letters:
                    self.knowledge[pos][guess[pos]] = False
                    continue    

                for i in range(5):
                    self.knowledge[i][guess[pos]] = False

            elif val == "Y":
                self.needed_letters.add(guess[pos])
                self.knowledge[pos][guess[pos]] = False

            else:
                self.needed_letters.add(guess[pos])
                for lett in alphabet:
                    if lett != guess[pos]: self.knowledge[pos][lett] = False
                    else: self.knowledge[pos][guess[pos]] = True

    def get_guess(self):
        for word in self.word_list:
            if self.is_coherent(word):
                return word
        return "ERRO"