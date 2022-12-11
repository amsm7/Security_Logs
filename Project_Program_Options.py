from SecurityLogs import SecurityLogs
import pandas as pd


class ProgramOptions:

    def __init__(self, df):
        self.df = df

    @staticmethod
    def end_program():
        exit("Thank U very much for being with us!")

    @staticmethod
    def create_new_df():
        """Creating new data frame."""

        new_data = [['Wrong Password', '#50768', "Add to 'pass.log' file."],
                    ['Invalid User', '#30667', "Add to 'user.log' file."],
                    ["'Long' Login", '#40834', 'Block user for 15 minutes.']]
        data_frame2 = pd.DataFrame(new_data,
                                   columns=['Event Type', 'Event Code', 'Action'])
        return data_frame2

    def user_option(self, user_input):
        """Check user input and call to certain functions according to it."""

        SecurityLogs.quick_note()
        new_df = SecurityLogs(self.df.copy())
        new_df2 = ProgramOptions.create_new_df()
        while user_input <= 17:
            self.check_user_awareness(user_input)
            print("------------------------------------------")
            print(f"Entered step # {user_input}")
            if user_input == 1:
                SecurityLogs.original_data_frame(new_df)
            elif user_input == 2:
                SecurityLogs.create_and_mix_data(new_df)
            elif user_input == 3:
                SecurityLogs.filling_nulls(new_df)
            elif user_input == 4:
                SecurityLogs.delete_values(new_df)
            elif user_input == 5:
                SecurityLogs.delete_negatives(new_df)
            elif user_input == 6:
                SecurityLogs.new_data_frame(new_df2)
            elif user_input == 7:
                SecurityLogs.mapping_event_code(new_df, new_df2)
            elif user_input == 8:
                SecurityLogs.mapping_action(new_df, new_df2)
            elif user_input == 9:
                SecurityLogs.switching_columns(new_df)
            elif user_input == 10:
                SecurityLogs.removing_duplicate_rows(new_df)
            elif user_input == 11:
                SecurityLogs.printing_specific_column(new_df)
            elif user_input == 12:
                SecurityLogs.adding_spec_column(new_df)
            elif user_input == 13:
                SecurityLogs.removing_spec_column(new_df)
            elif user_input == 14:
                SecurityLogs.add_alert_column(new_df)
            elif user_input == 15:
                SecurityLogs.describe(new_df)
            elif user_input == 16:
                SecurityLogs.info(new_df)
            elif user_input == 17:
                SecurityLogs.save_to_csv(new_df)
            user_input += 1

        print(" \n# All rights reserved - Amir Sillam --> November - December 2022 \n")
        print("Hope you enjoyed our program !")
        ProgramOptions.end_program()

    @staticmethod
    def check_user_awareness(check_input):
        """Checking user input"""

        tries = 4
        print("------------------------------------------")
        check_user = input("Are you ready to step # ")
        while int(check_user) != check_input:
            if tries != 0:
                print(f"You have {tries} more tries.")
                check_user = input("Please try again :\n")
                tries -= 1
            else:
                print("That was your last try.")
                print("You are with use or not ?")
                print(f"You have tried {tries + 5} times, that's the limit.")
                exit("Try again next time, Thank you.")
