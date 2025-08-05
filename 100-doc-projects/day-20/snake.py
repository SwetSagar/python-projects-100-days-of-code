import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20



class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITION:
            segment = turtle.Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
            
    def move(self):
        
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        
                