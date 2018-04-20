import pandas as pd
import os
import sys # ----------------------------- To handle system paths
sys.path.append('.') # ------------------- All paths till the current folder have alias as '.'

class Airport():
    '''Class defining the object
    Airports. It will hold all
    the airport data and provide
    relevant methods to modify &
    maintain this data'''

    # Constructor for the Airport class
    def __init__(self):
        self.__airport_df = pd.DataFrame()
    
    # Accessor to get the Airport Data
    def get_AirportData(self,path):
        """Return Airport Data"""
        if os.path.isfile(path):
            self.__airport_df = pd.read_csv(path, header=None, encoding='utf-8', names=[
                                        'ID', 'AirportName', 'CityName', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Elevation', 'TimeZone', 'FrctHours', 'Continent/Capital'])  # Airport Data
            return self.__airport_df
        else:
            print("Airport File Not Found")
            return None
