
from lm_constraint_satisfaction.variable import Variable


class Solver:
    def __init__(self):
        self.variables = []
        self.constraints = []

    def addVariable(self,var):
        self.variables.append(var)

    def addConstraint(self,const):
        self.constraints.append(const)
    
    def solve(self):
        self._makeArcConsistent()

    def _makeArcConsistent(self):
        agenda = []

        for constraint in self.constraints:
            agenda.append(constraint)
            # TODO add complement of dynamic constraints

        while len(agenda)>0:
            constraint = agenda.pop()

            for var in self.variables:
                # Skip testing unmatching constraints
                if var.name != constraint.challenge:
                    continue

                # Remove any variable domains where it does not match constraint
                else:
                    var.domain, modifeid = constraint.pruneDomain(var.domain)
                    
                    # If domain has been modified add it's dependand constraints to agenda
                    if modifeid:
                        pass
        print("Made Arc Consistent")


