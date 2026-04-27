class Counter:
    __count: int = 0
    def increase(self):
        self.__count += 1
        return None
    
    def read(self):
        return self.__count
    
    def reset(self):
        self.__count == 0
        return self.__count
    
Counter1 = Counter()                # initializes the 'counter' object
print("count:", Counter1.read())
Counter1.increase()
print("count:", Counter1.read())
Counter1.increase()
print("count:", Counter1.read())
Counter1.__count = 4                # illegal operation (KYSY MIRALTA)
print("count:", Counter1.read())
Counter1._Counter__count = 9        # legal operation, see above brackets
print("count:", Counter1.read())
Counter1._Counter__count = 7
print("count:", Counter1.read())
Counter1.reset()
print("count:", Counter1.read())

