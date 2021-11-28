import random
from word import words
import string

def get_valid_word(words):
    word = random.choice(words) #choose randomly something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word) #Letter in words
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the user has guess

    lives = 6

    #Loop to guess all the letter of the words
    while len(word_letters) > 0 and lives > 0:

        # Letter used
        print("You have", lives, "lives left and You used these letters: ", ' '.join(used_letters)) #' ',join(['a', 'b', 'cd']) --> 'a b cd'

        #What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word.upper()]
        print("The current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1
                print('Letter is not in word')

        elif user_letter in used_letters:
            print("You have already used that character. Please try again ")
        else:
            print("Invalid character. Please try again")
    
    if lives == 0:
        print('You died, sorry. The word was: ', word)
    else:
        print('You guessed the word: ', word)


hangman()