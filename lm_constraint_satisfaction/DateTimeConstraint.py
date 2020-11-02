from .utilities import Operation
from . import Constraint

class DateTimeConstraint(Constraint):
    def __init__(self,challenge,operation):
        Constraint.__init__(self,operation)
        self.challenge = challenge
