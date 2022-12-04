import random

import pandas as pd
import numpy as np


class SecurityLogs:

    def __init__(self, df):
        self.df = df

    def original_data_frame(self):
        """Step 1: Showing the first 20 rows of the original data frame."""
        print(SecurityLogs.original_data_frame.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    def mix_data(self):
        """Step 2: Creating and mixing new and wrong formats of data.
         1. Creating and filling new 'Event Code' column with random values, instead of unique ones.
         2. Creating and filing new 'Action' column with wrong data types.
         3. Subtract 'Total events' column values by 1000 (some will become negative).
            """
        event_code = np.array(['#2082', '#22878', '#2082', '#5053', '#9063', "#4852", None])
        self.df['Event Code'] = np.random.choice(event_code, 10000)

        action = np.array([False, None, 'No action', True, 567, '#123', 99])
        self.df['Action'] = np.random.choice(action, 10000)

        self.df['Total Events'] = self.df['Total Events'] - 1000

        print(SecurityLogs.mix_data.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))
        """future columns = ['Alert type', 'Date','Time']) """

    def filling_nulls(self):
        """Step 3: Filling  'None' Values with 'dump!' value."""

        self.df.fillna('dump!', inplace=True)

        print(SecurityLogs.filling_nulls.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    def delete_values(self):
        """Step 4: Deleting every 'dump!' value from 'Event Type' column. """

        self.df.drop(self.df.index[self.df['Event Type'] == 'dump!'], inplace=True)
        print(SecurityLogs.delete_values.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    def delete_negatives(self):
        """Step 5: Deleting all negative values from 'Total Events' column."""

        self.df = self.df.loc[self.df['Total Events'] >= 0]
        print(SecurityLogs.delete_negatives.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    @staticmethod
    def new_data_frame(new_df):
        """Step 6: Creating new Data frame and print it. """

        print(SecurityLogs.new_data_frame.__doc__)
        print("------------------------------------------------------------------------------")
        print(new_df.head(20))

    def mapping_event_code(self, df_2):
        """ Step 7: Mapping new data frame values.
         1. 'Mapping correct  'Event Code' column values from the new data frame,
          instead of the original wrong values, that matches to their 'Event Type' value."""

        self.df.loc[self.df['Event Type'] == df_2['Event Type'][0], 'Event Code'] = df_2['Event Code'][0]
        self.df.loc[self.df['Event Type'] == df_2['Event Type'][1], 'Event Code'] = df_2['Event Code'][1]
        self.df.loc[self.df['Event Type'] == df_2['Event Type'][2], 'Event Code'] = df_2['Event Code'][2]

        print(SecurityLogs.mapping_event_code.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    def mapping_action(self, df_2):
        """ Step 8: Mapping new data frame values.
         1. 'Mapping correct 'Action' column values from the new data frame,
          instead of the original wrong values, that matches to their 'Event Code' value."""

        self.df.loc[self.df['Event Code'] == df_2['Event Code'][0], 'Action'] = df_2['Action'][0]
        self.df.loc[self.df['Event Code'] == df_2['Event Code'][1], 'Action'] = df_2['Action'][1]
        self.df.loc[self.df['Event Code'] == df_2['Event Code'][2], 'Action'] = df_2['Action'][2]

        print(SecurityLogs.mapping_action.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    def fill_date(self):
        """ Step 9: Add 'Date' column with date ranges of the events. """
        random_dates = np.array(pd.date_range('2022/11/01', '2022/11/30'))

        # self.df.assign(Date = random_dates )
        self.df.loc[:, 'Date'] = random_dates
        # self.df["Date"] = np.random.choice(random_dates, len(self.df))

        print(SecurityLogs.fill_date.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    def printing_specific_column(self):
        """ Step 10: Printing specific column the user will choose
            and counting and printing each value in it."""

        print("------------------------------------------------------------------------------")
        print(SecurityLogs.printing_specific_column.__doc__)
        print(" --------------------------------------------------")

        count = 4
        titles = list(self.df.columns.values)
        for val in titles:
            print(f"{val}. ")
        print(" --------------------------------------------------")
        input_title = input("Enter the column you wish to see from the list: \n\n")
        while input_title not in titles:
            if count > 0:
                print(f"You have {count} more tries.")
                input_title = input("Please try again :\n")
                count -= 1
            else:
                exit("too many tries, run the program again.")

        print(self.df[input_title].head(50))

        print(f"\n# of values for each column member.")
        print(" --------------------------------------------------")
        print(self.df[input_title].value_counts())

    def adding_spec_column(self):
        """ Step 11: Adding a column to the table, at a specific and random position
          ** We added the 'Check' column and 'to remove' values in it. """

        rand_num = random.randint(0, (len(self.df.columns) - 1))
        self.df.insert(rand_num, 'Check', 'to remove')

        print("------------------------------------------------------------------------------")
        print(SecurityLogs.adding_spec_column.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"Added a column at index # {rand_num}.\n")
        print(f"{self.df.head(20).to_string()} \n")

    def removing_column(self):
        """ Step 12: Removing column at specific place in the table. """

        print("Removing Columns in the table.\n")
        self.df.drop(['Check'], axis=1, inplace=True)

        print("------------------------------------------------------------------------------")
        print(SecurityLogs.removing_column.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.head(20).to_string()} \n")

    def info(self):
        """ Step 13: Showing the info of all columns in the data frame  . """

        print(SecurityLogs.info.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.info()} \n")

    def add_alert_column(self):
        """ Step 14:  Add new column to the data frame. .
        Adding 'Alert ** column which will categorize alert base on # of events in 'Total Events' column."""

        # self.df['Total Events'] = self.df['Total Events'] - 1000

        self.df['Alert**'] = ['Red Alert' if val > 1500 else 'Orange Alert' if 500 <= val < 1499 else
        'Yellow Alert' for val in self.df['Total Events']]

        print(SecurityLogs.add_alert_column.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.head(20).to_string()} \n")

    def describe(self):
        """ Step 15: Describe  . """

        print(SecurityLogs.describe.__doc__)
        print("------------------------------------------------------------------------------")
        print(f"{self.df.describe().astype('int')} \n")

    def save_to_csv(self):
        self.df.to_csv('my_df.csv', encoding='utf-8', index=False)


