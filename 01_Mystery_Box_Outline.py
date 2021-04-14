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

        # Disable low stakes button
        partner.low_stakes_button.config(state=DISABLED)

        # Initialise variable(s):
        self.balance = IntVar()

        # Set starting balance to amount entered by user at the start of the game.
        self.balance.set(starting_balance)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Game Heading (Row 0)
        self.game_heading_label = Label(self.game_frame, text="Mystery Box Play Area",
                                       font="Arial 24 bold", padx=10, pady=10)
        self.game_heading_label.grid(row=0)

        # Balance Frame (Row 1)
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)
        
        # Balance Label (Row 2)
        self.balance_label = Label(self.game_frame, text="Balance: $_.__")
        self.balance_label.grid(row=2)

        # Play Button (Row 3)
        self.play_button = Button(self.game_frame, text="Gain",
                                    padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

    def reveal_boxes(self):
        # Retrieve the balance from the initial function:
        current_balance = self.balance.get()

        # Adjust the balance (subtract the game cost and payout)
        # [For testing purposes, this adds two (2) to the overall balance.]
        current_balance += 2

        # Set balance to adjusted balance
        self.balance.set(current_balance)

        # Edit label so that the user can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
