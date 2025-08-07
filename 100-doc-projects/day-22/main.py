## Creating a ping pong game using turtle graphics
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball   
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = Ball()  # Create a ball instance
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Here you would typically add logic for the ball movement and collision detection
    # For simplicity, we are just keeping the paddle moving up and down
    ball.move()  # Assuming you have a ball class with a move method
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #Detect collision with paddles
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    
    def reset_position():
        ball.goto(0, 0)
        ball.bounce_x()
        
    # Detectif the ball goes out of bounds
    if ball.xcor() > 390 : 
        scoreboard.l_point()
        reset_position() 
    
    
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()

