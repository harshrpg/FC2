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


    def getRoute(self, graph, input, aircrafts,data):
        
        """ This method takes 4 arguments: graph = Adjaceny materix of the airports, 
        input = list of the airports, aircrafts = aircrafts data, data=filteredData.
        This method uses Dijkstra's algorithm to get
        the shortest possible route within the graph taking
        index 0 of the input as the source. It also takes aircrafts into account in order to calculate
        for refueling"""
        self.__unvisited= input[0][:]
        aircraft = input[1]
        if aircraft == None:
            self.__utils.displayWarningFormatMessage("No Aircraft provided. No refeuling charges will be calculated")
        else:
            self.__acRange = aircrafts.get(aircraft)['range']  # Range of the aircraft
        acCount=0
        src = self.__unvisited[0]
        iten = graph[0]
        j=0
        while j< len(graph):
            self.__airportCost=[]
            self.__airports = []
            indexVi = -1
            # print(iten)
            i = 0
            while i< len(iten):
                distance = iten[i][1]
                dest = self.__unvisited[i]
                # print(dest)
                # print(distance)
                # print("Source: {}, Destination: {}, Distance: {}".format(src,dest,distance))
                # print("Visited: {}".format(self.__visited))
                if not (distance == 0):
                    toEur = data.get(src)['toEUR']
                    legCost = self.__price.getPrice(distance, 1)
                    self.__airportCost.append(legCost)
                    self.__airports.append([src,dest])
                    print("\tFrom {} -> {}: \u20ac {}".format(src, dest, legCost))
                # if src==dest:
                #     print("TRUE")
                #     print(self.__unvisited)
                i+=1
            minimumCost = min(self.__airportCost)
            indexMin = self.__airportCost.index(minimumCost)
            airports = self.__airports[indexMin]
            indexVisited = self.__unvisited.index(airports[0])
            for k in range(len(graph)):
                graph[k].pop(indexVisited)
            if self.__visited == []:
                sourceAirport = airports[0]
                sourceAirportCost = self.__airportCost
            self.__visited.append(self.__unvisited.pop(indexVisited))
            # print(self.__unvisited)
            src = airports[1]   
            indexVi = input[0].index(src)
            # print("Index Visited:::::", indexVi)
            iten = graph[indexVi]
            self.__utils.displaySuccessFormatMessage("\n\t{} -> {}. Cost: \u20ac{:.2f}".format(airports[0], airports[1], minimumCost))
            print("-------------------------------------------\n")
            if len(self.__unvisited) == 1:
                # print("Final Leg")
                self.__utils.displaySuccessFormatMessage(
                    "\n\t{} -> {}. Cost: \u20ac{:.2f}".format(airports[0], sourceAirport, sourceAirportCost[indexVi-1]))
                break
            j+=1

