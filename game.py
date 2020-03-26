def make_guess():
    guess = input("Make a guess: ").lower()
    if len(guess) > 1 or not guess.isalpha():
        print("Oops, your guess is invalid!")
        return make_guess()
    else:
        return guess


def check_hidden_word(word_to_guess, letters_found):
    hidden_word = ""
    for letter in word_to_guess:
        if letter in letters_found:
            hidden_word += letter
        else:
            hidden_word += "_"
    return hidden_word


def check_game_state(hidden_word, remaining_attempts, word_to_guess):
    if remaining_attempts == 0:
        print("You lost 😅")
        return True
    if hidden_word == word_to_guess:
        print(f"Congrats, you guessed the word : {word_to_guess} 💪")
        return True
    return False
