from .utilities import Operation
from . import Constraint

class DateTimeConstraint(Constraint):
    def __init__(self,startDateTime, endDateTime,operation):
        Constraint.__init__(self,operation)
        self.startDateTime = startDateTime
        self.endDateTime = endDateTime
