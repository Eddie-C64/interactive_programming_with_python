## http://www.codeskulptor.org/#user40_jzwQiPUypY_2.py
#para espanolhttp://www.codeskulptor.org/#user40_jzwQiPUypY_3.py
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#local variables
num_range = 100 
secret_num = 0
remaining_guesses = 10

# helper function to start and restart the game
def new_game():
    """ This creates a new game to play """
    global secret_num, remaining_guesses, num_range
    if(num_range == 100):
        secret_num = random.randint(1, 100)
    else:
        secret_num = random.randint(1, 1000)
    pass

# define event handlers for control panel
def range100():
    """This is the handler for range of 0 to 100"""
    global remaining_guesses, num_range
    remaining_guesses = 7
    num_range = 100
    print "New game. Range from 0 to 100"
    print "Number of remaining guesses is 7"
    print ""
    pass

def range1000():
    """ This is the handler for the range of 0 to 1000 """
    new_game()
    global secret_num, remaining_guesses, num_range
    num_range = 1000
    remaining_guesses = 10
    print "New game. Range from 0 to 1000"
    print "Number of remaining guesses is 10"
    print""
    pass
    
def get_input(guess):
    global secret_num, remaining_guesses, num_range
    your_guess = int(guess)
    remaining_guesses = remaining_guesses - 1
    print "You guess was", your_guess
    print "Number of remaining guesses is", remaining_guesses
    if(remaining_guesses == 0):
        print "Out of guess"
    else:
        if(your_guess > secret_num):
            print "Lower"
        elif(your_guess < secret_num):
            print "Higher"
        elif(your_guess == secret_num):
            print "Correct! You win!"
    
    print ""
    pass

# create frame
frame = simplegui.create_frame("Guess the Number!?", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("The Range is [0,100)", range100, 200)
frame.add_button("The Range is [0,1000)",range1000, 200)
frame.add_input("Your Guess:", get_input, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
