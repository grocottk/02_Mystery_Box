# Design taken from planning page.

from tkinter import *

# Beginning of Start class
class Start:
    def __init__(self, parent):

        # GUI to find starting balance and stakes from the user:
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (Row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Mystery Subheading (Row 1)
        self.mystery_subheading = Label(self.start_frame, text="Welcome to the Mystery Box Game",
                                       font="Arial 10")
        self.mystery_subheading.grid(row=1)

        # Text wrap and Justify code from "01_Help_GUI.py".
        # First Instruction (Row 2)
        self.first_instruction = Label(self.start_frame, text="Please enter a dollar amount in the box below (between 5 and 50).",
                                       font="Arial 10 italic", wrap=300,
                                       justify=LEFT)
        self.first_instruction.grid(row=2)

        # Entry Box (Row 3)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=3)

        # Text wrap and Justify code from "01_Help_GUI.py".
        # Second Instruction (Row 4)
        self.second_instruction = Label(self.start_frame, text="After you have entered this number, please choose your stakes. The higher stakes that you choose, the higher your possible winnings are.",
                                       font="Arial 10 italic", wrap=300,
                                       justify=LEFT)
        self.second_instruction.grid(row=4)
        
        # Inspired by "Conversion buttons frame" from "12g_Assembled_Program.py" as a part of "01_Temperature_Converter".
        # Stakes Buttons Frame (Row 5)
        self.stakes_buttons_frame = Frame(self.start_frame)
        self.stakes_buttons_frame.grid(row=5, pady=10)

        # Low Stakes Button (Row 0, Column 0)
        self.low_stakes_button = Button(self.stakes_buttons_frame,
                                        text="Low: $5.00",
                                        bg="#04E762") # Green
        self.low_stakes_button.grid(row=0, column=0, padx=10)

        # Medium Stakes Button (Row 0, Column 1)
        self.medium_stakes_button = Button(self.stakes_buttons_frame,
                                        text="Medium: $10.00")
        self.medium_stakes_button.grid(row=0, column=1, padx=10)

        # Low Stakes Button (Row 0, Column 2)
        self.high_stakes_button = Button(self.stakes_buttons_frame,
                                        text="High: $15.00")
        self.high_stakes_button.grid(row=0, column=2, padx=10)

        # Help Button (Row 6)
        self.help_button = Button(text="How to Play",
                                        command=lambda: self.to_game(1))
        self.help_button.grid(row=6, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)

# Beginning of Game class
class Game:
    def __init__(self, partner, stakes, starting_balance):

        # Prints variables for testing:
        print(stakes)
        print(starting_balance)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
