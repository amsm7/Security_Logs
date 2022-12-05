# All rights reserved - Amir Sillam --> November - December 2022

from ProgramOptions import ProgramOptions
from Menus import Menus
import pandas as pd
import numpy as np

def run_program(df):

    input_obj = Menus()
    input_obj.instructions_menu()
    input_obj.options_menu()

    user_input = input_obj.menu_input()

    df_obj = ProgramOptions(df)
    df_obj.user_option(user_input)


def creating_data_frame():
    """ Creating new Data frame with just column names. """
    data_frame = pd.DataFrame(
        columns=['Host', 'Event Type', 'Total Events', 'Date'])


    """Creating 3 NumPy arrays"""
    hosts = np.array(['host1', 'host2', 'host3', 'host4', 'host5',
                      'host6', 'host7', 'host8', 'host9', 'host10',
                      'host11', 'host12', 'host13', 'host14', 'host15',
                      'host16', 'host17', 'host18', 'host19', 'host20',
                      'host21', 'host22', 'host23', 'host24', 'host25'])
    event_type = np.array(['Wrong Password', 'Invalid User', "'Long' Login", None])
    random_dates = np.array(pd.date_range('2022/11/01', '2022/12/03'))

    """Filling the data frame with different data types."""
    data_frame['Host'] = np.random.choice(hosts, 10000)
    data_frame['Event Type'] = np.random.choice(event_type, 10000)
    data_frame['Total Events'] = np.random.randint(0, 3000, 10000)
    data_frame['Date'] = np.random.choice(random_dates, 10000)
    df_copy = data_frame.copy()
    run_program(df_copy)


creating_data_frame()
