import uuid

class Constraint:

    count = 0

    def __init__(self,scope = (None,None), relation = None, testTrue = True, priority = 0.5):
        self.name = "Constraint"+str(Constraint.count)
        self.uuid = uuid.uuid1()
        self.scope = scope
        self.relation = relation
        self.testTrue = testTrue
        self.priority = priority
        Constraint.count += 1

    def __str__(self):
        return "Constraint: %s [%s]\n\tscope: %s\n\trelation: %s\n\ttestTrue: %s\n\tpriority: %s" % (self.name, self.uuid, self.scope,self.relation,self.testTrue,self.priority)

    def printFull(self):
        print(self)

    def makeComplement(self):
        return

    #Removes all parts of a domain that are inconsistent with constraint
    #TODO depreciate?
    def pruneDomain(self,domain = []):
        modified = False
        for x in domain:
            if self.challenge != x:
                domain.remove(x)
                modified = True
                print("Constraint.py > pruneDomain()> Removed",x)  
        return domain, modified