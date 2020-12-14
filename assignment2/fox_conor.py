"""CS2513 Assignment 2 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""

import tkinter as tk


class Game(tk.Frame):
    """A game where you click a figure on the screen as fast as you can."""

    def __init__(self):
        """Initialise the game."""
        super().__init__()

        self.name = "Player"
        self.lives = 5
        self.score = 0
        self.menu = None
        self.game = None

        self.width = 1280
        self.height = 800

        self.master.minsize(width=self.width, height=self.height)
        self.master.title("Peekaboo")
        self.grid()
        self.new_game()

    def new_game(self):
        """Create all the widgets needed for a new game."""
        self.lives = 5
        self.score = 0
        if self.menu:
            self.menu.destroy()
        if not self.game:
            # Frame for the canvas
            self.game = tk.Frame(self)
            self.game.grid(row=0, column=0)

            self.canvas = tk.Canvas(self.game, width=1230, height=650)
            self.canvas.pack(padx=25, pady=25)
            self.canvas.configure(bg="#e5e5e5")
        else:
            self.canvas.delete("all")

        # Frame for the menu of buttons
        self.menu = tk.Frame(self)
        self.menu.grid(row=1, column=0, padx=5, pady=5)

        # Input box to take the user's name
        self.name_label = tk.Label(self.menu, text="Enter your name:")
        self.name_label.configure(padx=20, pady=10)
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.menu)
        # self.name_entry.insert(0, "Player")
        self.name_entry.grid(row=0, column=1)

        # Button to start the game
        self.play_btn = tk.Button(self.menu, text="Play!", command=self.play)
        self.play_btn.configure(padx=20, pady=10)
        self.play_btn.grid(row=1, column=1)

    def play(self):
        """Reconfigures the widgets and starts the game."""
        # Play button now starts a new game instead
        self.play_btn.configure(text="New Game", command=self.game_over)

        # Label to show remaining lives
        self.lives_label = tk.Label(self.menu)
        self.lives_label.configure(padx=20, pady=10)
        self.lives_label.grid(row=1, column=0)
        self.update_lives()

        # Label to show the total score
        self.score_label = tk.Label(self.menu)
        self.score_label.configure(padx=20, pady=10)
        self.score_label.grid(row=1, column=2)
        self.update_score()

        # Get the user's name from the input box
        name = self.name_entry.get()
        if name:
            self.name = name
        else:
            self.name = "Player"
        self.name_entry.destroy()
        self.name_label.destroy()

        print("playing", self.name)
        # square = self.canvas.create_text(100, 100, text="Playing")
        # square.configure(justify="center", font={Arial 20 bold})

        # Create the first figure, which starts the game

    def new_figure(self):
        """Clear the canvas and make a new figure."""
        self.canvas.delete("all")

    def click_handler(self):
        """Handle the callback for clicking on a figure."""

    def update_score(self):
        """Update the score label with the current score."""
        self.score_label["text"] = "Score: " + str(self.score)

    def update_lives(self):
        """Update the lives label with the current number of lives."""
        self.lives_label["text"] = "Lives: " + str(self.lives)

    def game_over(self):
        """Stop the game."""
        self.canvas.delete("all")

        # Add the gameover message to the canvas
        gameover_font = tk.font.Font(font=("Helvetica", 24))
        text = "Game Over {}! - Final Score: {}".format(self.name, self.score)
        self.canvas.create_text(615, 325, text=text, font=gameover_font)

        self.score_label.destroy()
        self.lives_label.destroy()

        self.quit_btn = tk.Button(self.menu, text="Quit", command=self.exit)
        self.quit_btn.configure(padx=20, pady=10)
        self.quit_btn.grid(row=1, column=2, padx=10, pady=5)

    def exit(self):
        """Close the game window."""
        self.master.destroy()


game = Game()
game.mainloop()
