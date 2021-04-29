# Code partially inspired by "12a_History_GUI.py"

from tkinter import *

from functools import partial  # To prevent unwanted windows (being created)

import random

class Game:
    def __init__(self, parent):

        # Formatting variables... (This gives the hard coded starting and ending balance(s) respectively.)
        self.game_statistics_list = [50, 6]

        # In the actual program. this will be blank, and populated with user calculation(s)
        self.round_statistics_list = ['Silver\n($4.00) | Lead\n($0.00) | Lead\n($0.00) - Cost: $10.00 | Payback: $4.00 | Current Balance: $44.00', 
                                        'Lead\n($0.00) | Lead\n($0.00) | Gold\n($10.00) - Cost: $10.00 | Payback: $10.00 | Current Balance: $44.00', 
                                        'Lead\n($0.00) | Copper\n($2.00) | Copper\n($2.00) - Cost: $10.00 | Payback: $4.00 | Current Balance: $38.00', 
                                        'Copper\n($2.00) | Silver\n($4.00) | Lead\n($0.00) - Cost: $10.00 | Payback: $6.00 | Current Balance: $34.00', 
                                        'Lead\n($0.00) | Silver\n($4.00) | Lead\n($0.00) - Cost: $10.00 | Payback: $4.00 | Current Balance: $28.00', 
                                        'Copper\n($2.00) | Silver\n($4.00) | Silver\n($4.00) - Cost: $10.00 | Payback: $10.00 | Current Balance: $28.00', 
                                        'Copper\n($2.00) | Silver\n($4.00) | Copper\n($2.00) - Cost: $10.00 | Payback: $8.00 | Current Balance: $26.00', 
                                        'Copper\n($2.00) | Copper\n($2.00) | Lead\n($0.00) - Cost: $10.00 | Payback: $4.00 | Current Balance: $20.00', 
                                        'Lead\n($0.00) | Copper\n($2.00) | Silver\n($4.00) - Cost: $10.00 | Payback: $6.00 | Current Balance: $16.00', 
                                        'Copper\n($2.00) | Lead\n($0.00) | Silver\n($4.00) - Cost: $10.00 | Payback: $6.00 | Current Balance: $12.00', 
                                        'Lead\n($0.00) | Lead\n($0.00) | Silver\n($4.00) - Cost: $10.00 | Payback: $4.00 | Current Balance: $6.00']

        # Statistics Main Screen GUI...
        self.game_frame = Frame()
        self.game_frame.grid()

        # Statistics Heading (Row 0)...
        self.heading_label = Label(self.game_frame,
                                          text="Play...",
                                          font=("Arial 18 bold"),
                                          padx=10, pady=10)
        self.heading_label.grid(row=0)

        # History Button (Row 1)
        self.statistics_button = Button(self.game_frame, text="Game Statistics",
                                     font=("Arial 14"),
                                     padx=10, pady=10,
                                     command=lambda: self.to_statistics(self.round_statistics_list, self.game_statistics_list))
        self.statistics_button.grid(row=1)

    def to_statistics(self, game_history, game_statistics):
        GameStatistics(self, game_history, game_statistics)

class GameStatistics:

    # Set up initial function
    def __init__(self, partner, game_history, game_statistics):

        print(game_history)

        # Disable history button
        partner.statistics_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (or statistics box)
        self.statistics_box = Toplevel()

        # If users press cross at the top of the window, statistics closes and the statistics button 'releases'
        self.statistics_box.protocol('WM_DELETE_WINDOW', partial(self.close_statistics, partner))

        # Set up GUI Frame
        self.statistics_frame = Frame(self.statistics_box)
        self.statistics_frame.grid()

        # Set up Statistics heading (Row 0)
        self.statistics_heading_label = Label(self.statistics_frame,
                                    text="Game Statistics",
                                    font="arial 19 bold")
        self.statistics_heading_label.grid(row=0)

        # To Export [Instructions] (Row 1)
        self.export_instructions = Label(self.statistics_frame,
                                    text="Here are your Game Statistics. "
                                            "Please use the Export button to "
                                            "access tge results of each "
                                            "round that you played",
                                    justify=LEFT, fg="green",
                                    font="arial 10 italic", wrap=250,
                                    padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Statistics Frame (Row 2)
        self.details_frame = Frame(self.statistics_frame)
        self.details_frame.grid(row=2)

        # Starting Balance Heading (Row 0, Column 0)
        self.starting_balance_label = Label(self.details_frame, text="Starting Balance:",
                                        font=heading, anchor="e")
        self.starting_balance_label.grid(row=0, column=0, padx=0)

        # Starting Balance Text (Row 0, Column 1)
        self.starting_balance_value_label = Label(self.details_frame, font=content,
                                                    text="${}".format(game_statistics[0]),
                                                    anchor="w")
        self.starting_balance_value_label.grid(row=0, column=1, padx=0)

        # Current Balance Heading (Row 1, Column 0)
        self.current_balance_label = Label(self.details_frame, text="Current Balance:",
                                            font=heading, anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        # Current Balance Text (Row 1, Column 1)
        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                    text="${}".format(game_statistics[1]),
                                                    anchor="w")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        # To find whether a win or loss has occured
        if game_statistics[1] > game_statistics[0]:
            win_or_loss = "Amount Won:"
            amount = game_statistics[1] - game_statistics[0]
            win_or_loss_fg = "green"
        else:
            win_or_loss = "Amount Lost:"
            amount = game_statistics[0] - game_statistics[1]
            win_or_loss_fg = "red"

        # Amount won or lost Heading (Row 2, Column 0)
        self.win_or_loss_label = Label(self.details_frame, text=win_or_loss,
                                            font=heading, anchor="e")
        self.win_or_loss_label.grid(row=2, column=0, padx=0)

        # Amount won or lost Text (Row 2, Column 1)
        self.win_or_loss_value_label = Label(self.details_frame, font=content,
                                                    text="${}".format(amount),
                                                    fg=win_or_loss_fg,
                                                    anchor="w")
        self.win_or_loss_value_label.grid(row=2, column=1, padx=0)

        # Rounds Played Heading (Row 3, Column 0)
        self.games_played_label = Label(self.details_frame, text="Rounds Played:",
                                            font=heading, anchor="e")
        self.games_played_label.grid(row=3, column=0, padx=0)

        # Rounds Played Text (Row 3, Column 1)
        self.games_played_value_label = Label(self.details_frame, font=content,
                                                    text=len(game_history),
                                                    anchor="w")
        self.win_or_loss_value_label.grid(row=3, column=1, padx=0)

        # Dismiss button [From "00_Compiled_Version_2.py"] (Row 4)
        self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                        width =10, bg="pink", font="arial 10 bold",
                                        command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=4, pady=10)



# From "02_Start_GUI.py"
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Game(root)
    root.mainloop()
