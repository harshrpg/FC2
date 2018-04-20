import pandas as pd
import os
import sys # ----------------------------- To handle system paths
sys.path.append('.') # ------------------- All paths till the current folder have alias as '.'

class Currency():
    '''Class defining the object
    Currency. It will hold all
    the currency data and provide
    relevant methods to modify &
    maintain this data'''

    # Constructor for the Currency class
    def __init__(self):
        self.__currency_df = pd.DataFrame()

    # Accessor to get the Currency Data
    def get_CurrencyData(self,path):
        if os.path.isfile(path):
            self.__currency_df = df2 = pd.read_csv(
                path, header=None, encoding='utf-8', names=['Name', 'Code', 'toEUR', 'fromEUR'])  # Currency
            return self.__currency_df
        else:
            print("Currency File Not Found")
            return None
