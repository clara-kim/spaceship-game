'''
Clara Kim
CS5001
November 4, 2018
HW5
'''
import spaceship
import turtle

# list of spaceship drawing functions as a constant
DRAW_SPACESHIP = [spaceship.draw_body, spaceship.draw_rocket_right,
  spaceship.draw_rocket_left, spaceship.draw_fire_right,
  spaceship.draw_fire_left]

def main():

    # welcome player, give instructions, and ask player if they want to play
    print('Welcome to Spaceship-- hangman without the death!\n\n'
          'Instructions:\n'
          '1. Each game, a random word will be generated.\n'
          '2. Guess one character at a time\n   '
          '(letter, space, comma, hyphen, or apostrophe).\n'
          '3. If the letter is in the word, that is a correct guess\n   '
          'and you get the letter!\n'
          '4. If the letter is not in the word, that is an incorrect guess\n   '
          'and one of five parts of the spaceship will be drawn.\n'
          '5. After 5 incorrect guesses, you lose.\n'
          '6. If you guess the word, you win 1 point!\n')
    select = input('Would you like to play? Y/N\n')
    games_won = 0
 
    while select == 'Y':
        # SET-UP PORTION (choose word, set up graphics)
        # use generate_word function to randomly generate word for play
        word = spaceship.generate_word().lower()
        # use draw_background function to draw background for play
        spaceship.draw_background()
        # use draw_letterlines function to draw lines for each letter
        spaceship.draw_letterlines(len(word))

        # GUESS PORTION (while < 5 incorrect guesses and word not guessed)
        incorrect_guess = 0
        correct_guess = 0
        prev_corrects = []
        while incorrect_guess < 5 and correct_guess < len(word):
            # ask player for guess and save as lowercase
            guess = input('Guess a character!\n').lower()
            if len(guess) != 1:
                print('Guesses can only be one character long.')
            elif guess in word:
                # if correct guess made previously--inform player (no points)
                if guess in prev_corrects:
                    print('You guessed this correct letter before!')
                else:
                    # list of correct guesses to keep track
                    prev_corrects.append(guess)
                    # use find_letters function to find its position
                    positions = spaceship.find_letters(guess, word)
                    # add number of times the guess appears in the word
                    # when the whole correct word is guessed, should == len(word)
                    correct_guess += len(positions)
                    # use write_right function to write letter on the right line
                    spaceship.write_right(guess, positions)
            else:
                incorrect_guess += 1
                # use write_wrong function for turtle to write bad guesses
                spaceship.write_wrong(guess, incorrect_guess)
                DRAW_SPACESHIP[incorrect_guess - 1]()

        # REPORTING RESULTS
        if correct_guess == len(word):
            games_won += 1
            print('You won! You now have', games_won, 'points!\n')
        else:
            print('You lost! The word was ', word.upper(), '.\n', sep = '')

        select = input('Would you like to play again? Y/N\n')

        #clear all turtle graphics
        turtle.clearscreen()

    # SAVING SCORE ONCE PLAYER QUITS
    print('Thanks for dropping by!\n')
    name = input('What is your name?\n').upper().replace(' ', '_')
    spaceship.new_score(name, games_won)
    spaceship.high_score(name, games_won)
    print('Your score of', games_won, 'and name', name, 'have been saved.\n'
          'Come by again soon!')
    
main()
