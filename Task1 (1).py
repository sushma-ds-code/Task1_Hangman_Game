# Task 1: Hangman Game (Beginner Friendly Version)

# We will fix one secret word instead of using random
secret_word = "python"
guessed_letters = ""
chances = 6  # number of tries

print("Welcome to the Hangman Game!")
print("Guess the secret word, one letter at a time.")
print("You have", chances, "chances.\n")

while chances > 0:
    failed = 0

    # Check each letter in the secret word
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    # If no failed letters, player wins
    if failed == 0:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Ask player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Add guessed letter to the list
    guessed_letters += guess

    # If wrong guess
    if guess not in secret_word:
        chances -= 1
        print("Wrong guess! You have", chances, "chances left.")

        if chances == 0:
            print("😢 Game Over! The word was:", secret_word)
