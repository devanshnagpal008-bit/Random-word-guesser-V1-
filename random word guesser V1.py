import random
import sys

def play_game():
    easy=['car','dog','cap', 'bat','hat','mat']
    medium=['park','road','camp','shut','lion']
    hard=['banana','apple','mercedes','mountain','river',]

    a=input("please choose the difficulty level (easy / medium / hard) :").strip().lower()

    if a=='easy':
        word=random.choice(easy)
        print('the word has been chosen. Guess it using the following hints.\nHint 1--> the length of the word is  : ',len(word))
        print('Hint 2--> the first letter is :',word[0])
        print('Hint 3--> the last letter is :',word[len(word)-1])
        user_guess=input('enter your guess :').strip().lower()
        if user_guess==word:
            print("Hurray you got it right!!!!!!")
            continue_game=input('To play again enter yes or enter quit to exit :').strip().lower()
            if continue_game=='yes':
                play_game()
            elif continue_game=='quit':
                sys.exit("---GOODBYE---")
        else:
            print("uhuh... nice try but thats not the word.\n please try again...")
            user_guess=input('enter your guess :').strip().lower()
            while True:
                if user_guess==word:
                    print("Hurray you got it right!!!!!!")
                    continue_game=input('To play again enter yes or enter quit to exit :').strip().lower()
                    if continue_game=='yes':
                        play_game()
                    elif continue_game=='quit':
                        sys.exit("---GOODBYE---")
                else:
                    print("uhuh... nice try but thats not the word.\n please try again...")
                    user_guess=input('enter your guess :').strip().lower()
                continue

    if a=='medium':
        word=random.choice(medium)
        print('the word has been chosen. Guess it using the following hints.\nHint 1--> the length of the word is  : ',len(word))
        print('Hint 2--> the first letter is :',word[0])
        print('Hint 3--> the last letter is :',word[len(word)-1])
        user_guess=input('enter your guess :').strip().lower()
        if user_guess==word:
            print("Hurray you got it right!!!!!!")
            continue_game=input('To play again enter yes or enter quit to exit :').strip().lower()
            if continue_game=='yes':
                play_game()
            elif continue_game=='quit':
                sys.exit("---GOODBYE---")
        else:
            print("uhuh... nice try but thats not the word.\n please try again...")
            user_guess=input('enter your guess :').strip().lower()
            while True:
                if user_guess==word:
                    print("Hurray you got it right!!!!!!")
                    continue_game=input('To play again enter yes or enter quit to exit :').strip().lower()
                    if continue_game=='yes':
                        play_game()
                    elif continue_game=='quit':
                        sys.exit("---GOODBYE---")
                else:
                    print("uhuh... nice try but thats not the word.\n please try again...")
                    user_guess=input('enter your guess :').strip().lower()
                continue

    if a=='hard':
        word=random.choice(hard)
        print('the word has been chosen. Guess it using the following hints.\nHint 1--> the length of the word is  : ',len(word))
        print('Hint 2--> the first letter is :',word[0])
        print('Hint 3--> the last letter is :',word[len(word)-1])
        user_guess=input('enter your guess :').strip().lower()
        if user_guess==word:
            print("Hurray you got it right!!!!!!")
            continue_game=input('To play again enter yes or enter quit to exit :').strip().lower()
            if continue_game=='yes':
                play_game()
            elif continue_game=='quit':
                sys.exit("---GOODBYE---")
        else:
            print("uhuh... nice try but thats not the word.\n please try again...")
            user_guess=input('enter your guess :').strip().lower()
            while True:
                if user_guess==word:
                    print("Hurray you got it right!!!!!!")
                    continue_game=input('To play again enter yes or enter quit to exit :').strip().lower()
                    if continue_game=='yes':
                        play_game()
                    elif continue_game=='quit':
                        sys.exit("---GOODBYE---")
                else:
                    print("uhuh... nice try but thats not the word.\n please try again...")
                    user_guess=input('enter your guess :').strip().lower()
                continue



print("Welcome to the word guesser game.\nChoose your difficulty and guess the correct word using the given hints!!!")
play=input('To play the game enter yes or no :').strip().lower()
if play=='yes':
    play_game()
elif play=='no':
    print('---GOODBYE---')
    sys.exit("---GOODBYE---")
