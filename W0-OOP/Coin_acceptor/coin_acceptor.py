class CoinAcceptor:

    def __init__(self):
        self.__amount = 0

    def insertCoin(self):
        self.__amount = self.__amount + 1

    def getAmount(self):
        return self.__amount

    def returnCoins(self):
        coins_returned = self.__amount
        self.__amount = 0
        return coins_returned
