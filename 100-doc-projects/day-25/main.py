import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(f"x: {x}, y: {y}")

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()