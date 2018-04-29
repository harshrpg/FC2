from FC2 import utils
class Price:
    """This class will calculate the
    price of each itenerary taking into
    account of the aircraft provided."""

    def __init__(self):
        self.__utils = utils.Utility()  # Utility Object for formatted Prints

    def getPrice(self,route,distance,input,acRange):
        """This method gives the price based on the distane aircraft and currency"""

        totalDistance = sum(distance)
        sumCost = 0
        toEUR = input.get(route[0])['toEUR']
        # If the range of the aircraft is more than the entire journey. then fill in only journey distance fuel
        if acRange>totalDistance:
            totalCost = totalDistance*toEUR
            sumCost+=totalCost
        else:
            i = 0
            totalCost = 0
            fuelRemaining = acRange
            sumCost = acRange*toEUR
            while i < len(distance):
                # Get the currency value in Euros for the city
                toEUR = input.get(route[i])['toEUR']
                # No refuel until the fuel remaining is less than the distance for next leg
                if (fuelRemaining - distance[i]) >=0:
                    fuelRemaining -= distance[i]
                else:
                    # If refueling is needed on the last leg. Dont fill to max just fill what is needed
                    if i == (len(distance)-1):
                        remainingDistance = fuelRemaining-distance[i]  
                        totalCost = remainingDistance*toEUR
                    # Refuel from whatever fuel is remaining to the max capacity and calculate the price in euros
                    else:
                        totalCost = (acRange-fuelRemaining)*toEUR
                        fuelRemaining = acRange
                sumCost+=totalCost
                i+=1
        return route,sumCost
            
        

