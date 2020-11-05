from . import Constraint
from enum import Enum

class RangeConstraint(Constraint):

    class Op (Enum):
        WITHIN = 0

    def __init__(self,startDateTime, endDateTime,challenge,operation):
        Constraint.__init__(self,challenge,operation)
        self.startDateTime = startDateTime
        self.endDateTime = endDateTime

    def makeComplement(self):
        return RangeConstraint(self.endDateTime,self.startDateTime,self.operation)

    #Removes all parts of a domain that are inconsistent with constraint
    def pruneDomain(self,domain=[]):
        modifed = False
        for x in domain:
            if self.endDateTime <=x[0] or self.startDateTime >= x[1]:
                domain.remove(x)
                modified = True
                print("RangeConstraint.py > pruneDomain()> Removed",x)          
        return domain, modifed


