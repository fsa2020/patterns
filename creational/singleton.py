# type 1
# 状态一直，非对象一致
# 通过重新绑定self.__dict__ 实现每个子类绑定同样的state
class BorgSingleton():
    __state = {}
    def __init__(self) -> None:
        self.__dict__ = self.__state

class MyBorgSingleton(BorgSingleton):
    def __init__(self) -> None:
        super().__init__()
        self.count = 0
    def __str__(self) -> str:
        return "BorgSingleton"+str(self.count)
    def addOne(self):
        self.count+=1

# type 2
# 重写new
# 先调用 __new__ 传递实例给 __init__ 
class Singleton():
    __instance = None
    def __new__(cls):
        if cls.__instance ==None:
            cls.__instance = super().__new__(cls)
        return cls.__instance  # return instance is self in __init__(self)
    def __init__(self) -> None:
        self.count = 0 
    def __str__(self) -> str:
        return "BorgSingleton"+str(self.count)
    def addOne(self):
        self.count+=1

if __name__ == "__main__":
    # type 1
    # b1 = MyBorgSingleton()
    # b2 = MyBorgSingleton()
    # type 2
    b1 = Singleton()
    b2 = Singleton()

    print(b1,b2)
    b1.addOne()
    print(b1,b2)
    b2.addOne()
    print(b1,b2)
    print(id(b1),id(b2))
    print(id(b1.__dict__),id(b2.__dict__))
    print(id(b1.count),id(b2.count))
    print(b1.__dict__)
    # commit and push test


