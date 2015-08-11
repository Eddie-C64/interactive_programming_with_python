# Implementation of classic arcade game Pong
#http://www.codeskulptor.org/#user40_yFXFsJSM5R_2.py
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score_position = [WIDTH/2-43,50]
SCORING = "0 | 0"
ball_vel = [0,0]
ball_pos = [300,200]
acc = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [300,200]
    ball_dir = [1,-1]
    if(direction =="Left"):
        ball_dir = [1,-1]
    elif(direction == "RIGHT"):
        ball_dir = [-1,-1]
    horizontal_vel = random.randrange(120, 240)/100.0
    vertical_vel = random.randrange(60, 180)/100.0
    ball_vel = [horizontal_vel*ball_dir[0], vertical_vel*ball_dir[1]]
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, paddle1, paddle2
    score1 = 0
    score2  = 0
    paddle1 = [[0,160],[8,160],[8,240],[0,240]]
    paddle2 = [[600,160],[592,160],[592,240],[600,240]]
    paddle1_pos = [0]
    paddle2_pos = [0]
    paddle1_vel = [0]
    paddle2_vel = [0]   
    spawn_ball("LEFT")
    
def scoring(string):
    global score1, score2, SCORING
    SCORING = str(score1)+" | "+str(score2)
    return SCORING

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel, acc
      
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update paddle's vertical position
    paddle1_pos[0] += paddle1_vel[0]
    paddle2_pos[0] += paddle2_vel[0]
    paddle1 = [[0,160+paddle1_pos[0]],[8,160+paddle1_pos[0]],[8,240+paddle1_pos[0]],[0,240+paddle1_pos[0]]]
    paddle2 = [[600,160+paddle2_pos[0]],[592,160+paddle2_pos[0]],[592,240+paddle2_pos[0]],[600,240+paddle2_pos[0]]]
    paddle1_cen = [paddle1[1],paddle1[2]]
    paddle2_cen = [paddle2[1],paddle2[2]]

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]   
    
    #""" Updates the ball's location """"
    #Bounds for left and right gutters
    # determine whether paddle and ball collide    

    if ball_pos[0] <= BALL_RADIUS:
        if(paddle1_cen[0][1]< ball_pos[1] and ball_pos[1] < paddle1_cen[1][1]):
            ball_vel[0] = -1*(ball_vel[0]-2)
        else:
            score2 = score2 + 1
            spawn_ball("LEFT")
    if ball_pos[0] >= WIDTH-BALL_RADIUS:
        if(paddle2_cen[0][1]< ball_pos[1] and ball_pos[1] < paddle2_cen[1][1]):
            ball_vel[0] = -1*(ball_vel[0]+2)
        else:
            score1 = score1 + 1
            spawn_ball("RIGHT")
    
    #Bounds for top and bottom screen
    if (ball_pos[1] > 380):
        ball_vel[1] = -ball_vel[1]
    if (ball_pos[1] <= 20):
        ball_vel[1] = -ball_vel[1]
    #Checks if paddles are out of range
    if((paddle1[2][1])>=400):
        acc = -0
        paddle1_vel[0] = acc
    if(paddle2[2][1] >= 400):
        acc = -0
        paddle2_vel[0]=0
    if(paddle1[0][1] <= 0):
        acc = -0
        paddle1_vel[0] = acc
    if(paddle2[0][1]<=1):
        acc = -0
        paddle2_vel[0]=0
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # draw paddles
    canvas.draw_polygon(paddle1, 3, 'White', 'Red')
    canvas.draw_polygon(paddle2, 3, 'White', 'Blue')

    # draw scores
    canvas.draw_text(scoring(SCORING), score_position, 50, "White")
     
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1, acc
    acc = 5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= acc   
    pass

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] = 0
    pass

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.add_button("Restart",new_game,150)
frame.start()
