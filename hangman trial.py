import random
from words import words
import string

def get_random_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    str(word)
    return word

def hangman():
    word = get_random_word()
    alphabet = set(string.ascii_uppercase)
    word = word.upper()
    
    word_letters = set(word) #letters of the word
    used_letters = set()     #words the user has guessed

    while len(word_letters)>0:
        print("You have used these letters:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"Your current word:",[word_list])
        #getting user input
        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet:
            if user_letter not in used_letters:
                used_letters.add(user_letter)
                
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                                    
            else: print("You have used this letter already.")
       
    



hangman()



