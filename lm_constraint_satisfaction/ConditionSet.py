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
        self.variables = []
        self.constraints = []
        self.variablesDict = {}
        self.constraintsDict = {}
        ConditionSet.count += 1

        # Generate dictionary for variables & constraints in constructor
        for i, var in enumerate(self.variables):
            if isinstance(var,Variable):
                self.variablesDict[var.uuid] = i 
        for i, cons in enumerate(self.constraints):
            if isinstance(cons, Constraint):
                self.constraintsDict[cons.uuid] = i
        return

    def __str__(self):
        return "ConditionSet: %s [%s],\n\tVariable count: %s \n\tConstraint count: %s" % (self.name, self.uuid, len(self.variables),len(self.constraints))

    def printFull(self,):
        print(self)
        for x in self.variables:
            x.printFull()
        for x in self.constraints:
            x.printFull()

    def addVariable(self,variable):
        '''Adds a variable set and returns its index'''
        if isinstance(variable, Variable):
            self.variables.append(variable)
        return len (self.constraints) 
    
    def addConstraint(self, constraint):
        '''Adds a constraint set and returns its index'''
        if isinstance(constraint, Constraint):
            self.constraints.append(constraint)
        return len(self.constraints)