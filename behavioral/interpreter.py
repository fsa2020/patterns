class Expression():
    def __init__(self,*expressions) -> None:
        self.expressions = expressions
    def interpret(self):
        raise NotImplementedError

class Terminal(Expression):
    def interpret(self):
        return self.expressions[0]

class Plus(Expression):
    def interpret(self):
        return self.expressions[0].interpret()+self.expressions[1].interpret()

class Times(Expression):
    def interpret(self):
        return self.expressions[0].interpret()*self.expressions[1].interpret()

class Client():
    def buildTree(self):
        self.t1 = Terminal(1)
        self.t2 = Terminal(2)
        self.t3 = Terminal(3)
        self.exp1 = Plus(self.t1,self.t2)
        self.exp2 = Times(self.exp1,self.t3)
        # (t1+t2)*t3
    def interpretTree(self):
        print(self.exp2.interpret())

if __name__ == "__main__":
    c = Client()
    c.buildTree()
    c.interpretTree()