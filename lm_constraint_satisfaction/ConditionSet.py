import uuid
from typing import List
from .variable import Variable
from .constraint import Constraint

class ConditionSet():
    count = 0

    #TODO input variable&constraint parameters caused crippling duplication bug. 
    #They are not neccesary and now removed. Why did bug occur?
    def __init__(self):
        self.uuid = uuid.uuid1()
        self.name = "ConditionSet" + str(ConditionSet.count)
        self.variables = {}
        self.constraints = {}
        ConditionSet.count += 1

        return

    def __str__(self):
        return "ConditionSet: %s [%s],\n\tVariable count: %s \n\tConstraint count: %s" % (self.name, self.uuid, len(self.variables),len(self.constraints))

    def printFull(self):
        print(self)
        for x in self.variables:
            self.variables[x].printFull()
        for x in self.constraints:
            self.constraints[x].printFull()

    def addVariable(self,variable):
        '''Adds a variable set and returns its index'''
        if isinstance(variable, Variable):
            self.variables[variable.uuid] = variable
        return variable
    
    def addConstraint(self, constraint):
        '''Adds a constraint set and returns its index'''
        if isinstance(constraint, Constraint):
            self.constraints[constraint.uuid] = constraint
        return constraint