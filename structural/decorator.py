# 保持被装饰的函数调用方式不变
class MyText:
    def __init__(self,str) -> None:
        self.value = str
    def __str__(self) -> str:
        return self.value

class BookDecorator():
    def __init__(self,tar) -> None:
        self.tar = tar
    def __str__(self):
        return "<<"+self.tar.value+">>"

class BlankDecorator():    
    def __init__(self,tar) -> None:
        self.tar = tar
    def __str__(self):
        return " ".join(self.tar.value)

if __name__ == "__main__":
    t = MyText("test")
    bookt = BookDecorator(t)
    blankt = BlankDecorator(t)
    print(t,bookt,blankt)