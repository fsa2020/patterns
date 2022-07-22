# type 1
# create a new Iterator
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
    def __init__(self,content) -> None:
        self.content = content
    def createIterator():
        raise NotImplementedError

class NpcAggregate(Aggregate):
    def createIterator(self):
        return NpcIterator(self.content)

# type 2
# using python iterator protocol

class IterableNpcs():
    def __init__(self,num) -> None:
        self.npcs = []
        self.p = -1
        for i in range(num):
            self.npcs.append("npc"+str(i))
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.p < len(self.npcs)-1:
            self.p += 1
            return self.npcs[self.p]
        else:
            raise StopIteration

if __name__ == "__main__":
    
    npcs = ("mike","jordan","han")
    iter = NpcAggregate(npcs).createIterator()
    while iter.hasNext():
        print(iter.next())

    for npc in IterableNpcs(5):
        print(npc)

