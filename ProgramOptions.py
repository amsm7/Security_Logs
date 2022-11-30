from SecurityLogs import SecurityLogs
import pandas as pd


class ProgramOptions:

    def __init__(self, df):
        self.df = df

    @staticmethod
    def create_new_df():
        new_data = [['Wrong Password', '#50768', "Add to 'pass.log' file."],
                    ['Invalid User', '#30667', "Add to 'user.log' file."],
                    [" 'Long' Login", '#40834', 'Block user for 15 minutes.']]
        data_frame2 = pd.DataFrame(new_data,
                                   columns=['Event Type', 'Event Code', 'Action'])
        return data_frame2
        # future columns = [ 'Event Code', 'Alert type', 'Date','Time', 'Action'])

    def user_option(self, user_input):
        new_df = SecurityLogs(self.df)
        new_df2 = ProgramOptions.create_new_df()
        new_df3 = SecurityLogs(new_df2)
        # Check user input and call to certain functions according to it.
        while user_input <= 11:
            print("---------------------------------")
            print(f"Entered step # {user_input}")
            if user_input == 1:
                SecurityLogs.original_data_frame(new_df)
            elif user_input == 2:
                SecurityLogs.mix_data(new_df)
            elif user_input == 3:
                SecurityLogs.filling_nulls(new_df)
            elif user_input == 4:
                SecurityLogs.delete_values(new_df)
            elif user_input == 5:
                SecurityLogs.delete_negatives(new_df)
            elif user_input == 6:
                SecurityLogs.new_data_frame(new_df3)
            elif user_input == 7:
                print("ill be back - jump to next level;")
                #SecurityLogs.merge_data_frames(new_df, new_df2)
            elif user_input == 8:
                SecurityLogs.fill_date(new_df)
            elif user_input == 9:
                SecurityLogs.count_reasons(new_df)
            elif user_input == 10:
                SecurityLogs.add_new_values2(new_df)
            elif user_input == 11:
                SecurityLogs.save_to_csv('my_file.csv')
            user_input += 1
            self.check_user_awareness(user_input)

    @staticmethod
    def check_user_awareness(check_input):
        tries = 4
        print(" --------------------------------------------------")
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


