# 区别于装饰器,在于对修改的函数的使用方法可能会改变
class Adapter:
    def __init__(self,target,**methods) -> None:
        self.target = target
        self.methods = methods
    def __getattr__(self, name: str):
        if name not in self.methods:
            return getattr(self.target,name)
        else:
            return self.methods[name]

class Monster:
    def growl(self):
        print("oohhhh")

class Npc:
    def speakTo(self,target):
        print("hello",target)

if __name__ == "__main__":
    m = Monster()
    npc = Npc()
    npc.speakTo("mike")
    crazyNpc = Adapter(npc,speakTo=m.growl)
    crazyNpc.speakTo()
