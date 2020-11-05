class Variable:
    count = 0

    def __init__(self,domain,name):
        self.name = name
        self.id = Variable.count
        self.domain = []
        self.domain.append(domain)
        Variable.count += 1

    def addDomain(self,domain):
        self.domain.append(domain)
