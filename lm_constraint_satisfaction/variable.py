import uuid

class Variable:
    count = 0

    def __init__(self,domain = []):
        self.name = "Variable" +str(Variable.count)
        self.uuid = uuid.uuid1()
        self.domain = domain
        Variable.count += 1
        return

    def __repr__(self) -> str:
        return "Variable: %s [%s] Domain: %s" % (self.name, self.uuid, self.domain)

    def __str__(self):
        return "Variable: %s [%s]\n\tDomain: %s" % (self.name, self.uuid, self.domain)

    def printFull(self):
        print(self)

    def addDomain(self,domain):
        '''Adds a domain set and returns its index'''
        self.domain.append(domain)
        return len(self.domain) -1 
