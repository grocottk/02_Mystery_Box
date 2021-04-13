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
        root.start_frame.destroy()

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

        # Bind button to 'enter' key (so that users can press enter to reveal the boxes).
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())

        # End of Play button
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

        # Quit button (Row 6)
        self.quit_button = Button(self.game_frame, text="Quit", fg="#D5CFE1",
                                    bg="#F5B700", font="Arial 15 bold", width=20,
                                    command=self.to_quit, padx=10)
                                    # Lilac Text, Orange Button (From "02_Start_GUI.py")
        self.quit_button.grid(row=6, pady=10)

    # Parts taken from "04_Prize_Generation.py"
    def reveal_boxes(self):
        # Retrieve the balance from the initial function
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        # (Backgrounds used are for testing purposes, and are temporary.)
        round_winnings = 0
        prizes = []
        button_backgrounds = []
        for item in range(0, 3):
            prize_number = random.randint(1, 100)

            # This is a 5% chance of gold.
            if 0 < prize_number <= 5:
                prize = "Gold\n(${}.00)".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
                background_colour = "red"

            # This is a 20% chance of silver.
            elif 5 < prize_number <= 25:
                prize = "Silver\n(${}.00)".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
                background_colour = "yellow"
            
            # This is a 40% chance of getting copper.
            elif 25 < prize_number <= 65:
                prize = "Copper\n(${}.00)".format(1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
                background_colour = "blue"
            
            # If none of the above are true, the prize is Lead, worth $0.00
            else:
                prize = "Lead\n($0.00)"
                background_colour = "purple"

            prizes.append(prize)
            button_backgrounds.append(background_colour)

        # Display prizes and change colour(s)
        self.prize_one_label.config(text=prizes[0], bg=button_backgrounds[0])
        self.prize_two_label.config(text=prizes[1], bg=button_backgrounds[1])
        self.prize_three_label.config(text=prizes[2], bg=button_backgrounds[2])

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}.00\nPayback: ${} \n" \
                            "Current Balance: ${}.00".format(5 * stakes_multiplier, 
                            round_winnings, current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

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
