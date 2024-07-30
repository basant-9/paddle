import turtle

# Create window
wind = turtle.Screen()
wind.title("Pong Game") 
wind.bgcolor("black")
wind.setup(width=800, height=500)

# Paddle 1
paddel1 = turtle.Turtle()
paddel1.speed(0)
paddel1.shape("square")
paddel1.color("red")
paddel1.shapesize(stretch_wid=6, stretch_len=1)
paddel1.penup()
paddel1.goto(-350, 0)

# Paddle 2
paddel2 = turtle.Turtle()
paddel2.speed(0)
paddel2.shape("square")
paddel2.color("green")
paddel2.shapesize(stretch_wid=6, stretch_len=1)
paddel2.penup()
paddel2.goto(350, 0)

# Paddle 1 up and down 
def paddel1_up():
    y = paddel1.ycor() # get y coordinate of the paddle1
    y += 20  # set the y to increase by 20 
    paddel1.sety(y) # set the y of paddle1 to the new y coordinate 

def paddel1_down():
    y = paddel1.ycor() 
    y -= 20    # set the y to  decrease by 20 
    paddel1.sety(y)

# Keyboard
wind.listen() # tell the window to expect input 
wind.onkeypress(paddel1_up, "w") # by pressing w , function paddel1_up is invoked 
wind.onkeypress(paddel1_down, "s")

# Main loop 
while True:
    wind.update() # updates the screen everytime the loop run 