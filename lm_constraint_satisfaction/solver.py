class Solver:
    def __init__(self):
        self.variables = []
        self.constraints = []

    def addVariable(self,var):
        self.variables.append(var)

    def addConstraint(self,const):
        self.constraints.append(const)
    
    def solve(self):
        print("That's optimistic - Not implemented :D")
