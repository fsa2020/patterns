class Command():
    def execute(self):
        return NotImplementedError
    def undo(self):
        return NotImplementedError

class DrawPointCommand(Command):
    def __init__(self,client,name,i,j) -> None:
        self.name = name+str(i)+str(j)
        self.client = client
        self.pos = [i,j]
    def execute(self):
        self.client.drawPoint(self.pos[0],self.pos[1])
    def undo(self):
        self.client.clearPoint(self.pos[0],self.pos[1])

class Invoker():
    def __init__(self) -> None:
        self.commands = {}
        self.commandQueue = []

    def addCommand(self,command):
        self.commands[command.name] = command

    def do(self,cName):
        if cName not in self.commands:
            print("no cmd :",cName)
            return 

        self.commands[cName].execute()
        self.commandQueue.append(cName)

    def undo(self):
        if len(self.commandQueue)<=0:return
        undoName = self.commandQueue[-1]
        if undoName :
            self.commands[undoName].undo()
            self.commandQueue.pop(-1)

    def clean(self):
        self.commandQueue = []

class Client():
    def __init__(self,size) -> None:
        self.size = size
        self.screen = []
        for i in range(size):
            self.screen.append([])
            for _ in range(size):
                self.screen[i].append("0")

    def outPut(self):
        for line in self.screen:
            print("".join(line))
        print("-----------------")

    def drawPoint(self,i,j):
        self.screen[i][j] = "1"

    def clearPoint(self,i,j):
        self.screen[i][j] = "0"

    def run(self,invorker):
        while True:
            self.outPut()
            cmd = input()
            if cmd == "undo":
                invorker.undo()
            elif cmd == "stop":
                break
            else:
                invorker.do(cmd)


if __name__ == "__main__":
    screenSize = 5
    c = Client(screenSize)
    invoker = Invoker()
    # set command 
    for i in range(screenSize):
        for j in range(screenSize):
            newCommand = DrawPointCommand(c,"DrawPoint",i,j)
            invoker.addCommand(newCommand)

    c.run(invoker)
