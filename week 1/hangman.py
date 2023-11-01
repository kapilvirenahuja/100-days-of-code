import random

print ("This is a game - The Hangman")

# generate random word
words = ["apple", "banana", "orange", "pear", "grape", "pineapple", "mango", "strawberry", "blueberry", "raspberry"]
chosen_word = random.choice(words).lower()

# initialize guessed letters
guessed_letters = []
guessed_correct_letters = []
tries = 0

def generate_hangman(hangman_word):
    hangman = ""
    for i in range(len(hangman_word)):
        hangman += hangman_word[i] + " "
    print(hangman)

# generate a word of same length of that of chosen word, but this should be all blanks
for i in range(len(chosen_word)):
    guessed_correct_letters.append("_")

generate_hangman(guessed_correct_letters)
guessed_correct_letters = []

# this is so that we can generate a new hangman word with blanks
guessed_chosen_word = ""


# loop until the user guesses the word correctly
while True:
    # ask the user a letter
    letter = input("Guess a letter: ").lower()

    # clear screen
    print("\n" * 100)

    # check if the letter has already been guessed
    if letter in guessed_letters:
        print(f"You already guessed the letter {letter}. Try again.")
        continue
    
    # add the letter to the guessed letters list
    guessed_letters.append(letter)

    # check if the letter is in the word
    if letter in chosen_word:
        print(f"The letter {letter} is in the word!")
        guessed_correct_letters.append(letter)
        
        #replace the letters in the chosen_word which have not yet been guessed with a "_"
        guessed_chosen_word = chosen_word
        for i in range(len(guessed_chosen_word)):
            if guessed_chosen_word[i] not in guessed_correct_letters:
                guessed_chosen_word = guessed_chosen_word.replace(guessed_chosen_word[i], "_")
        generate_hangman(guessed_chosen_word)
    else:
        print(f"The letter {letter} is not in the word.")
        generate_hangman(guessed_chosen_word)
        tries += 1
        if tries == 7:
            print(f"You have not been able to guess the word {chosen_word}. You just lost the game. You guessed the letters {guessed_letters}.")
            print (set(chosen_word))
            print (set(guessed_letters))
            break
        else:
            print(f"You have {7 - tries} tries left.")
        
    # check if the user has guessed all the letters in the word
    if set(chosen_word) == set(guessed_correct_letters):
        print(f"You have guessed the word {chosen_word} correctly. You won the game with {7 - tries} left!")
        break


