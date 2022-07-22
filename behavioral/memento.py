from copy import deepcopy

class Memento:
    def write(self,target):
        self.record = deepcopy(target.__dict__)

    def restore(self,target):
        target.__dict__ = deepcopy(self.record)

class Player:
    def __init__(self,name) -> None:
        self.name = name
    def __str__(self) -> str:
        return self.name
    def changeName(self,name):
        self.name = name
    
if __name__ == "__main__":
    p = Player("player1")
    m = Memento()
    m.write(p)
    print(p)

    p.changeName("xxx")
    print(p)

    m.restore(p)
    print(p)

    p.changeName("xxx2")
    print(p)

    m.restore(p)
    print(p)