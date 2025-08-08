from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update()
    
    def get_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
        
    def increase_level(self):
        self.level += 1
        self.score += 10
        
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
                
        self.update()    
    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level} | Score: {self.score} | High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
                
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        
        
