import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load and preprocess the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# One-hot encode the labels
encoder = OneHotEncoder()
y_onehot = encoder.fit_transform(y.reshape(-1, 1)).toarray()  # Convert to dense array

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_onehot, test_size=0.2, random_state=42)

# Define a quantum device
n_qubits = 3  # Match the number of classes
dev = qml.device('default.qubit', wires=n_qubits)

# Define a quantum node
@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    # Ensure the number of inputs does not exceed the number of qubits
    for i in range(n_qubits):
        qml.RY(inputs[i % len(inputs)], wires=i)  # Wrap around if needed
    
    for i in range(n_qubits):
        qml.RX(weights[i], wires=i)
        qml.RY(weights[n_qubits + i], wires=i)
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# Define a hybrid quantum-classical model
def hybrid_model(inputs, weights):
    return quantum_circuit(inputs, weights)

# Initialize weights
np.random.seed(0)
weights = np.random.normal(0, np.pi, (2 * n_qubits,))

# Define a cost function
def cost(weights):
    predictions = np.array([hybrid_model(x, weights) for x in X_train])
    loss = np.mean((predictions - y_train) ** 2)
    return loss

# Optimize the weights using gradient descent
opt = qml.GradientDescentOptimizer(stepsize=0.1)
steps = 100
for i in range(steps):
    weights = opt.step(cost, weights)
    if i % 10 == 0:
        print(f"Step {i}, Cost: {cost(weights)}")

# Test the model
predictions = np.array([hybrid_model(x, weights) for x in X_test])
predicted_labels = np.argmax(predictions, axis=1)
true_labels = np.argmax(y_test, axis=1)

# Calculate the accuracy
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
