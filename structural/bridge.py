# 组合>继承 使用 xx has a xx 
class Element:
    def __init__(self,char) -> None:
        self.char = char

class NormalLen(Element):
    def getChar(self):
        return self.char

class DoubleLen(Element):
    def getChar(self):
        return self.char*2

class Draw:
    def __init__(self,size,element:Element) -> None:
        self.element = element
        self.size = size

class DrawSquare(Draw):
    def draw(self):
        for _ in range(self.size):
            print(self.element.getChar()*self.size)

class DrawTrangle(Draw):
    def draw(self):
        for i in range(self.size):
            print(self.element.getChar()*(self.size-i))

if __name__ == "__main__":
    element1 = NormalLen("*")
    element2 = DoubleLen("*")
    element3 = NormalLen("#")
    element4 = DoubleLen("#")

    draw1 = DrawSquare(3,element1)
    draw2 = DrawSquare(3,element2)
    draw3 = DrawTrangle(3,element3)
    draw4 = DrawTrangle(3,element4)

    draw1.draw()
    draw2.draw()
    draw3.draw()
    draw4.draw()