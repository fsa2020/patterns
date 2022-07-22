class State:
    def __init__(self,target) -> None:
        self.target = target 
    def turn(self):
        self.target.curState = self

class Idle(State):
    def sleep(self):
        print(self.target,"is idle")

class Offensive(State):
    def offence(self):
        print(self.target,"is Offensive")

class Monster:
    def __init__(self) -> None:
        self.idleState = Idle(self)
        self.OffensiveState = Offensive(self)
        self.curState = self.idleState
    def findPlayer(self):
        self.OffensiveState.turn()
        self.curState.offence()
    def getTired(self):
        self.idleState.turn()
        self.curState.sleep()

if __name__ == "__main__":
    m = Monster()
    m.getTired()
    m.findPlayer()
    m.getTired()

