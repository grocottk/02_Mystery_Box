# Code partially inspired by "12a_History_GUI.py"

from tkinter import *

from functools import partial  # To prevent unwanted windows (being created)

import random

class Game:

    def __init__(self, parent):

        # Formatting variables...
        self.game_statistics_list = [50, 6]

        # In the actual program. this will be blank, and populated with user calculation(s)
        self.round_statistics_list = ['Lead\n($0.00) | Lead\n($0.00) | Silver\n($4.00) - Cost: $10.00 | Payback: $4.00 | Current Balance: $34.00', 
                                        'Copper\n($2.00) | Copper\n($2.00) | Copper\n($2.00) - Cost: $10.00 | Payback: $6.00 | Current Balance: $30.00', 
                                        'Lead\n($0.00) | Lead\n($0.00) | Lead\n($0.00) - Cost: $10.00 | Payback: $0.00 | Current Balance: $20.00', 
                                        'Silver\n($4.00) | Copper\n($2.00) | Lead\n($0.00) - Cost: $10.00 | Payback: $6.00 | Current Balance: $16.00', 
                                        'Lead\n($0.00) | Silver\n($4.00) | Lead\n($0.00) - Cost: $10.00 | Payback: $4.00 | Current Balance: $10.00', 
                                        'Copper\n($2.00) | Lead\n($0.00) | Silver\n($4.00) - Cost: $10.00 | Payback: $6.00 | Current Balance: $6.00']

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
                                     command=lambda: self.to_statistics(self.round_statistics_list))
        self.statistics_button.grid(row=1)

    def to_statistics(self, game_history, game_statistics):
        GameStatistics(self, game_history, game_statistics)

class GameStatistics:

    # Set up initial function
    def __init__(self, game_history, game_statistics):

        print(game_history)

        # Disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (or history box)
        self.history_box = Toplevel()

        # If users press cross at the top of the window, history closes and the history button 'releases'
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (Row 0)
        self.how_heading = Label(self.history_frame,
                                    text="Calculation History",
                                    font="arial 19 bold",
                                    bg=background)
        self.how_heading.grid(row=0)

        # History text (Label, Row 1)
        self.history_text = Label(self.history_frame,
                                    text="Here are the most recently completed calculations."
                                        " Please use the export button to create a text file"
                                        " of all your calculations for this session (if desired).",
                                    font="arial 10 italic",
                                    justify=LEFT, width=40, fg="orange",
                                    bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Dismiss button (Row 2)
        self.dismiss_button = Button(self.history_frame, text="Dismiss",
                                        width=10, bg="orange", font="arial 10 bold",
                                        command=partial(self.close_history, partner))

        # History output: (Row 2)

        # Generate string from list of calculations:
        history_string = ""

        # Defining "empty string"
        if len(calculation_history) >= 7:
            for item in range(0, 7):
                history_string += calculation_history[len(calculation_history)
                                                        - item - 1]+"\n"

        # This code may come into effect when a small number of "calculation_history"
        # ... entries have been created.
        else:
            for item in calculation_history:
                history_string += calculation_history[len(calculation_history) -
                                                        calculation_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here are your complete calculations."
                                                " Please use the export button to create a text file"
                                                " of the calculations for this session (if desired).")

        # Label to display calculation history to user
        self.calculation_label = Label(self.history_frame, text=history_string,
                                        bg=background, font="Arial 12", justify=LEFT)
        self.calculation_label.grid(row=2)

        # Export / Dismiss buttons frame (Row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                        # (use of 'partner' parameter from 01_Help_GUI.py)
                                        font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    # Closes history
    def close_history(self, partner):

        # Put history button back to normal:
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    # Show user their [calculation] history (Row 2)


# From "02_Start_GUI.py"
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Game(root)
    root.mainloop()
