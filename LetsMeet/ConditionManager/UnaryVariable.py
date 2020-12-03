from. variable import Variable

class UnaryVariable(Variable):

    def __init__(self,domain) -> None:
        super().__init__(domain)

    def __repr__(self) -> str:
        return "UnaryVariable: %s [%s] Domain: %s" % (self.name, self.uuid, self.domain)

    def __str__(self) -> str:
        return "UnaryVariable: %s [%s]\n\tDomain: %s" % (self.name, self.uuid, self.domain)


    def addDomain(self, domain):
        '''Replaces domain with new instance'''
        self.domain = domain

