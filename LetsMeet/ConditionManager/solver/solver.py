from .. import *
from copy import deepcopy

class Solver():
    def __init__(self, event: Event) -> None:
        self.event = event
        self.mainIndex = 0
        self.matches = {}
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
        for var in self.event.event.variables.keys():
            event_variables.append(self.event.event.variables[var])

        # Get all user constraints & variables
        for x in self.event.users:
            for const in (self.event.users[x].constraints):
                constraints.append(self.event.users[x].constraints[const])
            
            for var in (self.event.users[x].variables.keys()):
                user_variables.append(self.event.users[x].variables[var])

        #print("Solver Variable References: ", user_variables + event_variables)
        #print("Solver Constraints: ", constraints)

        """For each constraint
        We want to see which ones are true"""
        for con in constraints:
            # For each constraint
            #TODO   1. Choose a value from each variables domain

            dom1, dom2 = con.scope
            dom1 = dom1.domain
            dom2 = dom2.domain

            #TODO   2. Test if this selection of values satisfies the constraints.
            #       If all constraints are satisfied rank = 100, else rank is dependant on number of constraints satisfied and their priority level
            for v in dom1:
                # Iterate over dom1 variables

                for v2 in dom2:
                    # Iterate over dom2 variables
                    # Check if dom2 is within dom1
                    if v.start <= v2.start and v.end >= v2.end:
                        self.match(v2)

        # Print matches
        print("MATCHES: ", self.matches)
        print("Optimal Time: ", self.matchesMax())

        #TODO Optimise this solver by only checking permutations that are centered around the date variable
        #TODO Optimise this solver by checking for arc consistency first (AC-3) and removing non consistent values from domain


        return

    def match(self, time):
        time = str(time)
        # Check self.matches to see if the time has already been matched
        if time in self.matches.keys():
            # If it has then plus 1 to the corresponding dict value
            self.matches[time] += 1
        else:
            # If not add it to dict with value 1
            self.matches[time] = 1

    def matchesMax(self):
        """Return match with most occurrences"""
        maximum = -1
        maximum_time = None
        for i in self.matches.keys():
            if self.matches[i] > maximum:
                maximum = self.matches[i]
                maximum_time = i

        return maximum_time
