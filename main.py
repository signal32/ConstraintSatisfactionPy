import lm_constraint_satisfaction as lmcs


solver = lmcs.Solver()

# Add all variables - 
# A DateTimeVariable is a "time ranges" the  COULD take place
solver.addVariable(lmcs.DateTimeVariable("arbitaryname",lmcs.DateTime(5,3),lmcs.DateTime(10,6)))
solver.addVariable(lmcs.DateTimeVariable("anothername",lmcs.DateTime(45,9),lmcs.DateTime(45,14)))

print(lmcs.Variable.count)

# Add all constraints
solver.addConstraint(lmcs.DateTimeConstraint(lmcs.DateTime(6,7),lmcs.DateTime(5,2),lmcs.Operation.WITHIN))  # Says event date/time must be in this range

print(lmcs.Constraint.count)


# Solve
solver.solve()