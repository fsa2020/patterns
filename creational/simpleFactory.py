# 简单工厂
class SimpleFactory():
    def __init__(self) -> None:
        self.numDict = {
            "chinese" : {1:"一",2:"二",3:"三"},
            "english" : {1:"one",2:"two",3:"three"},
        }
    def getNumToStrDict(self,type):
        return self.numDict[type]
class MyNum():
    def __init__(self,value=1,type="chinese") -> None:
        self.type = type
        self.value = value
        self.factory = SimpleFactory()
    def __str__(self) -> str:
        # print(self.factory.getNumToStrDict(self.type))
        return self.factory.getNumToStrDict(self.type)[self.value]
 
if __name__ == "__main__":
    print(MyNum(),MyNum(2),MyNum(3,"english"))