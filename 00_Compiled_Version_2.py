# Initial outline from Support Files.

from tkinter import *
import random

# The following has been done to prevent unwanted windows
from functools import partial

# Beginning of Start class
class Start:
    def __init__(self, parent):

        # From "02_Converter_GUI.py"
        background = "#D5CFE1" # Lilac

        self.starting_funds = IntVar()
        self.starting_funds.set(0)

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
        self.entry_error_frame = Frame(self.start_frame, width=200, bg=background)
        self.entry_error_frame.grid(row=3)

        # Entry Box
        self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 14 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        # Add Funds Button
        self.add_funds_button = Button(self.entry_error_frame, font="Arial 14 bold", text="Add funds",
                                command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1)

        # Error Message
        self.amount_error_label = Label(self.entry_error_frame, fg="#FF5733", text="", bg=background,
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
                                        font="Arial 10 bold",
                                        text="Low: $5.00",
                                        bg="#04E762", fg="black") # Black Text, Green Button
        self.low_stakes_button.grid(row=0, column=0, padx=10)

        # Medium Stakes Button (Row 0, Column 1)
        self.medium_stakes_button = Button(self.stakes_buttons_frame,
                                        command=lambda: self.to_game(2),
                                        font="Arial 10 bold",
                                        text="Medium: $10.00",
                                        bg="#F5B700", fg="black") # Black Text, Orange Button
        self.medium_stakes_button.grid(row=0, column=1, padx=10)

        # High Stakes Button (Row 0, Column 2)
        self.high_stakes_button = Button(self.stakes_buttons_frame,
                                        command=lambda: self.to_game(3),
                                        font="Arial 10 bold",
                                        text="High: $15.00",
                                        bg="#00A1E4", fg="black") # Black Text, Blue Button
        self.high_stakes_button.grid(row=0, column=2, padx=10)

        # Disable all stakes buttons at start of program
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # Help Button (Row 6) [Removed]
    
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
            
            elif starting_balance >= 10:
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

        # Retrieve starting balance
        starting_balance = self.start_amount_entry.get()

        Game(self, stakes, starting_balance)

        # Hide start up window (From "05_Game_Playable.py")
        self.start_frame.destroy()

# Beginning of Game class
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

        # List got holding statistics
        self.round_statistics_list = []

        # GUI Setup
        self.game_box = Toplevel()

        # If users press cross at top, the game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading (Row 0)
        self.heading_label = Label(self.game_frame, text="Play", font="Arial 24 bold",
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
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="question.gif")

        self.prize_one_label = Label(self.box_frame, image=photo, padx=10, pady=10)
        self.prize_one_label.photo = photo
        self.prize_one_label.grid(row=0, column=0)

        self.prize_two_label = Label(self.box_frame, image=photo, padx=10, pady=10)
        self.prize_two_label.photo = photo
        self.prize_two_label.grid(row=0, column=1)

        self.prize_three_label = Label(self.box_frame, image=photo, padx=10, pady=10)
        self.prize_three_label.photo = photo
        self.prize_three_label.grid(row=0, column=2)

        # Play button (Row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg="#04E762", fg="#464655",
                            font="Arial 15 bold", width=20, padx=10, pady=10,
                            command=self.reveal_boxes) # Green Button with Dark Grey Text (From "02_Start_GUI.py")

        # Bind button to 'enter' key (so that users can press enter to reveal the boxes).
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())

        # End of Play button
        self.play_button.grid(row=3)

        # Balance label (Row 4)
        start_text = "Game Cost: ${} \n "" \nHow much " \
                        "will you win?".format(stakes * 5)
        
        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="#464655",
                                text=start_text, wrap=300, justify=LEFT) # Dark Grey Text (From "02_Start_GUI.py")
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

        # Quit button (Row 6)
        self.quit_button = Button(self.game_frame, text="Quit", fg="black",
                                    bg="#F5B700", font="Arial 15 bold", width=20,
                                    command=self.to_quit, padx=10)
                                    # Black Text, Orange Button (From "02_Start_GUI.py")
        self.quit_button.grid(row=6, pady=10)

    # Parts taken from "04_Prize_Generation.py"
    def reveal_boxes(self):
        # Retrieve the balance from the initial function
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        # (Backgrounds used are for testing purposes, and are temporary.)
        round_winnings = 0
        prizes = []
        statistics_prizes = []
        for item in range(0, 3):
            prize_number = random.randint(1, 100)

            # This is a 5% chance of gold.
            if 0 < prize_number <= 5:
                prize = PhotoImage(file="gold_low.gif")
                prize_list = "Gold\n(${}.00)".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier

            # This is a 20% chance of silver.
            elif 5 < prize_number <= 25:
                prize = PhotoImage(file="silver_low.gif")
                prize_list = "Silver\n(${}.00)".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
                      
            # This is a 40% chance of getting copper.
            elif 25 < prize_number <= 65:
                prize = PhotoImage(file="copper_low.gif")
                prize_list = "Copper\n(${}.00)".format(1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
            
            # If none of the above are true, the prize is Lead, worth $0.00
            else:
                prize = PhotoImage(file="lead.gif")
                prize_list = "Lead\n($0.00)"

            prizes.append(prize)
            statistics_prizes.append(prize_list)
        
        photo_one = prizes[0]
        photo_two = prizes[1]
        photo_three = prizes[2]

        # Display prizes and change colour(s)
        self.prize_one_label.config(image=photo_one)
        self.prize_one_label.photo = photo_one
        self.prize_two_label.config(image=photo_two)
        self.prize_two_label.photo = photo_two
        self.prize_three_label.config(image=photo_three)
        self.prize_three_label.photo = photo_three

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}.00\nPayback: ${} \n" \
                            "Current Balance: ${}.00".format(5 * stakes_multiplier, 
                            round_winnings, current_balance)
        
        # Add round results to statistics list
        round_summary = "{} | {} | {} - Cost: ${}.00 | " \
                        "Payback: ${}.00 | Current Balance: ${}.00".format(
                            statistics_prizes[0], 
                            statistics_prizes[1], 
                            statistics_prizes[2],
                            5 * stakes_multiplier, round_winnings, current_balance)
        self.round_statistics_list.append(round_summary)
        print(self.round_statistics_list)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement, fg="#464655") # Dark Grey Text (From "02_Start_GUI.py")

        # Concludes game is remaining funds are too low.
        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}.00\n" \
                                "Your balance is too low. Your only options are to quit " \
                                "or view your statistics. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="red", font="Arial 10 bold", text=balance_statement)

    def to_quit(self):
        root.destroy()

# From "02_Start_GUI.py"
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
