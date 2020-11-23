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
        for x in self.event.event.constraints:
            #constraints.append(const)
            constraints.append(self.event.event.constraints[x])
            
        # Get reference to event variables
        for var in self.event.event.variables:
            variables.append(var)

        # Get all user constraints & variables
        for x in self.event.users:
            for const in (self.event.users[x].constraints):
                constraints.append(self.event.users[x].constraints[const])
            
            for var in (self.event.users[x].variables):
                variables.append(var)

        print("Solver Variable References: ",variables)
        print("Solver Constraints: ", constraints)

        #TODO   1. Choose a value from each variables domain
        #TODO   2. Test if this selection of values satisfies the constraints. 
        #       If all constraints are satisfied rank = 100, else rank is dependant on number of constraints satisfied and their priority level
        #TODO   3. Repeat steps 1 & 2 until all permutations have been tested

        #TODO Optimise this solver by only checking permutations that are centered around the date variable
        #TODO Optimise this solver by checking for arc consistency first (AC-3) and removing non consistent values from domain


        return
