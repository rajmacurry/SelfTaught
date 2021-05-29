class Square:
    square_list = []
    def __init__(self,l):
        self.length=l
        self.square_list.append(self.length)
        print(self.square_list)

squa_1 = Square(5)
squa_2 = Square(10)
