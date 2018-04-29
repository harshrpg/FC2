from FC2 import utils
class Price:
    """This class will calculate the
    price of each itenerary taking into
    account of the aircraft provided."""

    def __init__(self):
        self.__utils = utils.Utility()  # Utility Object for formatted Prints

    def getPrice(self,route,distance,input,acRange):
        """This method gives the price based on the distane aircraft and currency"""

        # If aircraft Range > than the entire distance then refuel only for the distance to be travelled
        totalDistance = sum(distance)
        sum_distances = 0
        totalPrice = -1
        sumPrice = 0
        toEUR = input.get(route[0])['toEUR']
        if acRange>totalDistance:
            totalPrice = totalDistance*toEUR
            sumPrice+=totalPrice
        else:
            i = 0
            fuelConsumed = 0
            while i < len(distance):
                sum_distances+=distance[i]
                if not acRange >= sum_distances:
                    if i == (len(distance)-1):
                        remainingDistance = fuelConsumed-distance[i]
                        toEUR = input.get(route[i])['toEUR']
                        totalPrice = (acRange-fuelConsumed)*toEUR
                        sumPrice += totalPrice
                    else:
                        toEUR = input.get(route[i])['toEUR']
                        totalPrice = (acRange-fuelConsumed)*toEUR
                        sumPrice += totalPrice
                        sum_distances = 0 + distance[i]
                        fuelConsumed = acRange - sum_distances
                else:
                    fuelConsumed = acRange - sum_distances
                i+=1
        return route,sumPrice
            
        

