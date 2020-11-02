from .utilities import Operation



class Constraint:

    count = 0

    def __init__(self,operation):
        if isinstance(operation,Operation):
            self.operation = operation
            self.id = Constraint.count
            Constraint.count+=1