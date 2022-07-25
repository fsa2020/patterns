class Resources:
    def __init__(self) -> None:
        self.resources = []
    def addResItem(self,item):
        self.resources.append(item)
    def accept(self,visitor):
        for item in self.resources:
            item.accept(visitor)
    def __str__(self) -> str:
        return ";".join([type(r).__name__ + str(r.num) for r in self.resources])

class Item:
    def __init__(self,num) -> None:
        self.num = num
    def accept(self,visitor):
        visitor.visit(self)

class Coin(Item):
    def __init__(self,num) -> None:
        self.num = num

class Food(Item):
    def __init__(self,num) -> None:
        self.num = num

class Visitor:
    def __init__(self,itemTypeList=[]) -> None:
        self.itemTypeList = itemTypeList

    def visit(self,item):
        if type(item) not in self.itemTypeList: 
            return
        else:
            visitFunc = getattr(self,"visit"+type(item).__name__)
            visitFunc(item)

class Player(Visitor):
    def visitCoin(self,coin):
        print("Player visit:"+type(coin).__name__)
        coin.num -=5
    def visitFood(self,food):
        print("Player visit:"+type(food).__name__)
        food.num -= 5

class Monster(Visitor):
    def visitFood(self,food):
        print("Monster visit:"+type(food).__name__)
        food.num -= 10

if __name__ == "__main__":
    coins = Coin(100)
    foods = Food(100)

    p = Player([type(coins),type(foods)])
    m = Monster([type(foods)])
    
    res = Resources()

    res.addResItem(coins)
    res.addResItem(foods)
    print(res)

    res.accept(p)
    print(res)

    res.accept(m)
    print(res)
