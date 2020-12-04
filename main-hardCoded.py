import LetsMeet as lmcs
import datetime


# Setup conditions for event
eventConditionSet = lmcs.ConditionManager.ConditionSet()
dateVariable = eventConditionSet.addVariable(lmcs.ConditionManager.Variable([
    lmcs.ConditionManager.types.DateRange(datetime.datetime(1999, 1, 9, 12), datetime.datetime(1999, 1, 9, 14)),
    lmcs.ConditionManager.types.DateRange(datetime.datetime(2020, 1, 1, 0), datetime.datetime(2020, 12, 31, 23, 59))]))
participantCount = eventConditionSet.addVariable(lmcs.ConditionManager.UnaryVariable(None))

# Use those conditions to initialise event
event = lmcs.EventManager.Event(eventConditionSet)

# Set up participant
participant1 = event.addUserConditionSet(lmcs.ConditionManager.ConditionSet())
event.users[participant1.uuid].name += " (participant 1)"
userDate = event.users[participant1.uuid].addVariable(lmcs.ConditionManager.Variable([lmcs.ConditionManager.types.DateRange(datetime.datetime(2020, 1, 1, 0), datetime.datetime(2020, 6, 30, 23))]))
event.users[participant1.uuid].addConstraint(lmcs.ConditionManager.Constraint((dateVariable, userDate), "="))

# Set up participant 2
# participant2 = event.addUserConditionSet(lmcs.ConditionManager.ConditionSet())
# event.users[participant2.uuid].name += " (participant 2)"
# userDate2 = event.users[participant2.uuid].addVariable(lmcs.ConditionManager.Variable([lmcs.ConditionManager.types.DateRange(datetime.datetime(1999, 1, 9, 12), datetime.datetime(1999, 1, 9, 14))]))
# event.users[participant2.uuid].addConstraint(lmcs.ConditionManager.Constraint((dateVariable, userDate2), "="))
# userDate3 = event.users[participant2.uuid].addVariable(lmcs.ConditionManager.Variable([lmcs.ConditionManager.types.DateRange(datetime.datetime(1999, 1, 9, 17), datetime.datetime(1999, 1, 9, 20))]))
# event.users[participant2.uuid].addConstraint(lmcs.ConditionManager.Constraint((dateVariable, userDate3), "="))

#event.printFull()

solver = lmcs.EventManager.solver.Solver(event)
solver.solve()