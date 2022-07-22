class Iterator():
    def __init__(self,elements) -> None:
        self.elements = elements
        self.p = -1
    def next(self):
        raise NotImplementedError
    def hasNext(self):
        raise NotImplementedError

class NpcIterator(Iterator):
    def next(self):
        if self.hasNext():
            self.p += 1
            return self.elements[self.p]         

    def hasNext(self):
        return self.p<len(self.elements)-1

class Aggregate():
    def __init__(self,list) -> None:
        self.list = list
    def createIterator():
        raise NotImplementedError

class NpcAggregate(Aggregate):
    def createIterator(self):
        return NpcIterator(self.list)

if __name__ == "__main__":
    npcs = ["mike","jordan","han"]
    iter = NpcAggregate(npcs).createIterator()
    while iter.hasNext():
        print(iter.next())