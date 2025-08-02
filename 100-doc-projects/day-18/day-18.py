import turtle as t
import random

timmy = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", 
         "Wheat", "SlateGray", "SeaGreen"]

timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for angle in range(0, 360, size_of_gap):
        timmy.color(random.choice(colors))
        timmy.setheading(angle)
        timmy.circle(100)

draw_spirograph(5)

t.exitonclick()