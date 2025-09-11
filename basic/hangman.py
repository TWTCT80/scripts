import random


print("Welcome to Hangman!")

wordlist = ["gurka", "morot", "dragon"]

secret_word = random.choice(wordlist)
display_word = []

for lett in secret_word:
    display_word += "_"

print(display_word)    
guesses = 5
game_over = False
while not game_over:
    gissa = input("Gissa på en bokstav: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]

        if letter == gissa:
            display_word[position] = letter
    
    if gissa not in secret_word:
        guesses -= 1
        print(f"You have {guesses} guesses left!")
        if guesses <= 0:
            print("You've lost!")
            game_over = True

        
    print(display_word)

    if "_" not in display_word:
        print("You Win!")
        game_over = True