import lm_constraint_satisfaction as lmcs
import datetime


# Setup conditions for event
eventConditionSet = lmcs.ConditionSet()
dateVariable = eventConditionSet.addVariable(lmcs.Variable([
    lmcs.types.DateRange(datetime.datetime(1999, 1, 9, 12), datetime.datetime(1999, 1, 9, 14)),
    lmcs.types.DateRange(datetime.datetime(1999, 1, 9, 17), datetime.datetime(1999, 1, 9, 20))]))
participantCount = eventConditionSet.addVariable(lmcs.UnaryVariable(None))

# Use those conditions to initialise event
event = lmcs.Event(eventConditionSet)

# Set up participant
participant1 = event.addUserConditionSet(lmcs.ConditionSet())
event.users[participant1.uuid].name += " (participant 1)"
userDate = event.users[participant1.uuid].addVariable(lmcs.Variable([lmcs.types.DateRange(datetime.datetime(1999, 1, 9, 12), datetime.datetime(1999, 1, 9, 14))]))
event.users[participant1.uuid].addConstraint(lmcs.Constraint((dateVariable, userDate), "="))

# Set up participant 2
participant2 = event.addUserConditionSet(lmcs.ConditionSet())
event.users[participant2.uuid].name += " (participant 2)"
userDate2 = event.users[participant2.uuid].addVariable(lmcs.Variable([lmcs.types.DateRange(datetime.datetime(1999, 1, 9, 12), datetime.datetime(1999, 1, 9, 14))]))
event.users[participant2.uuid].addConstraint(lmcs.Constraint((dateVariable, userDate2), "="))
userDate3 = event.users[participant2.uuid].addVariable(lmcs.Variable([lmcs.types.DateRange(datetime.datetime(1999, 1, 9, 17), datetime.datetime(1999, 1, 9, 20))]))
event.users[participant2.uuid].addConstraint(lmcs.Constraint((dateVariable, userDate3), "="))

#event.printFull()

solver = lmcs.solver.Solver(event)
solver.solve()
