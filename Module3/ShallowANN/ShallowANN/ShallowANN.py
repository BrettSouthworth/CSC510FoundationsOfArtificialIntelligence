import numpy as np

class TwoLayerANN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        np.random.seed(50) # set seed for repeatability during testing
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.biases_hidden = np.zeros(hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.biases_output = np.zeros(output_size)

    # sigmoid and its derivative
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
    
    def sigmoid_deriv(self, x):
        return x * (1 - x)
    
    # Normalize array
    def normalize(X, axis=-1, order=2):
        l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
        l2[l2 == 0] = 1
        return X / np.expand_dims(l2, axis)
    
    
    def feedforward(self, X):
        self.hidden_output = self.sigmoid(np.dot(X, self.weights_input_hidden) + self.biases_hidden)
        self.output = self.sigmoid(np.dot(self.hidden_output, self.weights_hidden_output) + self.biases_output)
        return self.output
    
    def backward(self, X, y, learning_rate):
        # output layer error
        output_error = y - self.output
        output_delta = output_error * self.sigmoid_deriv(self.output)
        
        # hidden layer error
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_deriv(self.hidden_output)
        
        # Update weights/biases
        self.weights_hidden_output += np.dot(self.hidden_output.T, output_delta) * learning_rate
        self.biases_output += np.sum(output_delta) * learning_rate
        self.weights_input_hidden += np.dot(X.T, hidden_delta) * learning_rate
        self.biases_hidden += np.sum(hidden_delta) * learning_rate
        
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.feedforward(X)
            self.backward(X, y, learning_rate)
            if epoch % 100 == 0:
                error = np.mean(np.square(y - output))
                print(f'Epoch {epoch}: Error {error:.4f}')
                
    def predict(self, X):
        return np.round(self.feedforward(X))

# Sample Code
if __name__ == "__main__":
    ## Hardcoded testing values
    ## input
    #X = np.array([[0, 0],
    #              [0, 1],
    #              [1, 0],
    #              [1, 1]])
    ## output
    #y = np.array([[0],
    #              [1],
    #              [1],
    #              [0]])
    #input_size = 2
    #hidden_size = 3
    #output_size = 1
    
    input_size = int(input("Enter the number of input variables: "))
    hidden_size = int(input("Enter the number of hidden neurons: "))
    output_size = int(input("Enter the number of output neurons: "))

    X = []
    y = []
    
    num_samples = int(input("Enter the number of training samples: "))
    for i in range(num_samples):
        sample = input(f"Enter input values for sample {i+1} (separated by spaces): ").split()
        X.append([float(x) for x in sample])
        label = float(input(f"Enter output value for sample {i+1}: "))
        y.append(label)
    
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)

    # Hardcoded based on assignmnet
    epochs = 1000
    learning_rate = 0.1

    ann = TwoLayerANN(input_size, hidden_size, output_size)
    ann.train(X, y, epochs, learning_rate)

    # Test prediction
    input_list = [float(x) for x in input("Enter test input (separated by spaces): ").split()]
    test_input = np.array(input_list)
    print("Prediction for [1, 0]:", ann.predict(test_input))