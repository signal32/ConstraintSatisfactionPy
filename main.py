import lm_constraint_satisfaction as lmcs
import datetime


# Setup conditions for event
eventConditionSet = lmcs.ConditionSet()
dateVariable = eventConditionSet.addVariable(lmcs.Variable([
    lmcs.types.DateRange(datetime.datetime(1999,1,9,12),datetime.datetime(1999,1,9,14)),
    lmcs.types.DateRange(datetime.datetime(1999,1,9,17),datetime.datetime(1999,1,9,20))]))
participantCount = eventConditionSet.addVariable(lmcs.UnaryVariable(0))

# Create event with conditions
event = lmcs.Event(eventConditionSet)

# Add a new participant to the event
participant1 = event.addUserConditionSet(lmcs.ConditionSet())
userDate = event.users[participant1].addVariable(lmcs.Variable([lmcs.types.DateRange(datetime.datetime(1989,1,9,12),datetime.datetime(1989,1,9,14))]))
event.users[participant1].addConstraint(lmcs.Constraint((event.event.variables[dateVariable],event.users[participant1].variables[userDate]),"="))


event.printFull()
# Index positions related to UUID are stored in dictionary
print("\n")
print(event.usersDict)

print("\n")
range1 = lmcs.types.DateRange(datetime.datetime(1999,1,5,5),datetime.datetime(1999,1,12,4))
range2 = lmcs.types.DateRange(datetime.datetime(1999,1,5,5),datetime.datetime(1999,1,13,5))
print(range1, "\n", range2)
print (range1 == range2)

solver = lmcs.solver.Solver(event)

solver.solve()