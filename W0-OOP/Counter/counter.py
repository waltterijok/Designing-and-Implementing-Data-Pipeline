class Counter:

    # sets the initial value at 0 / asettaa aloitus arvoksi 0
    def __init__(self):
        self.__count = 0
    
    # adds +1 to the current value / lisää sen hetkiseen arvoon +1
    def addCount(self):
        self.__count = self.__count + 1
        
    # returns the current value / palauttaa sen hetkisen arvon    
    def getCount(self): 
        return self.__count

    # resets the value or count / nollaa arvon
    def zeroCount(self):
        self.__count = 0