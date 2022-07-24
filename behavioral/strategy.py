# method cluster
class Monster:
    def attack(self)->float:
        raise NotImplementedError
    def setAttackStrategy(self,strategy):
        self.attack = strategy

# attack method cluster
def normalAttack():
    print("normalAttack")
    return 1
def criticalAttack():
    print("criticalAttack")
    return 2

Attack = {
    "normal":normalAttack,
    "critical":criticalAttack}

if __name__ == "__main__":
    m = Monster()
    m.setAttackStrategy(Attack["normal"])
    m.attack()
    m.setAttackStrategy(Attack["critical"])
    m.attack()

