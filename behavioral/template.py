# use template to change a part of method pipeline
class Template:
    def __init__(self,defaultSteps) -> None:
        self.steps = defaultSteps
        self.stepDict = {}
        for step in self.steps:
            self.stepDict[step.name] = step

    def runPipeline(self):
        for step in self.steps:
            step.do()
        print("finished")

    def changeStep(self,name,newStep):
        if name in self.stepDict:
            stepOrder = self.steps.index(self.stepDict.pop(name))
            self.steps[stepOrder] = newStep
            self.stepDict[newStep.name] = newStep


class Method:
    def __init__(self,name,func) -> None:
        self.name = name
        self.func = func
    def do(self):
        self.func()

if __name__ == "__main__":
    def step1():
        print("step1")
    def step2():
        print("step2")
    def step3():
        print("step3")
    def step2_new():
        print("step2 new")
        
    steps = [
        Method("step1",step1),
        Method("step2",step2),
        Method("step3",step3)
    ]

    template = Template(steps)
    template.runPipeline()
    template.changeStep("step2",Method("step2new",step2_new))
    template.runPipeline()
    