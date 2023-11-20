import random
from hangman_aski import hangman, hangman_title
from hangman_movie_list import word_list

print(hangman_title)
end_of_game = False
lives = 7

chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
    display+= "*"
print(display)


while not end_of_game:
    guess = input("Guess a letter ").lower()

    if guess in display:
        print(f'You have already guessed the letter {guess}')

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        #print("Congrats You entered a matching letter")
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    #print("You lost a life")

    if "*" not in display:
        end_of_game = True
        print("You win")

    print(hangman[lives])