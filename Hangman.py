import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()


guessedWord = False
wordList = []
for i in WORDS:
    wordList.append(i.decode("utf-8"))

keyWord = random.choice(wordList)
emptyKey = len(keyWord) * "?"

numGuesses = 10

print(emptyKey)

while not guessedWord:

    if emptyKey == keyWord:
        guessedWord = True
        print("You won!")
    else:
        guess = input("Guess a letter. ")
        print(emptyKey)

        if guess not in keyWord:
            numGuesses -= 1

            if numGuesses == 0:
                guessedWord = True
                print("You lose.")
                print(keyWord)
            else: 
                print(f'You have {numGuesses} guesses left.')

        for pos, letter in enumerate(keyWord):
            if guess == letter:
                emptyKey = emptyKey[:pos] + letter + emptyKey[pos+ 1:]
                print(emptyKey)
            

            

    #continue