# 关系结构为星形,消息发送者和接收者解耦
class Mediator():
    def __init__(self) -> None:
        self.player = Player(self)
        self.npcList = [Npc(self),Npc(self),Npc(self)]

    def invoke(self,event):
        if event == "PlayerSpeak":
            for npc in self.npcList:
                npc.Listen()
        elif event == "NpcSpeak":
             self.player.Listen()
        # add event type
        else:
            return

class Actor():
    def __init__(self,mediator) -> None:
        self.mediator = mediator

class Player(Actor):
    def speak(self):
        print("player speak")
        self.mediator.invoke("PlayerSpeak")
    def Listen(self):
        print("player listening")
    
class Npc(Actor):
    def speak(self):
        print("npc speak")
        self.mediator.invoke("NpcSpeak")
    def Listen(self):
        print("npc listening")

if __name__ == "__main__":
    mediator = Mediator()
    mediator.player.speak()
    mediator.npcList[0].speak()
    