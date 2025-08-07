import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen= turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# Bind the keys to the snake's movement methods

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment_score()
        snake.add_segment()
        
        # scoreboard.increase_score()  # Increment the score
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over", align="center", font=("Courier", 24, "normal"))
        
        # Detect collision with the snake itself
        # If head collides with tail then trigger game_over
        for segment in snake.segments[1:]:
            # Check if the head collides with any segment
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.write("Game Over", align="center", font=("Courier", 24, "normal"))
                break
        
screen.exitonclick()