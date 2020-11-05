from .variable import Variable


class RangeVariable(Variable):

    def __init__(self,domStart=0,domEnd=0,name="RangeVariable1"):
        Variable.__init__(self,[domStart,domEnd],name)
    
    def addDomain(self, domStart,domEnd):
        self.domain.append([domStart,domEnd])

