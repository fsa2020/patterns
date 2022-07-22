# 使用clone方法创建新对象
# use clone function to get instances 
class ProtoType():
    def __init__(self,**attrs) -> None:
        self.__dict__.update(attrs)
    def clone(self,**attrs):
        # same to deep copy
        copy = self.__class__(**self.__dict__)
        copy.__dict__.update(attrs)
        return copy

class Monster(ProtoType):
    def __init__(self, name="monseter",**attrs) -> None:
        self.__dict__.update(attrs)
        self.name = name
    def printAttrDict(self):
        print(self.__dict__)

class Npc(ProtoType):
    def __init__(self, name="Npc",**attrs) -> None:
        self.__dict__.update(attrs)
        self.name = name
    def printAttrDict(self):
        print(self.__dict__)

if __name__ == "__main__":
    npc1 = Npc(hp=10,mp=5)
    npc2 = npc1.clone(name = "npc2",hp=100,mp=50)
    npc3 = npc1.clone(hp=10,mp=20)

    npc1.printAttrDict()
    npc2.printAttrDict()
    npc3.printAttrDict()

    