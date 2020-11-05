import lm_constraint_satisfaction as lmcs
import datetime

x = datetime.datetime.now()
y = datetime.datetime(2005,7,4)
tst = datetime.datetime(2000,8,2)
if y <= tst <= x:
    print("ayy")




date = lmcs.RangeVariable(datetime.datetime(2020,1,4,5),datetime.datetime(2020,1,4,12),"date")
date.addDomain(datetime.datetime(2020,1,6,5),datetime.datetime(2020,1,7,18))

solver = lmcs.Solver()
solver.addVariable(date)

print(lmcs.Variable.count)

# Add all constraints
solver.addConstraint(lmcs.RangeConstraint(datetime.datetime(2020,1,4,8),datetime.datetime(2020,1,4,9),"date",lmcs.RangeConstraint.Op.WITHIN))  # Says event date/time must be in this range
solver.addConstraint(lmcs.RangeConstraint(datetime.datetime(2020,1,5,1),datetime.datetime(2020,1,12,23),"date",lmcs.RangeConstraint.Op.WITHIN))


print(lmcs.Constraint.count)


# Solve
solver.solve()