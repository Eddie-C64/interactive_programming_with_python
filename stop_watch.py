# template for "Stopwatch: The Game"
##http://www.codeskulptor.org/#user40_ErH4Z77qYg_1.py
import simplegui

# define global variables
message = "0:00.0"
position = [210, 300]
width = 500
height = 500
interval = 100
current_time = 0
message_plays = "0/0"
current_wins = 0
current_plays = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """ formats the time from mili_seconds to human time """
    global current_time, message
    t = current_time
    minutes = str(t/600)+":"
    dec_sec = str(((t/10)%60)/10)
    sec = str(((t/10)%60)%10)+"."
    mili_sec = str(t%10)
    message = ((minutes)+ (dec_sec) + (sec) + (mili_sec))
    return message
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    """ this is event starts the timer watch """
    timer.start()

def stop_timer():
    """Stops the timer on the watch"""
    global current_plays, current_time, current_wins, message_plays
    timer.stop()
    current_plays = current_plays + 1
    if( current_time%10 == 0):
        current_wins = current_wins+1
    else:
        current_wins = current_wins
    message_plays = (str(current_wins)+"/"+str(current_plays))   
        
def reset_timer():
    """ This resets the timer """
    global message, current_time, message_plays, current_wins, current_plays
    timer.stop()
    current_time = 0
    message = str(current_time)
    message_plays = "0/0"
    current_wins = 0
    current_plays = 0
    
# define event handler for timer with 0.1 sec interval
def creat_timer():
    global current_time
    timer = simplegui.create_timer(interval, timer_handler)

# define draw handler
def draw(canvas):
    global current_time, message, message_plays
    frame.set_canvas_background('White')
    message = format(current_time)
    canvas.draw_text(message, position, 75, "Green")
    canvas.draw_text(message_plays, [285,50], 40, "Blue")
    canvas.draw_text('Wins/Plays ->', (50, 50), 40, 'Gray', 'serif')
    
def update(text):
    global message
    message = text
    
def tick():
    global current_time
    current_time = current_time+1
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)

# register event handlers
frame.add_button("Start",start_timer,150)
frame.add_button("Stop", stop_timer,150)
frame.add_button("Reset", reset_timer,150)

# start frame
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()

# Please remember to review the grading rubric
