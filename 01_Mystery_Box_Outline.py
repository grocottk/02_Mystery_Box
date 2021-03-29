# Initial outline from Support Files.

from tkinter import *
import random

# The following has been done to prevent unwanted windows
from functools import partial


# Beginning of Start class
class Start:
    def __init__(self, parent):

        # GUI to find starting balance and stakes from the user:
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (Row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Entry Box (Row 1)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=1)

        # Play Button (Row 2)
        self.low_stakes_button = Button(text="Low: $5",
                                        command=lambda: self.to_game(1))
        self.low_stakes_button.grid(row=2, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


# Beginning of Game class
class Game:
    def __init__(self, partner, stakes, starting_balance):

        # Prints variables for testing:
        print(stakes)
        print(starting_balance)

        partner.low_stakes_button.config(state=DISABLED)


# Test class from template
class Foo:
    def __init__(self, parent):
        print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Foo(root)
    root.mainloop()
