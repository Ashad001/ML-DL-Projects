# Handwritten Digit Classification

This project focuses on building a machine learning model for handwritten digit classification. The model is trained using the Keras MNIST dataset, employing a Sequential model architecture with dense layers. The trained model is then tested on images using OpenCV.

## Features

- **Dataset:** The model is trained on the MNIST dataset, which consists of thousands of grayscale images of handwritten digits (0-9).
- **Model Architecture:** A Sequential model is employed, consisting of dense layers. This architecture allows for straightforward stacking of layers one after another.
- **Preprocessing:** Prior to training, the dataset is preprocessed to normalize and standardize the images. This ensures consistent input for the model and improves its performance.
- **Training:** The model is trained using the labeled images and their corresponding digit labels. The training process adjusts the model's parameters to minimize the error and improve accuracy.
- **Testing:** To evaluate the model's performance, it is tested on new images of handwritten digits. OpenCV is utilized for image handling and feeding the images to the trained model.
- **Evaluation:** The model's accuracy and performance metrics are measured using various evaluation metrics such as accuracy, precision, recall, and F1-score. These metrics provide insights into how well the model performs in classifying the handwritten digits.

## Requirements

- Python 3.x
- Keras
- OpenCV
- Numpy
- Matplotlib


Feel free to explore and experiment with different model architectures, hyperparameters, and evaluation techniques to further enhance the handwritten digit classification accuracy.