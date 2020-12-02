"""import uuid
from typing import Dict
from .ConditionSet import ConditionSet

class Event():

    count = 0

    def __init__(self,eventConditionSet: ConditionSet = None, userConditionSets: Dict[object,ConditionSet] = {}, name = None):
        self.name = name
        self.uuid = uuid.uuid1()
        self.event = eventConditionSet
        self.eventMain = 0
        self.users = userConditionSets
        self.lut = False
        if self.name == None:
            self.event = "Event" + str(Event.count)
        Event.count += 1 #TODO fix counter
        return

    def __str__(self):
        return "Event: %s [%s]\n\tUser count: %s" % (self.name, self.uuid, len(self.users))

    def __repr__(self) -> str:
        return "Event: %s [%s] User count: %s" % (self.name, self.uuid, len(self.users))

    def printFull(self):
        print(self)
        self.event.printFull()        
        for x in self.users:
            self.users[x].printFull()
        return

    def addUserConditionSet(self,userConditionSet: ConditionSet):
        '''Adds a user condition set and returns its index вы читать этот??'''
        self.users[userConditionSet.uuid] = userConditionSet
        return userConditionSet

"""