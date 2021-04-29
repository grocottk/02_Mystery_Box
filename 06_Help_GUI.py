# Import Statements
from tkinter import *

from functools import partial  # To prevent unwanted windows (being created)

import random

# Help GUI inspired by "01_Help_GUI.py"

class Converter:

    def __init__(self, parent):

        # Formatting variables...
        background_color = "grey"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)...
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "18", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (Row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "12"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)

if __name__ == '__main__':
    class Help:

        # Set up initial function
        def __init__(self, partner):

            background = "orange"

            # Disable help button
            partner.help_button.config(state=DISABLED)

            # Sets up child window (or help box)
            self.help_box = Toplevel()

            # If users press cross at the top of the window, help closes and the help button 'releasrs'
            self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

            # Set up GUI Frame
            self.help_frame = Frame(self.help_box, bg=background)
            self.help_frame.grid()

            # Help heading (Row 0)
            self.how_heading = Label(self.help_frame,
                                     text="Help/Instructions",
                                     font="Arial 16 bold",
                                     bg=background)
            self.how_heading.grid(row=0)

            # Help text definition
            help_text = "Choose an amount to play with and then choose the stakes. " \
                        "Higher stakes cost more per round, but you can win more as well." \
                        "When you enter the play area, you will see three mystery boxes. " \
                        "To reveal the contents of these boxes, " \
                        "click the Open Boxes " \
                        "button toward the bottom of the window. If you don't have enough money to"  \
                        "the button will turn red," \

            # Help text (Label, Row 1)
            self.help_text = Label(self.help_frame, text=help_text,
                                justify=LEFT, width=40,
                                bg=background, wrap=250)
            self.help_text.grid(row=1)

            # Dismiss button (Row 2)
            self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                         width =10, bg="pink", font="arial 10 bold",
                                         command=partial(self.close_help, partner))
            self.dismiss_button.grid(row=2, pady=10)

        # Defining close_help function
        def close_help(self, partner):

            # Put help button back into a normal state..
            partner.help_button.config(state=NORMAL)
            self.help_box.destroy()

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
