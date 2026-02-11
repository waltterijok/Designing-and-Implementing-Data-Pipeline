

# class Test:
#     def __init__(self):
#         self.__x = 10

# t = Test()
# print(t.x)

class Test:
    def __init__(self):
        self.__x = 10       # Python changes this to format _Test__x
        self._x = 20

t = Test()

print(t._Test__x)