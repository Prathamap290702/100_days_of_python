from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 272)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT,
                   font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over." , align = ALIGNMENT, font= FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
