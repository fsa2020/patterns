# 提供统一接口增加子系统可用性
# 一键开机
class BoostFacade:
    def __init__(self,power,displayer,sound) -> None:
        self.power = power
        self.displayer = displayer
        self.sound = sound
    def oneBtnBootUp(self):
        self.power.on()
        self.displayer.switchOn()
        self.sound.switchOn()
        self.displayer.show()
        self.sound.play()
        # ... etc
class Power:
    def on(self):
        print("Power on")
    def off(self):
        print("Power off")

class Displayer:
    def switchOn(self):
        print("displayer on")
    def show(self):
        print("######\n######")

class Sound:
    def switchOn(self):
        print("sound on")
    def play(self):
        print("ohhh~~~")

if __name__ == "__main__":
    t = BoostFacade(Power(),Displayer(),Sound())
    t.oneBtnBootUp()
