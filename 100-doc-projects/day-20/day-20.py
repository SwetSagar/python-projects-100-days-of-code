import turtle

screen= turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    segment = turtle.Turtle(shape='square')
    segment.color('white')
    segment.penup()
    segment.goto(position)
    segments.append(segment)
    
game_is_on = True

while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(20)
        
screen.exitonclick()