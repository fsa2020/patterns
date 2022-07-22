# 按规定顺序创建对象
# build by step in super __init__
class builder():
    def __init__(self) -> None:
        self.buildStep1()
        self.buildStep2()
    def buildStep1(self):
        raise NotImplemented
    def buildStep2(self):
        raise NotImplemented

class myBuilder(builder):
    def buildStep1(self):
        print("step1")
    def buildStep2(self):
        print("step2")

if __name__ == "__main__":
    myBuilder()