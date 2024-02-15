from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'bold') 

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.clear()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.goto(0, 280)
        self.write(f'Score: {self.score}',True, align=ALIGNMENT, font=FONT)
