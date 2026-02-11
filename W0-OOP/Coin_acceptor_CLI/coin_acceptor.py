class CoinAcceptor:

    def __init__(self):
        self.__amount = 0.0            # sets the initial total amount of coins in the collector
        self.__coin_count = 0          # sets the initial total value of coins in the collector

    def insertCoin(self, coin_value):       # inserts a coin with specific value
        self.__amount += coin_value         # adds the inputted value to the total amount
        self.__coin_count += 1

    def getAmount(self):
        return self.__amount
    
    def getCoinCount(self):
        return self.__coin_count

    def returnCoins(self):
        coins_returned = self.__coin_count
        amount_returned = self.__amount
        self.__amount = 0.0
        self.__coin_count = 0
        return coins_returned, amount_returned
