import pandas as pd
import os
import sys # ----------------------------- To handle system paths
sys.path.append('.') # ------------------- All paths till the current folder have alias as '.'

class Aircraft():
    '''Class defining the object
    Aircrafts. It will hold all
    the aircraft data and provide
    relevant methods to modify &
    maintain this data'''

    # Constructor for the Airport class
    def __init__(self):
        self.__aircraft_df = pd.DataFrame()
    
    # Accessor to get the Airport Data
    def get_AircraftData(self,path):
        """Return Airport Data"""
        if os.path.isfile(path):
            self.__aircraft_df = pd.read_csv(path, encoding='utf-8')  # Aircraft Data
            return self.__aircraft_df
        else:
            print("Aircraft File Not Found")
            return None
