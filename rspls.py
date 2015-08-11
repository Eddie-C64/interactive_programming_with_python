# Rock-paper-scissors-lizard-Spock game
#http://www.codeskulptor.org/#user40_iEcbo1uwYP_5.py
#Created for the purpose of simulating game play with a computer

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    #This function will genrate a random number
    # convert that name to a number
    if(name == 'rock'):
        the_number = 0
    elif(name == 'Spock'):
        the_number = 1
    elif(name == 'paper'):
        the_number =  2
    elif(name == 'lizard'):
        the_number =  3
    elif(name == 'scissors'):
        the_number =  4
        
    return the_number    


def number_to_name(number):
    #This function will generate a random number from 0 to 4
    if(number == 0):
        option = 'rock'
    elif(number == 1):
        option = 'Spock'
    elif(number == 2):    
        option = 'paper'
    elif(number == 3):
        option = 'lizard'
    else:    
        option = 'scissors'
        
    return option

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print("\n")
    
    # print out the message for the player's choice
    print("Player chooses "+ player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randint(0,4)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice 
    
    # compute difference of comp_number and player_number modulo five
    winner = ((comp_number-player_number)+5)%5
    # use if/elif/else to determine winner, print winner message
    if((winner == 3) or (winner == 4)):
        print('Player wins!')
    elif((winner==1) or (winner==2)):
        print("Computer wins!")
    else:
        print("Player and Computer tie!")
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


