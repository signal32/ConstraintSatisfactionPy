import lm_constraint_satisfaction as lmcs


solver = lmcs.Solver()

# Add all variables
solver.addVariable(lmcs.DateTimeVariable("arbitaryname",lmcs.DateTime(5,3),lmcs.DateTime(10,6)))
solver.addVariable(lmcs.DateTimeVariable("anothername",lmcs.DateTime(45,9),lmcs.DateTime(45,14)))

print(lmcs.Variable.count)

# Add all constraints
solver.addVariable(lmcs.DateTimeConstraint(lmcs.DateTime(6,7),lmcs.Operation.WITHIN))


print(lmcs.Constraint.count)