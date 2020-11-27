from .. import *
from copy import deepcopy

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
        event_variables = []
        user_variables = []

        # Get event constraints
        for x in self.event.event.constraints:
            #constraints.append(const)
            constraints.append(self.event.event.constraints[x])
            
        # Get reference to event variables
        print(self.event.event.variables)
        for var in self.event.event.variables.keys():
            event_variables.append(self.event.event.variables[var])

        # Get all user constraints & variables
        for x in self.event.users:
            for const in (self.event.users[x].constraints):
                constraints.append(self.event.users[x].constraints[const])
            
            for var in (self.event.users[x].variables.keys()):
                user_variables.append(self.event.users[x].variables[var])

        print("Solver Variable References: ", user_variables + event_variables)
        print("Solver Constraints: ", constraints)

        """For each constraint
        We want to see which ones are true"""
        for con in constraints:
            # For each constraint
            #TODO   1. Choose a value from each variables domain

            print(con)
            dom1, dom2 = con.scope
            dom1 = dom1.domain
            dom2 = dom2.domain

            #print("\n\n", dom1)
            #print(dom2)

            #TODO   2. Test if this selection of values satisfies the constraints.
            #       If all constraints are satisfied rank = 100, else rank is dependant on number of constraints satisfied and their priority level
            for v in dom1:
                # Iterate over dom1 variables
                print("\n\nv: ", v)
                print("v.start: ", v.start)

                for v2 in dom2:
                    # Iterate over dom2 variables
                    print("v2: ", v2)
                    print("v2.start: ", v2.start)

                    # Check if dom2 is within dom1
                    if v.start <= v2.start and v.end >= v2.end:
                        print("Match: ", v," & ", v2)



        #TODO   3. Repeat steps 1 & 2 until all permutations have been tested

        # TODO, Make system work with more than one user?

        #TODO Optimise this solver by only checking permutations that are centered around the date variable
        #TODO Optimise this solver by checking for arc consistency first (AC-3) and removing non consistent values from domain


        return
