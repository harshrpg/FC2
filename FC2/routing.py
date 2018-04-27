from FC2 import utils
from FC2 import price
import unicodedata
class Routes:

    """ Class to calculate the Shortest path using Dijkstra Algo"""

    def __init__(self):
        self.__airports = [] # List of all the airports provided in the input
        self.__airportCost = [] # This is a list of linkedLists thay will hold each airports cost to another airports
        # Airport Cost is actually a representation of a directed graph.
        # If on index 0 in airports we have 'Dublin'
        # Then on index 0 of airports cose we will have the edge values from 'Dublin' to other airports
        # Similarly for all other airports
        self.__previousVertex = [] # The previous vertex of the airport in the airports list
        # This list will hold the previous vertex of all the airports
        # This list will be our final least route
        self.__visited = [] # An array of all visited airports
        self.__unvisited = [] # An array of all unvisited airports
        self.__utils = utils.Utility()
        self.__acRange = -1
        self.__price = price.Price()
        self.__flag=False
        self.__minDist=[]

    def getRoute(self, graph, input, aircrafts,data):
        
        """ This method takes 4 arguments: graph = Adjaceny matrix of the airports, 
        input = list of the airports, aircrafts = aircrafts data, data=filteredData.
        This method uses the understanding of Dijkstra's algorithm to get
        the shortest possible route within the graph taking
        index 0 of the input as the source. It also takes aircrafts into account in order to calculate
        for refueling"""
        self.__airports = []  # List of all the airports provided in the input
        # This is a list of linkedLists thay will hold each airports cost to another airports
        self.__airportCost = []
        # Airport Cost is actually a representation of a directed graph.
        # If on index 0 in airports we have 'Dublin'
        # Then on index 0 of airports cose we will have the edge values from 'Dublin' to other airports
        # Similarly for all other airports
        self.__previousVertex = []  # The previous vertex of the airport in the airports list
        # This list will hold the previous vertex of all the airports
        # This list will be our final least route
        self.__visited = []  # An array of all visited airports
        self.__unvisited = []  # An array of all unvisited airports
        self.__utils = utils.Utility()
        self.__acRange = -1
        self.__price = price.Price()
        self.__flag = False
        self.__minDist = []
        self.__unvisited= input[0][:]
        aircraft = input[1]
        if aircraft == None:
            self.__utils.displayWarningFormatMessage("No Aircraft provided. No refeuling charges will be calculated")
        else:
            self.__acRange = aircrafts.get(aircraft)['range']  # Range of the aircraft
        # print("Range of Aircrafts: ",self.__acRange)

        acCount=0
        src = self.__unvisited[0]
        sourceCurr = data.get(src)['toEUR']
        iten = graph[0]
        j=0
        toEur = data.get(src)['toEUR']
        while j< len(graph):
            # print("SOURCE AIRPORT: ", src)
            self.__airportCost=[]
            self.__airports = []
            indexVi = -1
            # print(iten)
            i = 0
            while i< len(iten):
                distance = iten[i][1]
                dest = self.__unvisited[i]
                flag=True
                if not (distance == 0):
                    legCost = self.__price.getPrice(distance,1)
                    self.__airportCost.append(legCost)
                    self.__airports.append([src,dest])
                    # print("\tFrom {} -> {}: \u20ac {}".format(src, dest, legCost))
                i+=1
             # Minimum Cost Calculation below
            minimumCost = min(self.__airportCost)
            self.__minDist.append(minimumCost)
            # print('Airport Cost:==================================== ',self.__airportCost)
            # Index of the minimum distance selected so that we can get the next airport as the source
            indexMin = self.__airportCost.index(minimumCost)
            # getting the next source airport here
            airports = self.__airports[indexMin]
            # print("======================airports: ",airports[0])
            # From unvisited we need the index of the last visited airport
            indexVisited = self.__unvisited.index(airports[0])
            # POP out all the visited sources values from the graph
            for k in range(len(graph)):
                graph[k].pop(indexVisited)
            if self.__visited == []:
                sourceAirport = airports[0]
                sourceAirportCost = self.__airportCost
            # pop the visited airport from unvisited to visited list 
            self.__visited.append(self.__unvisited.pop(indexVisited))
            # New source
            presrc = airports[0]
            src = airports[1]   
            indexVi = input[0].index(src)
            # print("Index Visited:::::", indexVi)
            iten = graph[indexVi]
            # self.__utils.displaySuccessFormatMessage(
            #     "\n\t{} -> {} Cost: \u20ac{:.2f}".format(presrc, src, minimumCost))
            # print("-------------------------------------------\n")
            # print("UNVISITED: ",self.__unvisited)
            if len(self.__unvisited) == 1:
                self.__visited.append(self.__unvisited[-1])
                # print("Final Leg")
                # self.__utils.displaySuccessFormatMessage("\n\t{} -> {}. Cost: \u20ac{:.2f}".format(airports[0], sourceAirport, sourceAirportCost[indexVi-1]))
                # print("VISITED: ", self.__visited)
                break
            # print("VISITED: ", self.__visited)
            j+=1
        return self.__visited,self.__minDist,self.__acRange

    def isPossible(self,aircraftRange,routeDistances):
        count=0
        flag=False
        for i in routeDistances:
            if aircraftRange>=i:
                count+=1
        if count==len(routeDistances):
            flag=True
        return flag

    def getFinalAcRoute(self,acRange,routeList,routeDistance):
        sumDistance=0
        count=0
        revRouteDist = list(reversed(routeDistance))
        revRoute = list(reversed(routeList))
        finRoute=[]
        finDist = []
        finalR = []
        flag=True
        flagSum = False
        sumList=[]
        for i,r in enumerate(revRouteDist):
            # print(i)
            # print("SUM: ",sumDistance)
            if not flagSum:
                sumDistance+=r
            else:
                # print("In else")
                sumDistance=0
                sumDistance+=r
            sumList.append(sumDistance)
            # print(sumList)
            if acRange > sumDistance:
                count +=1
            elif count == 0:
                flag = False
            else:
                # print("In else")
                flagSum = True
                finRoute.append(revRoute[count])
                finDist.append(sumList[i-1])
                count += 1
        
        # print(count)
        if flag:
            if count == len(revRouteDist) and flagSum == True:
                finRoute.append(revRoute[count])
                finDist.append(revRouteDist[-1])
            elif count == len(revRouteDist):
                finRoute.append(revRoute[count])
                finDist.append(sumList[count-1])
            
            finalR = routeList + finRoute
            finalD = routeDistance + finDist
            return finalR, finalD
        else:
            return None,None
