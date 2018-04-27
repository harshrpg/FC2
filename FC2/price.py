import utils
class Price:
    """This class will calculate the
    price of each itenerary taking into
    account of the aircraft provided."""

    def __init__(self):
        self.__utils = utils.Utility()  # Utility Object for formatted Prints

    def getPrice(self,distance,currency):
        """This method gives the price based on the distane aircraft and currency"""
        return distance*currency
        
            
        

