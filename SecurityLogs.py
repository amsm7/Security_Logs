import pandas as pd
import numpy as np


class SecurityLogs:
    count = 0

    def __init__(self, df):
        print(SecurityLogs.count)
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

    def new_data_frame(self):
        """Step 6: Creating new Data frame """

        print(SecurityLogs.new_data_frame.__doc__)
        print("------------------------------------------------------------------------------")
        print(self.df.head(20))

    """ Step 7: Merge new data frame with the original according to same columns. """

    def merge_data_frames(self, df_2):
        #self.df[self.df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
        #for i in range(len(self.df)):
          #  print([self.df['Event Type'].values[i] == 'Wrong Password')]


        print(self.df.head(20))

    """ Step 8: Add 'Date' column with date ranges of the events. """

    def fill_date(self):
        random_dates = np.array(pd.date_range('2022/11/01', '2022/11/30'))
        self.df["Date"] = np.random.choice(random_dates, len(self.df))
        print(self.df.head(20))

    def printing_specific_column(self):
        print()
        titles = list(self.df.columns.values)
        for val in titles:
            print(f" '{val}'. ")
        input_title = input("Write your column you want to see from the list.")
        while input_title not in titles:
            input_title = input("You must insert only valid columns,try again please.\n")
        print(self.df[input_title])
        print(self.df['Date'])

    def replace_values(self):
        self.df.fillna(130, inplace=True)

    def time_stamp(self):
        pass


    def fill_alert_type(self):
        pass

    def fill_action(self):
        pass

    def count_reasons(self):
        print(self.df['Reason'].value_counts())

    def info(self):
        print("Info.\n")
        info = self.df.info()
        print(f"{info} \n")

    def describe(self):
        """Describe method"""
        print("Describe.\n")
        desc = self.df.describe()
        print(f"{desc} \n")

    def casting(self):
        """Cast method"""
        print("Casting.\n")
        desc_cast = self.df.describe().astype('int')
        print(f"{desc_cast} \n")


    def adding_spec_column(self):
        """Adding column at specific place in the table."""
        print("Adding a column to the table, at a specific position.\n")
        self.df.insert(0, "User", 'Not available')
        print(f"{self.df} \n")

    def removing_column(self):
        print("Removing Columns in the table.\n")
        self.df.drop(['User', 'Time'], axis=1, inplace=True)
        print(f"{self.df} \n")

    def terms(self):
        """Add some basic terms to out data."""
        print("Add some basic terms to our data.\n")
        self.df['Red Alert**'] = \
            np.where(self.df['TotalEvents'] >= 2000, True, False)
        print(f"{self.df} \n")

    def save_to_csv(self):
        self.df.to_csv('my_df.csv', index=False)

# security_log['Total_ev'] = pd.cut(security_log.TotalEvents, ranges, labels=names)
# print(f"{security_log} \n")
