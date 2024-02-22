# Example Python code using SciPy for optimization
from scipy.optimize import minimize

# Define the objective function to minimize (a simple quadratic function for illustration)
def objective_function(x):
    return x[0]**2 + x[1]**2

# Define constraints (e.g., x[0] + x[1] must be equal to 10)
def constraint_eq(x):
    return x[0] + x[1] - 10

# Define constraint in a form suitable for minimize function
con_eq = {'type': 'eq', 'fun': constraint_eq}

# Define bounds for x[0] and x[1] (e.g., both between 0 and 10)
bounds = [(0, 10), (0, 10)]

# Initial guess for the variables (e.g., [5, 5])
x0 = [5, 5]

# Perform the optimization
result = minimize(objective_function, x0, method='SLSQP', bounds=bounds, constraints=[con_eq])

# Output the optimal solution
print("Optimal values:", result.x)
print("Minimum cost:", result.fun)
