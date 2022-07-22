class Observer:
    def __init__(self) -> None:
        self.listeners = []
    def addListener(self,listener):
        self.listeners.append(listener)        
    def removeListener(self,listener):
        self.listeners.remove(listener)
    def removeAllListener(self):
        self.listeners = []
    def invokeListeners(self):
        for l in self.listeners:
            l.invoke()
                
class Listener:
    def __init__(self,i) -> None:
        self.id = i
    def invoke(self):
        print("invoked",self.id)

if __name__ == "__main__":
    obs = Observer()
    for i in range(5):
        obs.addListener(Listener(i))
    obs.invokeListeners()
    obs.removeAllListener()
    obs.invokeListeners()
