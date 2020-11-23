"""CS2513 Assignment 2 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""

import tkinter as tk


class Figure():
    def __init__(self, clickable=False):
        self._colour = "blue"
        self._figure = None

    def draw(self):
        self._figure = canv.create_oval(100, 100, 300, 300, fill=self._colour)

    def delete(self):
        if self._figure:
            canv.delete(self._figure)
    pass


def game():
    figure = Figure()
    figures_list.append(figure)
    for figure in figures_list:
        figure.draw()
    return


def delete():
    for figure in figures_list:
        figure.delete()


figures_list = []
root = tk.Tk()
root.minsize(height=600, width=1000)
root.title("Peekaboo")

# Create the canvas
canv = tk.Canvas(root, width=950, height=500)
canv.configure(bg="lightgray")
canv.pack(padx=25, pady=25)
# Create the start button
start_button = tk.Button(root, text="Play!", command=game)
start_button.configure(padx=20, pady=10)
start_button.pack()

delete_button = tk.Button(root, text="delete", command=delete)
delete_button.pack()


def create_game():
    pass


create_game()
root.mainloop()
