import torch
import torch.nn as nn
import torch.optim as optim

#Choose which activation function to use in code
defined_activation_function = 'relu'

activation_functions = {
    'relu': nn.ReLU(),
    'sigmoid': nn.Sigmoid(),
    'tanh': nn.Tanh(),
    'leaky_relu': nn.LeakyReLU()
}

# Initializing hyperparameters
num_samples = 100
batch_size = 10
num_epochs = 150
learning_rate = 0.001

# Define a simple synthetic dataset
def generate_data(num_samples):
    X = torch.randn(num_samples, 10)
    y = torch.randn(num_samples, 1)
    return X, y

# Generate synthetic data
X, y = generate_data(num_samples)

class SimpleModel(nn.Module):
    def __init__(self, activation=defined_activation_function):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(in_features=10, out_features=18)
        self.fc2 = nn.Linear(in_features=18, out_features=18)
        self.fc3 = nn.Linear(in_features=18, out_features=4)
        self.fc4 = nn.Linear(in_features=4, out_features=1)
        self.activation = activation_functions[activation]

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x) 
        x = self.activation(x)
        x = self.fc3(x) 
        x = self.activation(x)  
        x = self.fc4(x) 
        return x

# Initialize the model, define loss function and optimizer
model = SimpleModel(activation=defined_activation_function)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    for i in range(0, num_samples, batch_size):
        # Get the mini-batch
        inputs = X[i:i+batch_size]
        labels = y[i:i+batch_size]

        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(inputs)

        # Compute the loss
        loss = criterion(outputs, labels)

        # Backward pass and optimize
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss}')

print("Training complete.")