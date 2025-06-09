def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        display = ""

        for char in secret_word:
            if char.lower() in guesses:
                display += char
            else:
                display += "_"

        print("Current word:", display)

        return all(char.lower() in guesses for char in secret_word)

    return hangman_closure

# game time


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").strip()

    # Optionally hide the word by clearing the screen
    print("\n" * 50)
    print("Let's play Hangman!\n")

    play = make_hangman(secret_word)

    while True:
        guess = input("Guess a letter: ").strip().lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        word_guessed = play(guess)

        if word_guessed:
            print(f"\n🎉 You guessed the word: {secret_word}!")
            break
