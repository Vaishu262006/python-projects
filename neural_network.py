# neural_network.py
import numpy as np

# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training data for XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Network architecture
input_size = 2
hidden_size = 2
output_size = 1
np.random.seed(42)

# Weights
W1 = np.random.uniform(size=(input_size, hidden_size))
b1 = np.random.uniform(size=(1, hidden_size))
W2 = np.random.uniform(size=(hidden_size, output_size))
b2 = np.random.uniform(size=(1, output_size))

# Training
lr = 0.5
for epoch in range(10000):
    # Forward pass
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, W2) + b2
    final_output = sigmoid(final_input)
    
    # Error
    error = y - final_output
    
    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden_output)
    
    # Update weights and biases
    W2 += hidden_output.T.dot(d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += X.T.dot(d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

print("Predicted outputs:")
print(final_output)