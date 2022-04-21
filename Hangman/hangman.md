
```python
from Hangman import Hangman

# Get answer from player 1
answer = input("Enter a word: ")

hangman = Hangman(answer)

# Remove answer from last line
hangman.remove_last_line()

attempts = 10

# While player 2 still has attempts
while attempts > 0:
    # Give player 2 info
    print(hangman.hidden_characters)
    print("{} attempts left.".format(attempts))

    # Get guess from player 2
    guess = input("Guess a letter or word: ")

    # If the guess is less than 1 character long
    if len(guess) < 1:
        continue



    # If the guess is exactly 1 character long
    if len(guess) == 1:
        if guess in answer:
            hangman.add_character(guess)
        else:
            attempts = attempts - 1
            print("Wrong!")

    # If the guess is more than one character long
    if len(guess) > 1:
        if guess == answer:
            for char in guess:
                hangman.add_character(char)
        else:
            attempts = attempts - 1
            print("You got it!")


    # If the hidden word matches the answer
    if hangman.hidden_word == hangman.answer:
        print("You got it!")
        break

    # If you have no more attempts left
    if attempts < 1:
        print("Try again!")
        break
```





```python
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

```
