class ChainHandler():
    def __init__(self,msgType,successor=None) -> None:
        self.successor = successor
        self.msgType = msgType
    def sendToSuccessor(self,msg):
        if self.successor:
            self.successor.handle(msg)
    def handle(self,msg):
        if msg.type == self.msgType:
            self.onHandle(msg)
        else:
            self.sendToSuccessor(msg)
    def onHandle(self,msg):
        raise NotImplementedError

class msg():
    def __init__(self,msgType) -> None:
        self.type = msgType

class myHandler(ChainHandler):
    def onHandle(self,msg):
        print(msg.type,"deal in handler",self.msgType)


if __name__ == "__main__":
    # h1->h2
    msg1 = msg("type1")
    msg2 = msg("type2")

    h2 = myHandler("type2")
    h1 = myHandler("type1",successor=h2)

    h1.handle(msg1)
    h1.handle(msg2)