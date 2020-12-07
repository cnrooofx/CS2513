"""CS2513 Assignment 2 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""

import tkinter as tk


class Game(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.minsize(height=650, width=1000)
        self.master.title("Peekaboo")
        self.grid()
        self.createGame()

    def createGame(self):
        self.game = tk.Frame(self)
        self.game.grid(row=0, column=0)

        self.canvas = tk.Canvas(self.game, width=950, height=525)
        self.canvas.pack(padx=25, pady=25)
        self.canvas.configure(bg="lightgray")

        self.menu = tk.Frame(self)
        self.menu.grid(row=1, column=0, padx=5, pady=5)

        self.play_btn = tk.Button(self.menu, text="Play", command=self.play)
        self.play_btn.configure(padx=20, pady=10)
        self.play_btn.grid(row=0, column=1)

    def closeMenu(self):
        if self.menu:
            self.menu.destroy()
            self.menu = None

    def play(self):
        self.lives_label = tk.Label(self.menu, text="Lives: 5")
        self.lives_label.configure(padx=20, pady=10)
        self.lives_label.grid(row=0, column=0)

        self.score_label = tk.Label(self.menu, text="Score: 0")
        self.score_label.configure(padx=20, pady=10)
        self.score_label.grid(row=0, column=2)

        print("playing")

    def addScore(self, increment=1):
        score = self.score_label["text"]
        score = score.split(":")
        score_number = int(score[1].strip())
        if score_number < 999:
            score_number += increment
        score = score[0] + ": " + str(score_number)
        self.score_label["text"] = score

    def loseALife(self):
        lives = self.lives_label["text"]
        lives = lives.split(":")
        lives_number = int(lives[1].strip())
        if lives_number > 1:
            lives_number -= 1
        else:
            self.gameoverMenu()
        lives = lives[0] + ": " + str(lives_number)
        self.lives_label["text"] = lives

    def gameoverMenu(self):
        pass

    def exit(self):
        self.master.destroy()


game = Game()
game.mainloop()
