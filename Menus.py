from termcolor import colored
import pandas as pd
import numpy as np


class Menus:

    def __init__(self):
        pass

    @staticmethod
    def menu_input():
        """ User menu input."""
        message_start = 'Run the show!'
        print("---------------------------------------------------")
        print(f"Opening message is: {message_start}  ")
        print("---------------------------------------------------")
        user_input = input(colored(" Please enter c-o-r-r-e-c-t-l-y the 'Opening message' ", 'green'))
        count = 1
        while user_input != message_start:
            if count > 4:
                print(f"You have tried {count} times, that's the limit.")
                exit("Try again next time, Thank you.")
            count += 1
            print("Look for the 'opening message' at the beginning of the program.")
            user_input = input(colored("Please enter the 'Opening message' ", 'green'))

        return 1

    @staticmethod
    def options_menu():
        print("\n ------- Security------Logs----By--Amir--Sillam---- \n"
              "                                                                              \n"
              " 1. Show original Data Frame.                         \n"
              " 2. Make Data Frame messy (not messi :) )  \n"
              " 3. Filling every 'NaN' values with 'dump!' string type value.                \n"
              " 4. Deleting every 'dump!' value from 'Event Type' column.              \n"
              " 5. Deleting every negative value from 'Total Events' column. \n"
              " 6. Create new Data frame. \n"
              " 7. Merge new data frame with the original according to same columns.          \n"
              " 8. Fill new columns with new and correct values.        \n"
              " 9. Return the host with the most events and type. \n"
              " 10.Count the total of each 'Event Type'  log. \n"
              " 11.End program.                                                    \n"
              " 12.End program.                                                    \n"
              " 13.End program.                                                    \n"
              " 14.End program.                                                    \n"
              " 15.End program.                                                    \n"
              "---------------------------------------------------------------------")

    @staticmethod
    def instructions_menu():
        # Print menu message.
        print(" -------------------------------------------- \n "
              " ** Program instructions ** \n"
              "In this program, the user will see data frame\n"
              "with 'Nan' values, making data frame\n"
              "unorganized, with missing values.\n"
              "The Program will remove 'wrong' \n"
              "values and fill the data frame with new ones.\n"
              "Then we will make many kinds of manipulation,\n"
              "With our complete and interesting data.  Enjoy the ride :)\n"
              "-------------------------------------------- ")
