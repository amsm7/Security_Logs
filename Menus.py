
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
        user_input = input(" Please enter c-o-r-r-e-c-t-l-y the 'Opening message' ")
        count = 1
        while user_input != message_start:
            if count > 4:
                print(f"You have tried {count} times, that's the limit.")
                exit("Try again next time, Thank you.")
            count += 1
            print("Look for the 'opening message' at the beginning of the program.")
            user_input = input("Please enter the 'Opening message' ")

        return 1

    @staticmethod
    def options_menu():
        print("\n -------Security------Logs------By-----Amir----Sillam-----2022------ \n"
              "                                                                              \n"
              " 1. Show original Data Frame.\n"
              " 2. Make Data Frame messy (not messi :) )  \n"
              " 3. Filling every 'NaN' values with 'dump!' string type value.\n"
              " 4. Deleting every 'dump!' value from 'Event Type' column.\n"
              " 5. Deleting every negative value from 'Total Events' column.\n"
              " 6. Create new Data frame. \n"
              " 7. Mapping values to 'Event Code' column from new Data frame.\n"
              " 8. Mapping values to 'Action' column from new Data frame.\n"
              " 9. Switch columns positions in the data frame. \n"
              " 10. Removing Duplicated rows in data frame. \n"
              " 11. Showing specific column that the user will choose.\n"
              " 12. Adding a column to the data frame.\n"
              " 13. Removing a column at this specific position.\n"
              " 14. Adding 'Alert' column based on values from 'Total Events'.\n"
              " 15. Showing statistical description of numerical values.\n"
              " 16. Showing the info of all columns in the data frame.\n"
              " 17. Saving the updated data frame to a CSV file.\n"
              "----------------------------------------------------------------------------------------------")

    @staticmethod
    def instructions_menu():
        # Print program instructions .
        print("-------------------------------------------- \n "
              " ** Program instructions ** \n"
              ""
              "In this program, the user will see data frame\n"
              "with 'Nan' values, making data frame\n"
              "unorganized, with missing values.\n"
              "Remove 'wrong' and duplicated \n"
              "values and fill the data frame with new ones.\n"
              "Creating new columns, mapping from new data \n"
              "frame, showing data and save it to new CSV file.\n"
              "The user should be focused because in every step\n"
              "he should be aware of the steps(not of the stairs)\n"
              "that we are in the program, it's like a game to make the\n"
              "user more focused and to enjoy the program. \n"
              "In the program, like in life, there is no shortcuts to success :)\n"
              "You need to pass every step to complete the program.\n"
              "Enjoy the ride :)\n"
              "---------------------------------------------------------")

    @staticmethod
    def program_description():
        print("\n# All rights reserved - Amir Sillam --> November - December 2022 \n")
        # Print program description menu.
        print("--------------------------------------------------\n"
        "** Program description ** \n"
        "This program simulates a log file in which\n"
        "information is collected regarding failed\n"
        "login attempts to various websites\n"
        "and their documentation.\n"
        "--------------------------------------------------\n")
