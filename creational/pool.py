# 对象池可以避免频繁划分内存创建对象
import queue
import protoType as pt

class Pool():
    def __init__(self,temple) -> None:
        self.typePools = queue.Queue()
        self.creator = temple
        # add Proto instance as temple
    def createItem(self):
        return self.creator.clone()

    # create one instance each time queue empty
    def addItem(self,num=5):
        print("add item")
        for _ in range(num):
            self.typePools.put(self.createItem())

    def get(self):
        if self.typePools and self.typePools.qsize()<=0:
            self.addItem()
        return self.typePools.get()

    def put(self,item):
        self.typePools.put(item)

    def destory(self):
        self.typePools = None
        self.creator = None


if __name__ == "__main__":
    monsterPool = Pool(pt.Monster(hp=10,mp=10))
    for i in range(10):
        m = monsterPool.get()
        m.printAttrDict()
        monsterPool.put(m)