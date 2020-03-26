import dictionary
import game

word_to_guess = dictionary.get_word()
hidden_word = "_" * len(word_to_guess)
letters_found = []
remaining_attempts = 10

print(f"""
Welcome to this Hangman Game!
You have {remaining_attempts} attempts to guess the word.
Have fun!
""")

game_over = False
while not game_over:
    print(f"Here is your word to guess : {hidden_word}")
    guess = game.make_guess()
    if guess in letters_found:
        print("You've already used this letter.")
    elif guess in word_to_guess:
        print("Good guess!")
        letters_found.append(guess)
    else:
        print("Bad Guess!")
        remaining_attempts -= 1
        print(f"Still {remaining_attempts} attempts left.")
    hidden_word = game.check_hidden_word(word_to_guess, letters_found)
    game_over = game.check_game_state(
        hidden_word, remaining_attempts, word_to_guess)
