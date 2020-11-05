class Constraint:

    count = 0

    def __init__(self,challenge,operation):
        self.operation = operation
        self.challenge = challenge
        self.id = Constraint.count
        Constraint.count+=1

    def makeComplement(self):
        return

    #Removes all parts of a domain that are inconsistent with constraint
    def pruneDomain(self,domain = []):
        modified = False
        for x in domain:
            if self.challenge != x:
                domain.remove(x)
                modified = True
                print("Constraint.py > pruneDomain()> Removed",x)  
        return domain, modified