from lm_constraint_satisfaction.constraint import Constraint
import lm_constraint_satisfaction as lmcs
import datetime



# Setup data for new event
dateVariable = lmcs.Variable([1,2,3,4,5])
participantsVariable = lmcs.Variable([])
eventConditionSet = lmcs.ConditionSet([dateVariable,participantsVariable])
event = lmcs.Event(eventConditionSet)

# It's also posible to create an event in short-form
event2 = lmcs.Event(lmcs.ConditionSet([lmcs.Variable(["1,2,3"]),lmcs.Variable(["Geoff,Bob"])]))

# Enter a participants data
participantDateVariable = lmcs.Variable([2,3])
participantDateConstraint = lmcs.Constraint((dateVariable.uuid,participantDateVariable.uuid),"=") # Create constraint referecing variables UUIDs
optimalConstraint = lmcs.Constraint((event.event.constraints[0],event.users[0].variables[0]),"=") # Create constraint using variables indexes (More performant, use whenever possible)
conditionset = lmcs.ConditionSet([participantDateVariable],[participantDateConstraint,optimalConstraint])
event.addUserConditionSet(conditionset)


event.printFull()

# Index positions related to UUID are stored in dictionary
print("\n")
print(event.usersDict)
print(event.users[event.usersDict[conditionset.uuid]])