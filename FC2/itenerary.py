from math import pi, sin, cos, acos
from FC2 import utils
from FC2 import linkList
class Itenerary:
    """This class creates the required list of
    dictionaries that will hold all the required
    values like Latitude, Longitude and the Euro conversion
    price for the airport"""

    def __init__(self):
        
        self.__airports = {} # -------- Dictionary of airports provided
        self.__allAirports = [] # ----- List of Dictionaries of all the airports from the DB
        self.__itenerary = [] # ------- List of all airports with their calculated distance and from Euro value
        
        self.__utils = utils.Utility() # Utility Object for formatted Prints

        self.__radiusEarth = 6371 # radius of earth in km
    
    def getIteneraryData(self,itList,allData):
        """This method will return a dictionary
        that will contain only the important fields
        like Lat, Lng, Eur value etc"""
        
        for key in itList[0]: # ------ Tuple's 0 position has airports and 1 position has aircraft
            self.__airports[key] = allData.get(key) # ----- Dictionary with required fields
        return self.__airports

    def getDistance(self,latitude1,latitude2,longitude1,longitude2):
        theta1 = longitude1 * (2*pi)/360  # Radians
        theta2 = longitude2 * (2*pi)/360  # Radians
        phi1 = (90-latitude1)*(2*pi)/360  # Radians
        phi2 = (90-latitude2)*(2*pi)/360  # Radians
        return acos(sin(phi1)*sin(phi2)*cos(theta1-theta2) + cos(phi1)*cos(phi2))*self.__radiusEarth


    def getAdjacencyGraph(self,locations):
        """This method will return an adjacency
        list of the airports graph in interest"""

        length = len(locations)
        if length<2 or length>5:
            self.__utils.displayErrFormatMessage('Locations are not with required range')
            return None
        else:
            self.__utils.displayStatusFormatMessage('Creating the Graph and the Adjacency List')
            __adjacencyList = [[]*x for x in range(len(locations))]  # --- Adjaceny List that will hold adjacent vertex of the node of interest in graph
            for j,src in enumerate(locations):
                self.__linkList = linkList.LinkList()
                for i,dest in enumerate(locations):
                    __linkList = []  # --- A linked list that will hold the distance of the node with source node in the adjacency list
                    if i==j:
                        __linkList.append(i) # --- Link list pointer to previous node. If 0 then thats the head
                        __linkList.append(0) # --- Value in the node
                        self.__linkList.addNode(__linkList)
                    else:
                        # theta1 = src[1] * (2*pi)/360  # Radians
                        # theta2 = dest[1] * (2*pi)/360  # Radians
                        # phi1 = (90-src[0])*(2*pi)/360  # Radians
                        # phi2 = (90-dest[0])*(2*pi)/360  # Radians
                        distance = self.getDistance(src[0],dest[0],src[1],dest[1])
                        __linkList.append(i)
                        __linkList.append(distance)
                        self.__linkList.addNode(__linkList)
                __adjacencyList[j] = self.__linkList.getList()
            return __adjacencyList 

