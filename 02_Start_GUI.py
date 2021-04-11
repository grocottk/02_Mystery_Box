# Design taken from planning page.

from tkinter import *

# Beginning of Start class
class Start:
    def __init__(self, parent):

        # From "02_Converter_GUI.py"
        background = "#D5CFE1" # Lilac

        # GUI to find starting balance and stakes from the user:
        self.start_frame = Frame(padx=10, pady=10, bg=background)
        self.start_frame.grid()

        # Mystery Heading (Row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box",
                                       font="Arial 19 bold",
                                       bg=background, fg="#464655") # Dark Grey
        self.mystery_box_label.grid(row=0)

        # Mystery Subheading (Row 1)
        self.mystery_subheading = Label(self.start_frame, text="Welcome to the Mystery Box Game",
                                       font="Arial 10", bg=background, fg="#464655") # Dark Grey
        self.mystery_subheading.grid(row=1)

        # Text wrap and Justify code from "01_Help_GUI.py".
        # First Instruction (Row 2)
        self.first_instruction = Label(self.start_frame, text="Please enter a dollar amount in the box below (between 5 and 50).",
                                       font="Arial 10 italic", wrap=300,
                                       justify=LEFT, bg=background, fg="#464655") # Dark Grey
        self.first_instruction.grid(row=2)

        # Entry Box, Button and Error Label Frame (Row 3)
        self.entry_error_frame = Entry(self.start_frame, width=200)
        self.entry_error_frame.grid(row=3)

        # Entry Box
        self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 14 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        # Add Funds Button
        self.add_funds_button = Button(self.entry_error_frame, font="Arial 14 bold", text="Add funds",
                                command=self.check_funds)
        self.add_funds_button.grid(row=0, collumn=1)

        # Error Message
        self.amount_error_label = Label(self.entry_error_frame, fg="#FF5733", text="",
                                        font="Arial 10 bold", wrap=300,
                                        justify=LEFT) # Bright Red
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # Text wrap and Justify code from "01_Help_GUI.py".
        # Second Instruction (Row 4)
        self.second_instruction = Label(self.start_frame, text="After you have entered this number, please choose your stakes. The higher stakes that you choose, the higher your possible winnings are.",
                                       font="Arial 10 italic", wrap=300,
                                       justify=LEFT, bg=background, fg="#464655") # Dark Grey
        self.second_instruction.grid(row=4)
        
        # Inspired by "Conversion buttons frame" from "12g_Assembled_Program.py" as a part of "01_Temperature_Converter".
        # Stakes Buttons Frame (Row 5)
        self.stakes_buttons_frame = Frame(self.start_frame, bg=background)
        self.stakes_buttons_frame.grid(row=5, pady=10)

        # Low Stakes Button (Row 0, Column 0)
        self.low_stakes_button = Button(self.stakes_buttons_frame,
                                        command=lambda: self.to_game(1),
                                        text="Low: $5.00",
                                        bg="#04E762", fg="#464655") # Dark Grey Text, Green Button
        self.low_stakes_button.grid(row=0, column=0, padx=10)

        # Medium Stakes Button (Row 0, Column 1)
        self.medium_stakes_button = Button(self.stakes_buttons_frame,
                                        command=lambda: self.to_game(2),
                                        text="Medium: $10.00",
                                        bg="#F5B700", fg="#464655") # Dark Grey Text, Orange Button
        self.medium_stakes_button.grid(row=0, column=1, padx=10)

        # High Stakes Button (Row 0, Column 2)
        self.high_stakes_button = Button(self.stakes_buttons_frame,
                                        command=lambda: self.to_game(3),
                                        text="High: $15.00",
                                        bg="#00A1E4", fg="#464655") # Dark Grey Text, Blue Button
        self.high_stakes_button.grid(row=0, column=2, padx=10)

        # Disable all stakes buttons at start of program
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # Help Button (Row 6)
        self.help_button = Button(self.start_frame, text="How to Play", fg="#D5CFE1",
                                    command=lambda: self.to_game(4),
                                    bg="#464655") # Lilac Text, Dark Grey Button
        self.help_button.grid(row=6, pady=10)

    def check_funds(self):
    starting_balance = self.start_amount_entry.get()
    
    # Set error background colours (and assume that there are no errors at the start)
    error_background="#FFCCBB" # Pink
    has_errors = "no"

    # Change background to white (for testing purposes)
    self.start_amount_entry.config(bg="#D5CFE1") # Lilac
    self.amount_error_label.config(text="")

    # Disable all stakes buttons at start of program
    self.low_stakes_button.config(state=DISABLED)
    self.medium_stakes_button.config(state=DISABLED)
    self.high_stakes_button.config(state=DISABLED)

    try:
        starting_balance = int(starting_balance)

        if starting_balance < 5:
            has_errors = "yes"
            error_feedback = "Sorry, the lowest amount that you can play the game with is $5.00."

        elif starting_balance > 50:
            has_errors = "yes"
            error_feedback = "Sorry, the most that you can risk in this game is $50.00."

        elif starting_balance >= 15:
            # Enable all buttons
            self.low_stakes_button.config(state=NORMAL)
            self.medium_stakes_button.config(state=NORMAL)
            self.high_stakes_button.config(state=NORMAL)
        
        elif starting_balance > = 10:
            # Enable low and medium stakes buttons
            self.low_stakes_button.config(state=NORMAL)
            self.medium_stakes_button.config(state=NORMAL)

        else:
            self.low_stakes_button.config(state=NORMAL)
        
    except ValueError:
        has_errors = "yes"
        error_feedback = "Please enter a dollar amount (Text and decimal numbers are not allowed)."

    if has_errors == "yes":
        self.start_amount_entry.config(bg=error_background)
        self.amount_error_label.config(text=error_feedback)

    else:
        # Set starting balance to amount entered by user
        self.starting_funds.set(starting_balance)
    
    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        
        # Set error background colours (and assume that there are no errors at the start)
        error_background="#FFCCBB" # Pink
        has_errors = "no"

        # Change background to white (for testing purposes)
        self.start_amount_entry.config(bg="#D5CFE1") # Lilac
        self.amount_error_label.config(text="")

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the lowest amount that you can play the game with is $5.00."

            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Sorry, the most that you can risk in this game is $50.00."

            elif starting_balance < 10 and (stakes == 2 or stakes == 3):
                has_errors = "yes"
                error_feedback = "Sorry, you can only afford to play a low stakes game."
            
            elif starting_balance < 15 and stakes == 3:
                has_errors = "yes"
                error_feedback = "Sorry, you can onlu afford to play a low or medium stakes game."

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (Text and decimal numbers are not allowed)."

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_background)
            self.amount_error_label.config(text=error_feedback)
        
        else:
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
