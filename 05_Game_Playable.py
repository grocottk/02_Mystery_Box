# Some lines of code are inspired by "02_Start_GUI.py"

from tkinter import *
from functools import partial # To prevent unwanted windows.
import random

# Beginning of Start class
class Start:
    def __init__(self, parent):

        # GUI to find starting balance and stakes from the user:
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Test Button (Row 0)
        self.push_me_button = Button(text="Press This", command=self.to_game)
        self.push_me_button.grid(row=0, pady=5)

    def to_game(self):

        # Retrieve starting balance
        starting_balance = 50
        stakes = 2

        Game(self, stakes, starting_balance)

        # Hide start up window
        root.withdraw()

class Game:
    def __init__(self, partner, stakes, starting_balance):

        print(stakes)
        print(starting_balance)

        # Initialise variables
        self.balance = IntVar()
        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # Get value of stakes (Use it as a multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading (Row 0)
        self.heading_label = Label(self.game_frame, text="Play", fomt="Arial 24 bold",
                                padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions label (Row 1)
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                    text="Please press the enter key or click the "
                                    "'Open Boxes' button to reveal the "
                                    "contents of the mystery boxes.",
                                    font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes space (Row 2)
        box_text = "Arial 16 bold"
        box_background = "#04E762" # Green (From "02_Start_GUI.py")
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize_one_label = Label(self.box_frame, text="?\n", font=box_text,
                                bg=box_background, width=box_width, padx=10, pady=10)
        self.prize_one_label.grid(row=0, column=0)

        self.prize_two_label = Label(self.box_frame, text="?\n", font=box_text,
                                bg=box_background, width=box_width, padx=10, pady=10)
        self.prize_two_label.grid(row=0, column=1)

        self.prize_three_label = Label(self.box_frame, text="?\n", font=box_text,
                                bg=box_background, width=box_width, padx=10, pady=10)
        self.prize_three_label.grid(row=0, column=2)

        # Play button (Row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg="#F5B700",
                            font="Arial 15 bold", width=20, padx=10, pady=10,
                            command=self.reveal_boxes) # Orange (From "02_Start_GUI.py")
        self.play_button.grid(row=3)

        # Balance label (Row 4)
        start_text = "Game Cost: ${} \n "" \nHow much " \
                        "will you win?".format(stakes * 5)
        
        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="#D5CFE1",
                                text=start_text, wrap=300, justify=LEFT) # Dark Grey (From "02_Start_GUI.py")
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Statistics button (Row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help/Rules",
                            font="Arial 15 bold", bg="#464655", fg="#D5CFE1") 
                            # Lilac Text, Dark Grey Button (From "02_Start_GUI.py")
        self.help_button.grid(row=0, column=0, padx=2)

        self.statistics_button = Button(self.help_export_frame, text="Game Statistics",
                                    font="Arial 15 bold", bg="#464655", fg="#D5CFE1") 
                                    # Lilac Text, Dark Grey Button (From "02_Start_GUI.py")
        self.statistics_button.grid(row=0, column=1, padx=2)
