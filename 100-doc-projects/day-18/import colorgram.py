# import colorgram

import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract("/Users/swetsagar/Documents/GitHub/python-projects/100-doc-projects/day-18/image.jpg", 30)



# for color in colors : 
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(203, 171, 107), (221, 227, 234), (152, 181, 196), (193, 161, 176), (151, 187, 174), (233, 242, 239), (214, 204, 111), (207, 179, 198), (163, 202, 214), (174, 189, 213), (159, 214, 188), (113, 123, 186), (215, 180, 180), (181, 160, 66), (97, 97, 97), (99, 97, 98), (42, 42, 42), (200, 206, 44), (41, 39, 40), (129, 127, 128), (65, 63, 64), (101, 113, 153)]

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()


timmy.setheading(270)
timmy.forward(250)
timmy.setheading(0)
number_of_dots = 100


for dot_count in range(10):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()

    