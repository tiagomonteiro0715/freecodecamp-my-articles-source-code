import sympy as sp

# Define the variable and function
t = sp.symbols('t')
F = sp.Function('F')(t)

# Define the function to be transformed
f = sp.exp(-2*t)

# Perform the Laplace transform
F_transformed = sp.laplace_transform(f, t, sp.symbols('s'))

# Print the result
print("Original Function f(t): ", f)
print("Laplace Transform F(s): ", F_transformed[0])
