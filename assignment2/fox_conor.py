"""CS2513 Assignment 2 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""

import tkinter as tk
import tkinter.font as font
from random import randint
from time import time


class Game(tk.Frame):
    """A game where you click a figure on the screen as fast as you can."""

    def __init__(self):
        """Initialise the game."""
        super().__init__()
        self.master.minsize(width=1280, height=800)
        self.master.title("Peekaboo")

        self.name = None
        self.lives = 5
        self.score = 0
        self.shape = tk.StringVar()
        self.shape.set("circle")
        self.difficulty = tk.IntVar()
        self.difficulty.set(1)  # 1 means Normal difficulty by default
        self.time = 2
        self.menu = None
        self.game = None
        self.width = 1230  # Width of the canvas
        self.height = 650  # Height of the canvas

        menu_bar = tk.Menu(self)  # Main menu
        # Menu for new game and exit
        game_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_command(label="Exit", command=self.exit)

        # Difficulty menu
        difficulty = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Difficulty", menu=difficulty)
        difficulty.add_radiobutton(label="Easy", variable=self.difficulty,
                                   value=0)
        difficulty.add_radiobutton(label="Normal", variable=self.difficulty,
                                   value=1)
        difficulty.add_radiobutton(label="Hard", variable=self.difficulty,
                                   value=2)

        # Menu for changing the shape of the figure
        shapes_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Shape", menu=shapes_menu)
        shapes_menu.add_radiobutton(label="Circle", variable=self.shape,
                                    value="circle")
        shapes_menu.add_radiobutton(label="Square", variable=self.shape,
                                    value="square")
        shapes_menu.add_radiobutton(label="Oval", variable=self.shape,
                                    value="oval")
        shapes_menu.add_radiobutton(label="Rectangle", variable=self.shape,
                                    value="rectangle")
        self.master.config(menu=menu_bar)  # Link to the root window
        self.grid()
        self.set_difficulty()
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

            self.canvas = tk.Canvas(self.game, bg="#e5e5e5")
            self.canvas.configure(width=self.width, height=self.height)
            self.canvas.pack(padx=25, pady=25)
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
        if self.name is not None:
            self.name_entry.insert(0, self.name)
        self.name_entry.grid(row=0, column=1)

        # Button to start the game
        self.play_btn = tk.Button(self.menu, text="Play!", command=self.play)
        self.play_btn.configure(padx=20, pady=10)
        self.play_btn.grid(row=1, column=1)

    def play(self):
        """Reconfigures the widgets and starts the game."""
        # Play button now starts a new game instead
        self.play_btn.configure(text="New Game", command=self.new_game)

        # Label to explain the rules
        rules = "Click on the red icon in under {} seconds".format(self.time)
        self.rules = tk.Label(self.menu, text=rules)
        self.rules.configure(padx=20, pady=10)
        self.rules.grid(row=0, column=0, columnspan=3)

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

        # Create the first figure, which starts the game
        self.new_figure()

    def new_figure(self):
        """Clear the canvas, make a new figure and start the timer."""
        canvas = self.canvas
        canvas.delete("all")

        size = randint(25, 50)
        size2 = randint(25, 50)
        x = randint(0, self.width - size)
        y = randint(0, self.height - size)
        colour = "red"

        self.start = time()  # Start of timer for the figure

        shape = self.shape.get()
        if shape == "circle":
            fig = canvas.create_oval(x, y, x+size, y+size, fill=colour)
        elif shape == "oval":
            fig = canvas.create_oval(x, y, x+size, y+size2, fill=colour)
        elif shape == "rectangle":
            fig = canvas.create_rectangle(x, y, x+size, y+size2, fill=colour)
        else:
            fig = canvas.create_rectangle(x, y, x+size, y+size, fill=colour)
        canvas.tag_bind(fig, "<ButtonPress-1>", self.click_handler)

    def click_handler(self, event):
        """Handle the callback for clicking on a figure."""
        end = time()
        time_elapsed = end - self.start

        if time_elapsed < 2:
            self.score += 1
        else:
            self.lives -= 1

        if self.lives <= 0:
            self.game_over()
        else:
            self.update_score()
            self.update_lives()
            self.new_figure()

    def update_score(self):
        """Update the score label with the current score."""
        self.score_label["text"] = "Score: " + str(self.score)

    def update_lives(self):
        """Update the lives label with the current number of lives."""
        self.lives_label["text"] = "Lives: " + str(self.lives)

    def set_difficulty(self):
        pass

    def game_over(self):
        """Stop the game."""
        self.canvas.delete("all")

        # Add the gameover message to the canvas
        gameover_font = font.Font(font=("Helvetica", 32))
        text = "Game Over {}! - Final Score: {}".format(self.name, self.score)
        self.canvas.create_text(615, 325, text=text, font=gameover_font)

        self.rules.destroy()
        self.score_label.destroy()
        self.lives_label.destroy()

        # Create the button to exit the game
        self.quit_btn = tk.Button(self.menu, text="Quit", command=self.exit)
        self.quit_btn.configure(padx=20, pady=10)
        self.quit_btn.grid(row=1, column=2, padx=10, pady=5)

    def exit(self):
        """Close the game window."""
        self.master.destroy()


game = Game()
game.mainloop()
