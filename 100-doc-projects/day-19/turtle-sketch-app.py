import turtle as t

tim = t.Turtle()
screen  = t.Screen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(move_forward, key="w")
screen.onkey(move_backward, key="s")
screen.onkey(turn_left, key="a")
screen.onkey(turn_right, key="d")
screen.onkey(clear, key="c")
screen.exitonclick()