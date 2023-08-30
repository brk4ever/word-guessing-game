import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon"]

def choose_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def main():
    print("Welcome to the Word Guessing Game!")
    random_word = choose_random_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nAttempts left:", attempts)
        displayed_word = display_word(random_word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You've guessed the word:", random_word)
            break

        if attempts == 0:
            print("Game over! The word was:", random_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in random_word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

if __name__ == "__main__":
    main()
