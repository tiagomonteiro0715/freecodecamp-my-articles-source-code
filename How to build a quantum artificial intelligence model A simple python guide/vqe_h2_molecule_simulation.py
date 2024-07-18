import pennylane as qml
from pennylane import numpy as np

# Define the molecule (H2 at bond length of 0.74 Å)
symbols = ["H", "H"]
coordinates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.74])

# Generate the Hamiltonian for the molecule
hamiltonian, qubits = qml.qchem.molecular_hamiltonian(
    symbols, coordinates
)

# Define the quantum device
dev = qml.device("default.qubit", wires=qubits)

# Define the ansatz (variational quantum circuit)
def ansatz(params, wires):
    qml.BasisState(np.array([0] * qubits), wires=wires)
    for i in range(qubits):
        qml.RY(params[i], wires=wires[i])
    for i in range(qubits - 1):
        qml.CNOT(wires=[wires[i], wires[i + 1]])

# Define the cost function
@qml.qnode(dev)
def cost_fn(params):
    ansatz(params, wires=range(qubits))
    return qml.expval(hamiltonian)

# Set a fixed seed for reproducibility
np.random.seed(42)

# Set the initial parameters
params = np.random.random(qubits, requires_grad=True)

# Choose an optimizer
optimizer = qml.GradientDescentOptimizer(stepsize=0.4)

# Number of optimization steps
max_iterations = 100
conv_tol = 1e-06

# Optimization loop
energies = []

for n in range(max_iterations):
    params, prev_energy = optimizer.step_and_cost(cost_fn, params)

    energy = cost_fn(params)
    energies.append(energy)
    if np.abs(energy - prev_energy) < conv_tol:
        break

    print(f"Step = {n}, Energy = {energy:.8f} Ha")

print(f"Final ground state energy = {energy:.8f} Ha")

# Visualize the results
import matplotlib.pyplot as plt

iterations = range(len(energies))

plt.plot(iterations, energies)
plt.xlabel('Iteration')
plt.ylabel('Energy (Ha)')
plt.title('Convergence of VQE for H2 Molecule')
plt.show()
