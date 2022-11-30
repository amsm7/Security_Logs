# All rights reserved - Amir Sillam - November 2022

from ProgramOptions import ProgramOptions
from Menus import Menus
import pandas as pd
import numpy as np

def run_program(df):
    # new = sns.countplot(x = 'Reason' , data = df)
    # plt.show()

    input_obj = Menus()
    input_obj.instructions_menu()
    input_obj.options_menu()

    user_input = input_obj.menu_input()

    #SecurityLogs(df)
    df_obj = ProgramOptions(df)
    df_obj.user_option(user_input)

def creating_data_frame():
    # Creating new Data frame with just column names.
    data_frame = pd.DataFrame(
        columns=['Host', 'Event Type', 'Total Events'])

    # Creating 2 NumPy arrays
    hosts = np.array(['host1', 'host2', 'host3', 'host4', 'host5', 'host6', 'host7', 'host8', 'host9', 'host10'])
    event_type = np.array(['Wrong Password', 'Invalid User', " 'Long' Login " , None])

    # Filling the data frame with different data types.
    data_frame['Host'] = np.random.choice(hosts, 10000)
    data_frame['Event Type'] = np.random.choice(event_type, 10000)
    data_frame['Total Events'] = np.random.randint(0, 2500, 10000)
    run_program(data_frame)


creating_data_frame()

































