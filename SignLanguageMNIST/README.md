# Sign Language MNIST Multi-Class Classification Project

## Overview

In this project, we tackled a multi-class classification problem where the goal was to correctly classify images of hands depicting the 26 letters of the English alphabet using a Convolutional Neural Network (CNN). The dataset used for this task is the [Sign Language MNIST dataset](https://www.kaggle.com/datamunge/sign-language-mnist), which consists of 28x28 grayscale images representing each letter.

## Dataset

The [Sign Language MNIST dataset](https://www.kaggle.com/datamunge/sign-language-mnist) is available on Kaggle and comprises images of hands forming the 26 letters of the English alphabet in American Sign Language (ASL). Each image is a 28x28 grayscale image, making it suitable for input into a CNN model.

## Pre-processing

Before feeding the data into our CNN model, we needed to pre-process it appropriately. The pre-processing steps may have included:

- Scaling: Scaling the pixel values of the images to a range suitable for neural networks, often between 0 and 1.
- Reshaping: Reshaping the 28x28 images into a format compatible with the CNN input layer.
- Label Encoding: Encoding the target labels (letters) into numerical format for training purposes.

## Model Architecture

For this project, we employed a Convolutional Neural Network (CNN) to classify the sign language images. CNNs are particularly effective for image classification tasks as they can automatically learn hierarchical features from the data.

## Model Performance

After training the CNN on the pre-processed data, we achieved the following performance:

- Training Accuracy: 88%
- Validation Accuracy: 95%

The model demonstrates promising results in accurately classifying the sign language images.

## Acknowledgments
This project is part of the Lab Assignment from the course "Natural Language Processing in Tensorflow" by deeplearning.ai from coursera.


## Conclusion

This project successfully tackled the multi-class classification problem of recognizing sign language images depicting the English alphabet using a Convolutional Neural Network. By pre-processing the data and training the CNN model, we achieved notable accuracy levels on the training and validation sets.

Feel free to explore the code in the repository and experiment with different models and hyperparameters to further enhance the performance. Happy coding!