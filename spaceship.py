'''
Clara Kim
CS5001
November 1, 2018
HW5

referred to Matplotlib for Python  color
(https://matplotlib.org/examples/color/named_colors.html)

referred to Python for Turtle graphics syntax
(https://docs.python.org/3.3/library/turtle.html?highlight=turtle)

'''
import turtle
import random

def generate_word(file_name='wordlist.txt',):
    '''function is generate_word
    parameters: none
    returns: string (a word)
    does: randomly selects and returns a word from wordlist.txt /
          prints an error message if file cannot be accessed
    '''
    try:
        file_open = open(file_name, 'r')
        # read file into a list
        wordlist = file_open.readlines()
        # close file
        file_open.close()
        # strip '\n' after each word
        for i in range(len(wordlist)):
            wordlist[i] = wordlist[i].strip('\n\n')
        # randomly select a number from the list and returns it
        return wordlist[random.randint(0,(len(wordlist)-1))]
    except OSError:
        print('Sorry, there was an error accessing the word list.')

def find_letters(letter, word):
    '''function is find_letters
    parameters: two strings (one letter and one word)
    returns: all of the positions in the word in which the letter is located'''
    positions = []
    for i in range(len(word)):
        if letter == word[i]:
            positions.append(i)
    return positions

def new_score(name, score, file_name='scores.txt'):
    '''function is new_score
    parameters: string (name) and integer (score)
    returns: none
    does: appends new score into scores.txt'''
    try:
        name.replace(' ', '_')
        file_open = open(file_name, 'a')
        file_open.write(name + ' ' + str(score) + '\n')
        file_open.close()
    except OSError:
        print('Sorry, there was an error accessing the scores list.')

def high_score(name, score, file_name='scores.txt'):
    '''function is high_score
    parameters: string (name) and integer (score)
    returns: none
    does: checks if score is new high score. if so, adds to top of list
          and deletes from bottom of list'''
    try:
        file_open = open(file_name, 'r')
        name_score = file_open.readlines()
        file_open.close()
        for i in range(len(name_score)):
            name_score[i] = name_score[i].strip('\n')
            name_score[i] = name_score[i].split(' ')
        if score >= int(name_score[0][1]):
            name_score.insert(0, [name, str(score)])
            name_score.pop(-1)
            file_open = open(file_name,'w')
            for i in range(len(name_score)):
                file_open.write(name_score[i][0] + ' ' + name_score[i][1] + '\n')
        file_open.close()
    except OSError:
        print('Sorry, there was an error accessing the scores list.')

# BELOW ARE GRAPHICS-RELATED FUNCTIONS

def draw_background():
    '''function is draw_background
    parameters: none
    returns: none
    does: set background color and draw the stars across it'''
    # background color
    turtle.bgcolor('midnightblue')
    # "stars" (small circles) randomly drawn across background
    stars = turtle.Turtle()
    stars.hideturtle()
    stars.speed(0)
    stars.color('gainsboro','mistyrose')
    for i in range(50):
        stars.penup()
        stars.goto(random.randint(-320,320),random.randint(-250,250))
        stars.pendown()
        stars.begin_fill()
        stars.circle(random.randint(1,4))
        stars.end_fill()

def draw_letterlines(n):
    '''function is draw_letterlines
    parameters: integer (number of characters in the word)
    returns: none
    does: draws one line for each character in the word'''
    line = turtle.Turtle()
    line.speed(10)
    line.hideturtle()
    line.color('black')
    line.width(5)
    line.penup()
    line.goto(-300, 200)
    for i in range(n):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(10)

def write_right(letter, positions):
    '''function is write_right
    parameters: string (a letter) and list (positions of the letter in a word)
    returns: none
    does: writes the letter on its corresponding position in a word'''
    character = turtle.Turtle()
    character.hideturtle()
    for i in range(len(positions)):
        character.penup()
        character.goto((-290 + 28 * positions[i]),205)
        character.pendown()
        character.write(letter, font=('Helvetica', 14, 'bold'))

def write_wrong(letter, n):
    '''function is write_wrong
    parameters: string (a letter) and int (n)
    returns: none
    does: writes the letter on the wrong guess side of the screen'''
    character = turtle.Turtle()
    character.hideturtle()
    character.penup()
    character.goto((180 + 15 * n),205)
    character.pendown()
    character.write(letter, font=('Helvetica', 14, 'bold'))

def draw_body():
    '''function is draw_body
    parameters: none
    returns: none
    does: draws the ship's body'''
    body = turtle.Turtle()
    body.speed(10)
    body.hideturtle()
    # tip
    body.color('black','red')
    body.width(3)
    body.penup()
    body.begin_fill()
    body.goto(0,175)
    body.pendown()
    body.goto(-50,110)
    body.goto(50,110)
    body.goto(0,175)
    body.end_fill()
    # between tip and body
    body.color('black','khaki')
    body.penup()
    body.goto(-55,100)
    body.pendown()
    body.begin_fill()
    body.goto(55,100)
    body.goto(55,110)
    body.goto(-55,110)
    body.goto(-55,100)
    body.end_fill()
    # body
    body.color('black','mediumturquoise')
    body.penup()
    body.goto(-50,100)
    body.pendown()
    body.begin_fill()
    body.goto(50,100)
    body.goto(50,-90)
    body.goto(-50,-90)
    body.goto(-50,100)
    body.end_fill()
    # top window
    body.color('black','khaki')
    body.penup()
    body.goto(0,33)
    body.pendown()
    body.begin_fill()
    body.circle(27)
    body.end_fill()
    body.color('black','cornflowerblue')
    body.penup()
    body.goto(0,40)
    body.pendown()
    body.begin_fill()
    body.circle(20)
    body.end_fill()
    # bottom window
    body.color('black','khaki')
    body.penup()
    body.goto(0,-35)
    body.pendown()
    body.begin_fill()
    body.circle(27)
    body.end_fill()
    body.color('black','cornflowerblue')
    body.penup()
    body.goto(0,-28)
    body.pendown()
    body.begin_fill()
    body.circle(20)
    body.end_fill()
    # between body and blasters
    body.color('black', 'khaki')
    body.penup()
    body.goto(-55,-90)
    body.pendown()
    body.begin_fill()
    body.goto(55,-90)
    body.goto(55,-100)
    body.goto(-55,-100)
    body.goto(-55,-90)
    body.end_fill()
    # blasters
    body.color('black','mediumorchid')
    body.penup()
    body.goto(-40,-100)
    body.pendown()
    body.begin_fill()
    body.goto(40,-100)
    body.goto(40,-115)
    body.goto(-40,-115)
    body.goto(-40,-100)
    body.end_fill()
    body.penup()
    body.goto(-35,-115)
    body.pendown()
    body.begin_fill()
    body.goto(35,-115)
    body.goto(35,-125)
    body.goto(-35,-125)
    body.goto(-35,-115)
    body.end_fill()
    # blaster fire
    body.color('black','orange')
    body.penup()
    body.goto(-15,-125)
    body.pendown()
    body.begin_fill()
    body.goto(15,-125)
    body.goto(25,-160)
    body.goto(10,-150)
    body.goto(0,-175)
    body.goto(-10,-150)
    body.goto(-25,-160)
    body.goto(-15,-125)
    body.end_fill()
    body.color('black','yellow')
    body.penup()
    body.goto(-10,-125)
    body.pendown()
    body.begin_fill()
    body.goto(5,-125)
    body.goto(10,-140)
    body.goto(5,-130)
    body.goto(0,-150)
    body.goto(-5,-130)
    body.goto(-10,-140)
    body.goto(-5,-125)
    body.end_fill()

def draw_rocket_right():
    '''function is draw_rocket_right
    parameters: none
    returns: none
    does: draws the right rocket'''
    # body to rocket connector
    right = turtle.Turtle()
    right.hideturtle()
    right.width(3)
    right.color('black','khaki')
    right.penup()
    right.goto(50,-35)
    right.pendown()
    right.begin_fill()
    right.goto(50,-55)
    right.goto(80,-95)
    right.goto(80,-75)
    right.goto(50,-35)
    right.end_fill()
    # rocket
    right.color('black','red')
    right.penup()
    right.goto(80,-75)
    right.pendown()
    right.begin_fill()
    right.goto(60,-120)
    right.goto(100,-120)
    right.goto(80,-75)
    right.end_fill()
    # rocket blaster
    right.color('black','mediumorchid')
    right.penup()
    right.goto(70, -120)
    right.pendown()
    right.begin_fill()
    right.goto(90,-120)
    right.goto(90, -130)
    right.goto(70,-130)
    right.goto(70,-120)
    right.end_fill()
    # rocket design
    right.width(0.5)
    for i in range(10):
        right.penup()
        right.color('aqua')
        right.goto(80,-75)
        right.pendown()
        right.goto(62 + 4 * i, -120)

def draw_rocket_left():
    '''function is draw_rocket_left
    parameters: none
    returns: none
    does: draws the left rocket'''
    # body to rocket connector
    left = turtle.Turtle()
    left.hideturtle()
    left.width(3)
    left.color('black','khaki')
    left.penup()
    left.goto(-50,-35)
    left.pendown()
    left.begin_fill()
    left.goto(-50,-55)
    left.goto(-80,-95)
    left.goto(-80,-75)
    left.goto(-50,-35)
    left.end_fill()
    # rocket
    left.color('black','red')
    left.penup()
    left.goto(-80,-75)
    left.pendown()
    left.begin_fill()
    left.goto(-60,-120)
    left.goto(-100,-120)
    left.goto(-80,-75)
    left.end_fill()
    # rocket blaster
    left.color('black','mediumorchid')
    left.penup()
    left.goto(-70, -120)
    left.pendown()
    left.begin_fill()
    left.goto(-90,-120)
    left.goto(-90, -130)
    left.goto(-70,-130)
    left.goto(-70,-120)
    left.end_fill()
    # rocket design
    left.width(0.5)
    for i in range(10):
        left.penup()
        left.color('aqua')
        left.goto(-80,-75)
        left.pendown()
        left.goto(-62 - 4 * i, -120)

def draw_fire_right():
    ''' function is draw_fire_right
    paremeters: none
    return: none
    does: draws the fire for the right rocket'''
    # outer fire
    firer = turtle.Turtle()
    firer.hideturtle()
    firer.width(3)
    firer.color('black','orange')
    firer.penup()
    firer.goto(75,-130)
    firer.pendown()
    firer.begin_fill()
    firer.goto(85,-130)
    firer.goto(100,-160)
    firer.goto(88,-150)
    firer.goto(80,-175)
    firer.goto(72,-150)
    firer.goto(60,-160)
    firer.goto(75,-130)
    firer.end_fill()
    # inner fire
    firer.color('black','yellow')
    firer.penup()
    firer.width(2)
    firer.goto(77.5,-130)
    firer.pendown()
    firer.begin_fill()
    firer.goto(82.5,-130)
    firer.goto(80,-155)
    firer.goto(77.5,-130)
    firer.end_fill()

def draw_fire_left():
    ''' function is draw_fire_left
    paremeters: none
    return: none
    does: draws the fire for the left rocket'''
    # outer fire
    firel = turtle.Turtle()
    firel.hideturtle()
    firel.width(3)
    firel.color('black','orange')
    firel.penup()
    firel.goto(-75,-130)
    firel.pendown()
    firel.begin_fill()
    firel.goto(-85,-130)
    firel.goto(-100,-160)
    firel.goto(-88,-150)
    firel.goto(-80,-175)
    firel.goto(-72,-150)
    firel.goto(-60,-160)
    firel.goto(-75,-130)
    firel.end_fill()
    # inner fire
    firel.color('black','yellow')
    firel.penup()
    firel.width(2)
    firel.goto(-77.5,-130)
    firel.pendown()
    firel.begin_fill()
    firel.goto(-82.5,-130)
    firel.goto(-80,-155)
    firel.goto(-77.5,-130)
    firel.end_fill()
