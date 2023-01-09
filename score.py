from turtle import Turtle
from tkinter import Tk
ARANJARE = "center"
FONT = ('Arial', 14, 'normal')
MOVE = False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scor = 0
        self.high_score = 0
        with open("data.txt", mode="r") as self.file:
            data_scor = int(self.file.read())
            print(data_scor)
            self.high_score = data_scor
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(arg=f"Scor: {self.scor} High score: {self.high_score}", move=MOVE, align=ARANJARE, font=FONT)

    def modify_scor(self):
        self.clear()
        self.scor += 1
        self.update_score()

    def reset_score(self):
        if self.scor > self.high_score:
            with open("data.txt", mode="w") as self.file:
                self.file.write(str(self.high_score))
        self.scor = 0
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Te-ai lovit de zid! Game over!", move=MOVE, align=ARANJARE, font=FONT)

    def game_over_muscat(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Te-ai muscat de coada! Game over!", move=MOVE, align=ARANJARE, font=FONT)






