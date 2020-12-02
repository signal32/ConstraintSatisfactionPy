from LetsMeet.ConditionManager.Event import Event
from datetime import datetime

from .variable import Variable
from .UnaryVariable import UnaryVariable
from .constraint import Constraint
from .ConditionSet import ConditionSet
from .types import DateRange

from ..EventManager import Manager as EventMan

class Manager():

    def __init__(self, conditionSet: ConditionSet = ConditionSet()):
        self.conditionSet = conditionSet
        self.eventID = None
        self.event = None #This is a bodge to get around lack of pointers in python
        return

    @classmethod
    def fromUUID(cls, uuid: object):
        #TODO get event with this UUID from storage model and initialise class
        conditions = ConditionSet()
        conditions.uuid = uuid
        return cls(open(conditions,))

    def initBlank(self):
        self.conditionSet.constraints = []
        self.conditionSet.variables = []
        return

    def setProperty(self,key,value):
        if key == "name":
            self.conditionSet.name = key
        else:
            #TODO dictionary
            pass
        return

    def getID(self):
        return self.conditionSet.uuid

    def setDateRange(self, startDate: datetime, endDate: datetime):
        val = self.conditionSet.addVariable(Variable(DateRange(startDate,endDate,30)))
        self._bindToEvent()
        return val

    def _bindToEvent(self):
        self.event.addUserConditionSet(self.conditionSet) #This is a bodge to get around lack of pointers in python, proper code below
        if False:
            man = EventMan().fromUUID(self.eventID)
            man.event.addUserConditionSet(self.conditionSet)


