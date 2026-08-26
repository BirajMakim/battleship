word_list = ["aardvark", "baboon", "camel"]
import random
lives = 6
chose_word = random.choice(word_list)
print(chose_word)
place_holder = "_" * len(chose_word)
print(place_holder)
game_over = False
current_word = [ ]
while not game_over:
    guess = input("Guess the letter: ").lower()
    display = ""
    for letter in chose_word:
        if letter == guess:
            display += letter
            current_word.append(guess)
        elif letter in current_word:
            display += letter
        else:
            display += "_"
    print(display)

    ''' ---------------lives of user-------------------'''
    if guess not in chose_word:
        lives -= 1
        print(f"Incorrerct Guess!. You have{lives} live left")
        if lives == 0:
            game_over = True
            print(f"You lose!. The word was {chose_word}")
    '''---------------checking the user track -------------'''
    if "_" not in display:
        game_over = True
        print("You Win!")
