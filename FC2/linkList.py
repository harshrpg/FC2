from FC2 import utils
class LinkList:
    """This is representation of a linked List"""

    def __init__(self):
        self.__linkList = [] # A list to hold a node of a linked List
        # A node represented as a list
        # A node will have two values [pointer,value]
        # Pointer will point to the next node in the list
        # If pointer is 0 it is the head of the linked list
        self.__utils = utils.Utility() # Utility Object to display printed Messages
    
    def addNode(self,node):
        self.__linkList.append(node)
    
    def getNode(self,index):
        try:
            return self.__linkList[index]
        except IndexError as err:
            self.__utils.displayErrFormatMessage("Index: {}, could not be found in the list. Check the size of the list".format(index))
    
    def getHead(self):
        try:
            return self.__linkList[0]
        except IndexError as err:
            self.__utils.displayErrFormatMessage("Head, could not be found in the list. List is empty")
    
    def getList(self):
        return self.__linkList
        
    
    def removeNode(self,node):
        try:
            self.__linkList.remove(node)
        except ValueError as err:
            self.__utils.displayErrFormatMessage("Cannot find the element: {} requested to remove".format(node))
        except TypeError as err:
            self.__utils.displayErrFormatMessage("Provide a node to remove")
    
    def getSize(self):
        return len(self.__linkList)
        
