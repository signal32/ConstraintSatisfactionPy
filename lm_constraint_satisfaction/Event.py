import uuid
from typing import List
from .ConditionSet import ConditionSet

class Event():

    count = 0

    def __init__(self,eventConditionSet: ConditionSet = None, userConditionSets: List[ConditionSet] = [], name = "Event " + str(count)):
        self.name = name
        self.uuid = uuid.uuid1()
        self.event = eventConditionSet
        self.eventMain = 0
        self.users = userConditionSets
        self.usersDict = {}
        self.lut = False
        #Event.count += 1 #TODO fix counter

        # Generate dictionary for variables & constraints in constructor
        for i, user in enumerate(self.users):
            if isinstance(user, ConditionSet):
                self.usersDict[user.uuid] = i
        return

    def __str__(self):
        return "Event: %s [%s]\n\tUser count: %s" % (self.name, self.uuid, len(self.users))

    def __repr__(self) -> str:
        return "Event: %s [%s] User count: %s" % (self.name, self.uuid, len(self.users))

    def printFull(self):
        print(self)
        self.event.printFull()        
        for x in self.users:
            x.printFull()
        return

    def addUserConditionSet(self,userConditionSet):
        '''Adds a user condition set and returns its index вы читать этот??'''
        self.users.append(userConditionSet)
        self.usersDict[userConditionSet.uuid] = len(self.users) - 1
        return len(self.users) - 1