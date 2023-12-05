import hangman_maker,word_handler

print("Welcome to the Hangman Game!")

player_tries=0
drawer=hangman_maker
winning_condition=False

guessword=word_handler.guessword()
guessword.choose_word()
known_word=''.join(guessword.letters)
victory_condition=False
while player_tries<6:
    print(' '.join(guessword.hidden_letters))
    drawer.draw(player_tries)
    guessed_letter=input("Guess a letter: ")
    if guessword.check_letter(guessed_letter)==False:
        player_tries = player_tries + 1

    try:
        guessword.hidden_letters.index('_')
    except:
        print("You won!")
        print("The word was "+known_word)
        victory_condition=True
        break





if victory_condition==False:
    drawer.draw(player_tries)
    print("You lose!")
    print("The word was "+known_word)

