from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

expression = 2 * x + 4 * y
type(expression)

constraint = 2 * x + 4 * y >= 8
type(constraint)

# Add the constraints to the model
model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

# Add the objective function to the model
obj_func = x + 2 * y
model += obj_func

# Otra alternativa
# # Add the objective function to the model
# model += x + 2 * y

# Add the objective function to the model
model += lpSum([x, 2 * y])

print(model)

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
# status: 1, Optimal

print(f"objective: {model.objective.value()}")
# objective: 16.8181817

for var in model.variables():
    print(f"{var.name}: {var.value()}")

# x: 7.7272727
# y: 4.5454545

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

# red_constraint: -9.99999993922529e-08
# blue_constraint: 18.181818300000003
# yellow_constraint: 3.3636362999999996
# green_constraint: -2.0000000233721948e-07)

model.variables() #[x,y]
model.variables()[0] is x #true
model.variables()[1] is y #true

model.solver #devuelve el solver is CBC