import turtle

turtle.title("Turtle Drawing")
turtle.bgcolor("black")
turtle.pensize(2)
def draw_square(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()