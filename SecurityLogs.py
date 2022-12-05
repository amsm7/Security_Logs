import random
import numpy as np
import pandas as pd


class SecurityLogs:

    def __init__(self, df):
        self.df = df

    @staticmethod
    def quick_note():
        """ **Note: Output of each step will be the top 30 rows of the data frame.
        You can see the whole data frame at the end, in CSV format file.
        Thank U and enjoy :)"""

        print("-------------------------------------------------------------------------------------------------------")
        print(SecurityLogs.quick_note.__doc__)
        print("------------------------------------------------------------------------------------------------------")

    def original_data_frame(self):
        """Step 1: Showing the first 20 rows of the original data frame."""
        print(SecurityLogs.original_data_frame.__doc__)
        print("------------------------------------------------------------------------------------")
        print(self.df.head(30))

    def mix_data(self):
        """Step 2: Creating and mixing new and wrong formats of data.
         1. Creating and filling new 'Event Code' column with random values, instead of unique ones.
         2. Creating and filing new 'Action' column with wrong data types.
         3. Subtract 'Total events' column values by 1000 (some will become negative."""

        event_code = np.array(['#2082', '#22878', '#2082', '#5053', '#9063', "#4852", None])
        self.df['Event Code'] = np.random.choice(event_code, 10000)

        action = np.array([False, None, 'No action', True, 567, '#123', 99])
        self.df['Action'] = np.random.choice(action, 10000)

        self.df['Total Events'] = self.df['Total Events'] - 1000

        print(SecurityLogs.mix_data.__doc__)
        print("-------------------------------------------------------------------------"
              "-----------------------------------------------------------------------")
        print(self.df.head(30))

    def filling_nulls(self):
        """Step 3: Filling  'None' Values with 'dump!' value."""

        self.df.fillna('dump!', inplace=True)

        print(SecurityLogs.filling_nulls.__doc__)
        print("-------------------------------------------------------------------------------------------------------------")
        print(self.df.head(30))

    def delete_values(self):
        """Step 4: Deleting every 'dump!' value from 'Event Type' column. """

        self.df.drop(self.df.index[self.df['Event Type'] == 'dump!'], inplace=True)
        print(SecurityLogs.delete_values.__doc__)
        print("------------------------------------------------------------------------------------------------------------------")
        print(self.df.head(30))

    def delete_negatives(self):
        """Step 5: Deleting all negative values from 'Total Events' column."""

        self.df = self.df.loc[self.df['Total Events'] >= 0]
        print(SecurityLogs.delete_negatives.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(30))

    @staticmethod
    def new_data_frame(new_df):
        """Step 6: Creating new Data frame and print it. """

        print(SecurityLogs.new_data_frame.__doc__)
        print("------------------------------------------------------------------------------")
        print(new_df.head(30))

    def mapping_event_code(self, df_2):
        """Step 7: Mapping new data frame values.
         1. 'Mapping correct  'Event Code' column values from the new data frame,
          instead of the original wrong values, that matches to their 'Event Type' value."""

        self.df.loc[self.df['Event Type'] == df_2['Event Type'][0], 'Event Code'] = df_2['Event Code'][0]
        self.df.loc[self.df['Event Type'] == df_2['Event Type'][1], 'Event Code'] = df_2['Event Code'][1]
        self.df.loc[self.df['Event Type'] == df_2['Event Type'][2], 'Event Code'] = df_2['Event Code'][2]

        print(SecurityLogs.mapping_event_code.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(30))

    def mapping_action(self, df_2):
        """Step 8: Mapping new data frame values.
         1. 'Mapping correct 'Action' column values from the new data frame,
          instead of the original wrong values, that matches to their 'Event Code' value."""

        self.df.loc[self.df['Event Code'] == df_2['Event Code'][0], 'Action'] = df_2['Action'][0]
        self.df.loc[self.df['Event Code'] == df_2['Event Code'][1], 'Action'] = df_2['Action'][1]
        self.df.loc[self.df['Event Code'] == df_2['Event Code'][2], 'Action'] = df_2['Action'][2]

        print(SecurityLogs.mapping_action.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(30).to_string())

    def switching_columns(self):
        """Step 9: Switch columns positions in the data frame """
        event_code_column = self.df.pop('Event Code')
        self.df.insert(2, 'Event Code', event_code_column)

        print(SecurityLogs.switching_columns.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(30).to_string())

    def removing_duplicate_rows(self):
        """Step 10: Removing Duplicated rows in data frame and keep the first appearance.
              * Filtering is done based on columns 'Host' ,'Date' and 'Event Type' values. """

        old_host_count = self.df['Event Type'].value_counts()
        self.df = self.df.drop_duplicates(
            subset=['Host', 'Date', 'Event Type'],
            keep='first').reset_index(drop=True)
        print(SecurityLogs.removing_duplicate_rows.__doc__)
        print("---------------------------------------------------")

        print("The difference:")
        print(f"Before removing duplicates: \n{old_host_count}")
        print("---------------------------------------------------")
        print(f"After removing duplicates: \n{self.df['Event Type'].value_counts()}")
        print("---------------------------------------------------")

    def printing_specific_column(self):
        """Step 11: Printing specific column the user will choose,
            counting and printing each value in it."""

        print("---------------------------------------------------------------------------------------------")
        print(SecurityLogs.printing_specific_column.__doc__)
        print("---------------------------------------------------------------------------------------------")

        count = 4
        titles = list(self.df.columns.values)
        for val in titles:
            print(f"{val}. ")
        print(" --------------------------------------------------")
        input_title = input("Enter the column you wish to see from the list: \n")
        while input_title not in titles:
            if count > 0:
                print(f"You have {count} more tries.")
                input_title = input("Please try again :\n")
                count -= 1
            else:
                exit("too many tries, run the program again.")

        print(self.df[input_title].head(30).to_string())

        print(f"\n# of values for each column member.")
        print(" --------------------------------------------------")
        print(self.df[input_title].value_counts())

    def adding_spec_column(self):
        """Step 12: Adding a column to the table, at a specific and random position.
            'Check' column has been added and filled with 'to remove' values."""

        rand_num = random.randint(0, (len(self.df.columns) - 1))

        self.df.insert(rand_num, 'Check', 'to remove')

        print("---------------------------------------------------------------------------------------------")
        print(SecurityLogs.adding_spec_column.__doc__)
        print(f"            Added a column at index # {rand_num}.\n")
        print("---------------------------------------------------------------------------------------------")

        print(f"{self.df.head(30).to_string()} \n")

    def removing_spec_column(self):
        """Step 13: Removing 'Check' column, that has been added at step 12. """

        self.df.drop(columns='Check', inplace=True)

        print("------------------------------------------------------------------------------")
        print(SecurityLogs.removing_spec_column.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.head(30).to_string()} \n")

    def add_alert_column(self):
        """Step 14:  Adding 'Alert' column which will categorize alert base on
         # of events in 'Total Events' column.
        1. if value in 'Total Events' column is equal or bigger than 1500 --> 'Red alert.
        2. if value in 'Total Events' column is between 500 to 1499) --> 'Orange alert.
        3. if value in 'Total Events' column is smaller than 500 --> 'Yellow alert.
        """

        conditions = [(self.df['Total Events'] >= 1500),
                      ((self.df['Total Events'] >= 500) & (self.df['Total Events'] < 1500)),
                      (self.df['Total Events'] < 500)]

        alerts = ["Red alert", "Orange alert", "Yellow alert"]
        self.df['Alert'] = np.select(conditions, alerts).copy()

        print(SecurityLogs.add_alert_column.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.head(30).to_string()} \n")

    def info(self):
        """Step 15: Showing the info of all columns in the data frame  . """

        print(SecurityLogs.info.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.info()} \n")
        pass

    def describe(self):
        """Step 16: Describe  . """

        print(SecurityLogs.describe.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.describe().astype('int')} \n")

    def save_to_csv(self):
        """Step 17: Saving the updated data frame to CSV file.  . """
        self.df.to_csv('my_df.csv', encoding='utf-8', index=False)
        print(SecurityLogs.save_to_csv.__doc__)


        print("------------------------------------------------------------------------------")

# security_log['Total_ev'] = pd.cut(security_log.TotalEvents, ranges, labels=names)
# print(f"{security_log} \n")
