#classes
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def area(self):
        return self.width() * self.height()

    def circumference(self):
        return 2 * self.width() + 2 * self.height()
    
    def __str__(self):
        return "(%s,%s),(%s,%s)" % (self.x1, self.y1,self.x2, self.y2)

#inheritance
class Square(Rectangle):
    def __init__(self, x1, y1, size):
        super().__init__(x1, y1, x1 + size, y1 + size)
