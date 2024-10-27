from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            contents=file.read()
            self.highscore= int(contents)

        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,280)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",move=False,align="center",font=('Courier', 13, 'normal'))
    def increment_score(self):
        self.score+=1
        self.display_score()



    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.display_score()


