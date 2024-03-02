import random
import time
import os


def playAgain():
    question = 'Do you want to play again? y = yes, n = no \n'
    playGame = input(question)
    while playGame.lower() not in ['y', 'n']:
        playGame = input(question)
    
    if playGame.lower() == 'y':
        return True
    else:
        return False



def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []
    while count < limit:
        guess = input(f'Wrong Guesses: {guessed} \nHangman Word: {display} Enter your guess: \n').strip()
        while len(guess) == 0 or len(guess) > 1:
            print('Invalid input. Enter a single letter\n')
            guess = input(
                f'Wrong Guesses: {guessed} \nHangman Word: {display} Enter your guess: \n'
            ).strip()

        if guess in guessed:
            print('Oops! You already tried that guess, try again!\n')
            continue

        if guess in letters:
            indices = [i for i, letter in enumerate(word) if letter == guess]   #find all instances of guessed letter
            for index in indices:
                display = display[:index] + guess + display[index + 1:]         #remove all instances of guessed letter from list of letters
            letters = [letter for letter in letters if letter != guess]

        else:
            guessed.append(guess)
            count += 1
            if count == 1:
                time.sleep(1)
                print(
                    '  ______ \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__    \n'
                )
                print(f'Wrong guess: {limit - count} guesses remaining\n')
            
            elif count == 2:
                time.sleep(1)
                print(
                    '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__    \n'
                )
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 3:
                time.sleep(1)
                print(
                    '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__    \n'
                )
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 4:
                time.sleep(1)
                print(
                    '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__    \n'
                )
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 5:
                time.sleep(1)
                print(
                    '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /|\   \n'
                    '  |    / \  \n'
                    '__|__     \n'
                )
                print(f'The word was: {word}')


        if display == word:
            print(f'Congrats! You have guessed the word \'{word}\' correctly!')
            break



def playHangman():
    print('\nWelcome to Hangman\n')
    name = input('Enter your name: ')
    print(f'Hello {name}! Best of Luck!')
    time.sleep(1)
    print('The game is about to start!\nLet\'s play Hangman!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    wordsToGuess = [
        'january', 'border', 'house', 'noob', 'ronnie', 'dinosaur', 'discord',
        'shocking', 'coffee', 'milkshake', 'medicine', 'record', 'trailer' ,
        'bully', 'capacinno', 'target', 'computer', 'laptop', 'television',
        'canary', 'matrix', 'shingle', 'pringle', 'titan', 'sword', 'art',
        'online', 'dragon', 'ball', 'electricity', 'magnet', 'solar', 'battle',
        'flare', 'diver', 'school', 'hippopotamus', 'there', 'their' ,
        'pterodactyl', 'aerodactyl', 'digtoise', 'blastoise', 
    ]
    play = True
    while play:
        word = random.choice(wordsToGuess)
        hangman(word)
        play = playAgain()
    
    print('Thanks for Playing! I expect you back again!')
    exit()


if __name__ == '__main__':
    playHangman()