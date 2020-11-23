from .. import *

class Solver():
    def __init__(self, event: Event) -> None:
        self.event = event
        self.mainIndex = 0
        return

    def __repr__(self) -> str:
        return "Solver: Event:%s"%(self.event)

    def _makeInverse(self, const: Constraint) -> Constraint:
        return Constraint((const.scope[1],const.scope[0]),const.relation,const.testTrue,const.priority)

    def solve(self) -> None:
        #1 Arc consistency check
        #2 Compare all permutations

        constraints = []
        variables = []

        # Get event constraints
        for const in self.event.event.constraints:
            constraints.append(const)
        
        # Get reference and assign value to event variables
        for var in self.event.event.variables:
            if isinstance(var, UnaryVariable):
                variables.append([var.uuid,var.domain])
            elif isinstance(var, Variable):
                variables.append([var.uuid,var.domain[0]])

        # Get user constraints
        for constraintSet in self.event.users:
            for const in constraintSet.constraints:
                constraints.append(const)
            
            for var in constraintSet.variables:
                if isinstance(var, UnaryVariable):
                    variables.append([var.uuid,var.domain])
                elif isinstance(var, Variable):
                    variables.append([var.uuid,var.domain[0]])

        #TODO For each value of "date" variable test the constraints against domains & rate that date /100
        #TODO date variables should be set as events "main" variable




        print(variables)
        #print(constraints)
