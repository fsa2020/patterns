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
    def speak(self):
        print("hello")

if __name__ == "__main__":
    m = Monster()
    npc = Npc()
    npc.speak()
    crazyNpc = Adapter(npc,speak=m.growl)
    crazyNpc.speak()
