# 组合：对象集合和单个对象需要具备同样的属性和方法
class Component:
    def __init__(self,name) -> None:
        self.nodes = []
        self.name = name

class Composite(Component):
    def add(self,c:Component):
        self.nodes.append(c)
    
    def remove(self,c:Component):
        self.nodes.remove(c)
        
    def makeNoise(self):
        print("---- "+self.name+" start ----")
        for node in self.nodes:
            node.makeNoise()    
        print("---- "+self.name+"  end  ----")

class Leaf(Component):
    def makeNoise(self):
        print(self.name,": ohhh")


if __name__ == "__main__":
    m1 = Leaf("m1")
    m2 = Leaf("m2")
    m3 = Leaf("m3")
    set1 = Composite("set1")
    set1.add(m1)
    set1.add(m2)
    set2 = Composite("set2")
    set2.add(set1)
    set2.add(m3)
    set2.makeNoise()