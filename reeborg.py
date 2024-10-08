from words import words
import random
import string


alphabet = set(string.ascii_uppercase)

word = random.choice(words)
word = word.lower()
print(word)

word_lenght  = len(word)


display = []
for _ in range(word_lenght):
    display += "_"
print(display)
end = False
lives = 6
used_letters = ""
while end == False and lives >0:
    user_input = input("Guess a letter: ").lower()
    if user_input not in alphabet:
        print("PLease print valid character")
   
    if user_input in used_letters:
            print(f"You have used this letter {user_input} already")
    used_letters+=user_input
    for position in range(word_lenght):
        letter = word[position]
        if user_input == letter:
            display[position] = user_input
    print(display)
    if user_input in display:
        print(f"Yay. you guessed right. \n You have {lives} lifes left")
    elif user_input not in display:
        lives -= 1
        print(f"You guessed {user_input}, thats not in the word. you lose a life")
    
    if lives == 0:
        print("You lose")
    if "_" not in display:
        end = True
        print("You won")
print(used_letters)