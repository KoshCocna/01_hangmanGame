import random
from hangmanWords import wordList
from hangmanArt import stages, logo

print(logo)
life = 6
endGame = False
chosenWord = random.choice(wordList)

display = []

for i in range(len(chosenWord)):
    display.append('_')

while not endGame:

    guessedLetter = input('Guess a letter: ').lower()

    # if guessedLetter == '111':
    #     print(chosenWord)

    guessed = 0
    for index, letter in enumerate(chosenWord):
        if letter == guessedLetter:
            display[index] = guessedLetter
            guessed = 1
    if guessed == 0:
        life -= 1
    if '_' not in display:
        print("you win!")
        endGame = True
    print(display)
    if life == 0:
        print("you lose...")
        endGame = True
    print(stages[life])

