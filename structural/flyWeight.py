# 大量对象以及子类对象拥有相同的属性时可用享元模式节省空间
class Body():
    intrinsicState = {}
    intrinsicState["head"] = "o"
    intrinsicState["body"] = "+"
    intrinsicState["leg"] = "/\\"
    intrinsicState["deadPose"] = "orz"
    def __init__(self,extrinsicState) -> None:
        self.extrinsicState = extrinsicState
    def getAwards(self):
        return self.extrinsicState["awards"]

class NpcBody(Body):
    def getAwards(self):
        print("Npc has coin")
        return self.extrinsicState["awards"]

class MonsterBody(Body):
    def getAwards(self):
        print("Monster has food")
        return self.extrinsicState["awards"]

if __name__ == "__main__":
    body1 = Body({"awards":"coin "})
    body2 = Body({"awards":"coin and food"})
    print(id(body1.intrinsicState),body1.intrinsicState["deadPose"],body1.extrinsicState["awards"])
    print(id(body2.intrinsicState),body2.intrinsicState["deadPose"],body2.extrinsicState["awards"])

    body1 = NpcBody({"awards":"coin"})
    body2 = MonsterBody({"awards":"food"})
    print(id(body1.intrinsicState),body1.intrinsicState["deadPose"],body1.extrinsicState["awards"])
    print(id(body2.intrinsicState),body2.intrinsicState["deadPose"],body2.extrinsicState["awards"])

