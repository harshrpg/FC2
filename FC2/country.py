import pandas as pd
import os
import sys # ----------------------------- To handle system paths
sys.path.append('.') # ------------------- All paths till the current folder have alias as '.'


class Country():
    '''Class defining the object
    Countries. It will hold all
    the Country-currency data and provide
    relevant methods to modify &
    maintain this data'''

    # Constructor for the Currency class
    def __init__(self):
        self.__countryCurrency_df = pd.DataFrame()

    # Accessor to get the Currency Data
    def get_CountryData(self,path):
        if os.path.isfile(path):
            self.__countryCurrency_df = pd.read_csv(
                path, encoding='utf-8')  # Country
            return self.__countryCurrency_df
        else:
            print("Country File Not Found")
            return None
