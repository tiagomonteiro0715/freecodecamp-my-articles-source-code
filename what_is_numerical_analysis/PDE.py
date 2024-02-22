# Example Python code using SciPy for solving a heat distribution problem in a rod
import numpy as np
from scipy.integrate import solve_bvp

# Define the differential equation representing heat transfer in the rod
def heat_equation(x, y):
    return np.vstack((y[1], -y[0]))

# Define boundary conditions
def boundary_conditions(ya, yb):
    return np.array([ya[0], yb[0] - 1])

# Setup the initial guess and the mesh
x = np.linspace(0, 1, 5)
y = np.zeros((2, x.size))

# Solve the BVP
sol = solve_bvp(heat_equation, boundary_conditions, x, y)

print(sol)