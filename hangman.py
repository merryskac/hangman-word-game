from words import word
from hang_guy import hangguy
import random
import string

words=word['data']
def word_chosen():
    word_valid=random.choice(words)
    return word_valid

def hangman():
    print('WELCOME TO HANGMAN')
    word = word_chosen().upper()
    word_set = set(word)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while lives>0 and len(word_letter) != 0:
        guess = [j if j in used_letters else '-' for j in word ]
        print(' '.join(guess))
        input_letter=input("\nInput letter: ").upper()

        if len(input_letter)>1:
            print("Multiple letter detected\n")
        if not input_letter in used_letters:
            if input_letter in word_set:
                print(f'Theres {input_letter} in the word\n')
                used_letters.add(input_letter)
                word_letter.remove(input_letter)
            else:
                live=5
                print(f'There\'s no {input_letter} in word\n')
                used_letters.add(input_letter)
                lives -=1
                print(hangguy[live-lives])
        else:
            print(f"letter {input_letter} has been used \n")

        if len(word_letter) == 0:
            print(' '.join(word))
            print("You win!")

    if lives ==0:
        print("You lose!")

hangman()