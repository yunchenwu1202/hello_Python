class Hangman:
    def __init__(self, word):
        self._word = word
        self._hidden_characters = ["_"] * len(self._word)

    @property
    def answer(self):
        return self._word
    @property
    def hidden_characters(self):
        return " ".join(self._hidden_characters)
    @property
    def hidden_word(self):
        return "".join(self._hidden_characters)

    def _indices(self, character):
        return [i for i, x in enumerate(self._word) if x == character]

    def add_character(self, character):
        for i in self._indices(character):
            self._hidden_characters[i] = character

    def remove_last_line(self):
        print ("\033[A                             \033[A")
