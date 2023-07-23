# Project: Fashion MNIST Image Classification using Convolutional Neural Networks (CNN)

This project demonstrates image classification using a Convolutional Neural Network (CNN) on the Fashion MNIST dataset. The code uses TensorFlow and includes normalization, early stopping with a custom callback, and a simple CNN model.

### Dataset
The Fashion MNIST dataset contains grayscale images of fashion items, each labeled with its corresponding class.

### Requirements
- TensorFlow
- NumPy
- Matplotlib

### Usage
1. Load the Fashion MNIST dataset and preprocess the data, including normalization.
2. Implement a custom callback (`myCallback`) for early stopping when the desired accuracy is achieved.
3. Create a convolutional neural network model (`convolutional_model`) with two Conv2D layers followed by MaxPooling2D layers, and fully connected Dense layers.
4. Compile the model with the Adam optimizer and sparse categorical cross-entropy loss function.
5. Train the model on the training data for 20 epochs, using the early stopping callback to terminate training when the accuracy reaches 99.5% or higher.
6. Evaluate the model on the validation data and print the evaluation results.
7. Make predictions on the validation data and display the predicted label and true label for the first {any} image.


### How to Run
Simply execute the provided Python script. Ensure that the required libraries are installed.

**Important:** The model training may take some time, depending on your hardware.

### Acknowledgments
The Fashion MNIST dataset is used under the TensorFlow Keras API. The CNN architecture is a basic example and can be modified for different image classification tasks.

Feel free to explore and improve the model for better accuracy and performance!