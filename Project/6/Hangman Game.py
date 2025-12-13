import random
from hangman_words import word_list
from hangman_art import hangman_logo,stage

# Prints the logo of Hangman
print(hangman_logo)

# Chooses Random word from the word list and Prints them
chosen_word=random.choice(word_list)
# print(chosen_word)

# Printing blanks equivalent to the chosen word
blanks=""
for s in chosen_word:
    blanks+="_"
print("The word to guess:", blanks, ",gcontains", len(chosen_word), "Letters")

# Lives tracking
lives=6

# Boolean Condition for While loop to execute till the condition is True
game_over=False

# Stores all the correct answers selected by the users
correct_answers=[]

while not game_over:
    # For the user to keep track of the Lives
    print(f"***************************************<{lives}/6 LIVES LEFT>***************************************")

    # Fetching Letter from the user:
    guessed_letter=input("Guess a letter to form up the Word, Type a letter: ").lower()
    print(guessed_letter) # Prints the User typed answers

    # If the guessed letter is repeated & It notifies the user that he has already selected it
    if guessed_letter in correct_answers:
        print(f"You have already guessed the letter: {guessed_letter}")

    # Display the output eg: chosen word: Glue, when user selects "G", it displays: "G___"
    display="" # An empty string to store the display
    for s in chosen_word: # For Letters in Chosen Word
        if guessed_letter==s:   # If the guessed letter = Letter in chosen word
            display+=s          # Displays the Correct Guessed Letter
            correct_answers.append(guessed_letter)  # Stores the Guessed Letter in the Correct answers List, To keep Track all the past correct answers
        elif s in correct_answers:     # Prints the Previous Correct answers
            display+=s                 # Displays the Output all with Current Correct ones
        else:
            display+="_"               # Displays Blanks "_", for every Incorrect & Unguessed Letters

    # Prints the Display output eg: "b_b__n"
    print("Word to guess:", display)

    # If the guessed letter is incorrect the lives will decrease by 1
    if guessed_letter not in chosen_word:
        lives-=1
        print(f"You have guessed the letter {guessed_letter} that's not in word. Try again guessing the correct one") # Prints the Incorrect answer

    # If lives are emptied, Game is Over so,it replaces the boolean with True, Finally Breaking the execution of While Loop since the Criteria is met
    if lives==0:
        game_over=True
        print(f"***************************************<{lives}/6 LIVES LEFT>, THE WORD IS: {chosen_word}, YOU LOSE***************************************") # Reveals the answer to the user, and prints he lost the game

    # If there are no blanks left in the Guessed word
    if "_" not in display:
        # If the Guessed Word is same as the Chosen Word
        if display==chosen_word:
            # Game is Over, replaces the Boolean value of game_over by True, Breaking the While Loop
            game_over=True
            print(f"***************************************<YOU WIN>***************************************") # Prints that the user has won the game

    # Prints the Hangman stages for the user to keep track of lives, Each stage Image aligns with the lives left
    print(stage[lives])