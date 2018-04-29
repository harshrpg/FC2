import csv
import pandas as pd
import numpy as np
from colorama import init
from termcolor import colored
import csv
import os
init()
class Utility:
    
    """Utility for FC2. Resposnible for arbitrary functions like, clean data merge data. Check for errors etc..."""

    def __init__(self):
        self.__testRoutes = [] # ---------------- List which will hold the test routes provided as inputs
        self.__airports_List = [] # ------------- A list to hold the airports
        self.__aircraft = None # ---------------- Variable for Aircraft
        self.__cleanedInput = [] # -------------- Clean input values
        self.__merged = pd.DataFrame() # -------- DataFrame to hold merged data
    
    # Reads Test Input File
    def handleTestInput(self,path):
        self.displayStatusFormatMessage(
            "\tReading File: ", params=path)
        self.displayStatusFormatMessage("\tTest: Duplicate Airport")
        with open(path,'r') as csvfile:
            airports = csv.reader(csvfile)
            for i,rows in enumerate(airports):
                # Check for duplicates
                if len(rows) != len(set(rows)):
                    self.displayErrFormatMessage(
                        "\tDuplicate Airports Found in Input: ", params=rows)
                else:
                    self.__testRoutes.append(rows)
        csvfile.close()
        self.displaySuccessFormatMessage("\tTest: Duplicate Airport -- COMPLETE")
        return self.__testRoutes
    
    # Handles Errors from the test input file
    def checkInputErrors(self,testAirports,allAirports,allAircrafts):
        self.displayStatusFormatMessage(
            "\tChecking for data Errors in: ", params=testAirports)
        # ---------- 1. Check if there is a Aircraft provided then split the aircraft and airports
        testAircraft = testAirports[-1] # ----------------------------------- Check The last item in the list (Expected position for a Aircraft)
        isAircraft = allAircrafts['code'].isin([testAircraft]) # ------------ Check if this item is in our Aircrafts Data
        self.displayStatusFormatMessage("\tTest: Aircraft Provided?")
        if (np.sum(isAircraft)==0): # --------------------------------------- If Aircraft not found in the data, then aircraft not provided
            self.displayWarningFormatMessage(
                "\tAircraft Not Provided in: ", params=testAirports)  # Display Message to user
            self.__airports_List = testAirports # --------------------------- If not an aircraft then must be all airports
            self.__aircraft = None
        elif (np.sum(isAircraft)==1): # ------------------------------------- If an aircraft is found
            self.__aircraft = testAircraft # -------------------------------- Then set it to aircraft
            self.__airports_List = testAirports[:-1] # ---------------------- Set the airports to all the values except the last one
        self.displaySuccessFormatMessage(
            "\tTest: Aircraft Provided? -- COMPLETE")
        # ---------- 2. Check the number of airports
        self.displayStatusFormatMessage("\tTest: Number of Airports Provided")
        lengthAirports = len(self.__airports_List) # ------------------------ Length of the airports list
        if not (lengthAirports>=2 and lengthAirports<=5): # ----------------- There must be atleast 2 airports and maximum of 5 airports
            self.displayErrFormatMessage(
                "\tThere number of airports provided is not between 2 and 5: ", params=self.__airports_List)
        else:
            # ------ 3. If the number of airports is right. Check if they are present in the data
            isAirports = allAirports['IATA'].isin(self.__airports_List) # --- Check if the airports provided is in our data
            if (np.sum(isAirports)==lengthAirports): # ---------------------- If all the airports are present
                self.__cleanedInput = self.__airports_List # ---------------- Final Cleaned input
            else:
                self.displayErrFormatMessage(
                    "Error in the Airports provided in the test file. Not in the airports_new.csv file")
        self.displaySuccessFormatMessage("\tTest: Number of Airports Provided -- COMPLETE")
        self.displaySuccessFormatMessage(
            "\tData Checks Completed in: ", params=testAirports)
        return (self.__cleanedInput,self.__aircraft) # ---------------------- Checks Completed
    
    def getDict(self,df1, df2, df3):
        """ Merge and Return Data"""

        # This function is responsible to generate a JSON Representation [Dictionary]
        # of all the given airports [Cleaned] with their currency and EURO conversion
        # details

        # Merging Airports and Country Data on Country Name
        df4 = pd.merge(df1, df3, left_on='Country', right_on='name')

        # Merging the new Airports Country Data with Currency data to get the final JSON
        self.__merged = pd.merge(df4, df2, left_on="currency_alphabetic_code", right_on="Code")

        self.__merged.set_index('IATA', inplace=True)

        return self.__merged.to_dict(orient='index')
   
    def to_csv(self,finalOp):
        flag = False
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filePath = dir_path+"\output.csv"
        self.displayStatusFormatMessage("\tSaving file at: {}\n".format(filePath))

        try:
            with open("output.csv", "w", newline='') as f:
                writer = csv.writer(f)
                try:
                    flag=True
                    writer.writerows(finalOp)
                except StopAsyncIteration as identifier:
                    flag=False
                    self.displayErrFormatMessage("Iteration stoped. File cannot be created")
        except PermissionError as err:
            self.displayErrFormatMessage("{} is open. Please close the file and try again later".format(filePath))
        if flag:
            self.displaySuccessFormatMessage("\tOutput File Created")
            
    def displayStatusFormatMessage(self, message, params=""):
        message += str(params)
        print(colored(str("STATUS::"+message), 'blue'))
        print()

    def displayErrFormatMessage(self,message, params=""):
        message += str(params)
        print(colored(str("ERROR::"+message), 'red'))
        print()
    
    def displayWarningFormatMessage(self,message,params=""):
        message += str(params)
        print(colored(str("WARNING::"+message), 'yellow'))
        print()

    def displaySuccessFormatMessage(self, message, params=""):
        message += str(params)
        print(colored(str("SUCCESS::"+message), 'green'))
        print()
        
    def displayManFormatMessage(self,message,color="magenta"):
        print(colored(message, color))
        print()


