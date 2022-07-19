# 抽象工厂 使用NotImplementedError构建抽象方法
class AbstractNum():
    def __init__(self,value=1) -> None:
        self.value = value
    def __str__(self) -> str:
        raise NotImplementedError

class MyNumEnglish(AbstractNum):
    __numToStr = {1:"one",2:"two",3:"three"}
    def __str__(self) -> str:
        return self.__numToStr[self.value]

class MyNumChinese(AbstractNum):
    __numToStr = {1:"一",2:"二",3:"三"}
    def __str__(self) -> str:
        return self.__numToStr[self.value]

if __name__ == "__main__":
    print(MyNumChinese(),MyNumChinese(2),MyNumEnglish(3))