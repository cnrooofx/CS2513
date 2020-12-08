"""CS2513 Assignment 2 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""

import tkinter as tk


class Game(tk.Frame):
    def __init__(self):
        super().__init__()

        self.lives = 5
        self.score = 0

        self.master.minsize(width=1280, height=800)
        self.master.title("Peekaboo")
        self.grid()
        self.createGame()

    def createGame(self):
        self.game = tk.Frame(self)
        self.game.grid(row=0, column=0)

        self.canvas = tk.Canvas(self.game, width=1230, height=650)
        self.canvas.pack(padx=25, pady=25)
        self.canvas.configure(bg="#e5e5e5")

        self.menu = tk.Frame(self)
        self.menu.grid(row=1, column=0, padx=5, pady=5)

        self.name_label = tk.Label(self.menu, text="Enter your name:")
        self.name_label.configure(padx=20, pady=10)
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.menu)
        self.name_entry.insert(0, "Player")
        self.name_entry.grid(row=0, column=1)

        self.play_btn = tk.Button(self.menu, text="Play!", command=self.play)
        self.play_btn.configure(padx=20, pady=10)
        self.play_btn.grid(row=1, column=1)

    def play(self):
        lives_string = "Lives: " + str(self.lives)
        self.lives_label = tk.Label(self.menu, text=lives_string)
        self.lives_label.configure(padx=20, pady=10)
        self.lives_label.grid(row=1, column=0)

        score_string = "Score: " + str(self.score)
        self.score_label = tk.Label(self.menu, text=score_string)
        self.score_label.configure(padx=20, pady=10)
        self.score_label.grid(row=1, column=2)

        print("playing")

    def addScore(self):
        if self.score < 999:
            self.score += 1
        self.score_label["text"] = "Score: " + self.score

    def loseALife(self):
        if self.lives > 1:
            self.lives -= 1
        else:
            self.gameoverMenu()
        self.lives_label["text"] = "Lives: " + str(self.lives)

    def gameOver(self):
        gameover_string = "Game Over! - Final Score: " + str(self.score)

        self.score_label.destroy()
        self.lives_label.destroy()

        self.new_btn = tk.Button(self.menu, text="New Game", command=self.newGame)
        self.new.configure(padx=20, pady=10)
        self.new_btn.grid(row=1, column=1)

        self.quit_btn = tk.Button(self.menu, text="Quit", command=self.exit)
        self.quit_btn.configure(padx=20, pady=10)
        self.quit_btn.grid(row=1, column=2)

        self.game_over_label = tk.Label(self.menu, text=gameover_string)
        self.game_over_label.configure(padx=20, pady=10)
        self.game_over_label.grid(row=0, column=1, columnspan=2)

    def newGame(self):
        self.lives = 5
        self.score = 0
        self.menu.destroy()
        self.game.destroy()
        self.createGame()

    def exit(self):
        self.master.destroy()


game = Game()
game.mainloop()
