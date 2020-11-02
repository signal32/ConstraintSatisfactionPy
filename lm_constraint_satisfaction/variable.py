class Variable:
    count = 0

    def __init__(self,name):
        self.name = name
        self.id = Variable.count
        Variable.count += 1
