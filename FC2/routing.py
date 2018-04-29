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

        # Unvisited List holds all the airports. Since none of them are visited yet
        self.__unvisited= input[0][:]

        # ========================================================================================================================
        # This gives the aircraft information to get the Aircraft Range
        aircraft = input[1]
        if aircraft == None:
            self.__utils.displayWarningFormatMessage("\tNo Aircraft provided. No refeuling charges will be calculated")
            self.__acRange = None
        else:
            self.__acRange = aircrafts.get(aircraft)['range']  # Range of the aircraft
        # ========================================================================================================================

        # ========================================================================================================================
        # -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ ROUTING ALGORITHM BEGINHS /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

        src = self.__unvisited[0] # ------------------------ First Source ***************** The STARTING POINT
        iten = graph[0] # ---------------------------------- Get the Starting airport's adjacency matrix
        j=0 # ---------------------------------------------- Iterator for the graph

        while j< len(graph): 
            self.__airportCost = []  # --------------------- Cost [Distance]
            self.__airports = [] # ------------------------- Holds the intenerary of the minimum cost
            indexVi = -1 # --------------------------------- Index of the visited airports
            
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: MINIMUM DISTANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # Getting the minimum distance from the source to next airport out of all the aiports 
            i = 0 # ---------------------------------------- Iterator
            while i< len(iten): # -------------------------- Iterate to get the list of all the distances from the source
                distance = iten[i][1]
                dest = self.__unvisited[i]
                if not (distance == 0):
                    self.__airportCost.append(distance) # -- Distances that are not zero 
                    self.__airports.append([src,dest]) # --- Airports in each distances
                i+=1
            minimumCost = min(self.__airportCost) # -------- Get the Minimum Cost
            self.__minDist.append(minimumCost) # ----------- List with minimum cost [Used as final route]
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: MINIMUM DISTANCE [OVER] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: REMOVE PREVIOUS SOURCE FROM GRAPH <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # Setting the destination calculated above as the new source
            indexMin = self.__airportCost.index(minimumCost) # ----- Index of the minimum distance selected so that we can get the next airport as the source
            airports = self.__airports[indexMin] # ----------------- getting the next source airport here
            indexVisited = self.__unvisited.index(airports[0]) # --- From unvisited we need the index of the last visited airport
            # ------ <POP: visited sources values from the graph>
            for k in range(len(graph)):
                graph[k].pop(indexVisited)
            # ------ </POP>

            if self.__visited == []:
                sourceAirport = airports[0]
                sourceAirportCost = self.__airportCost
             
            self.__visited.append(self.__unvisited.pop(indexVisited)) # pop the visited airport from unvisited to visited list
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: REMOVE PREVIOUS SOURCE FROM GRAPH [OVER] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: NEW SOURCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            presrc = airports[0] # -------------- PREVIOUS SOURCE
            src = airports[1] # ----------------- NEW SOURCE
            indexVi = input[0].index(src)
            iten = graph[indexVi]  # ------------ Graph List for the new source
            self.__utils.displayManFormatMessage(
                "\n\t\t\t\t{} -> {} Distance: {:.2f}km".format(presrc, src, minimumCost),color="cyan")
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: NEW SOURCE [OVER] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: FINAL LEG <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if len(self.__unvisited) == 1:
                self.__visited.append(self.__unvisited[-1])
                self.__utils.displayManFormatMessage("\n\t\t\t\t{} -> {}. Cost: {:.2f}km".format(airports[1], sourceAirport, sourceAirportCost[indexVi-1]),color="cyan")
                break
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CALCULATION: FINAL LEG [OVER] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # ========================================================================================================================
            j+=1
        return self.__visited,self.__minDist,self.__acRange,aircraft

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
