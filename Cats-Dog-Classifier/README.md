# Cats and Dogs Image Recognition/Classification

This project is focused on developing an image recognition and classification system that can differentiate between images of cats and dogs. The dataset used for this project consists of 12,500 images of dogs and 12,500 images of cats.

## Dataset

The dataset can be obtained from the following link: [Kaggle Link](https://www.kaggle.com/competitions/dogs-vs-cats?rvi=1) 
Note: This notebook automatically fetches the dataset using the following [link](https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip)

The data is organized as follows:
- Training data:
  - 11,249 images of cats
  - 11,249 images of dogs

- Validation data:
  - 1,250 images of cats
  - 1,250 images of dogs

Note: Some images (e.g., 666.jpg, 11702.jpg) were found to be zero-length and were ignored during processing.

## Data Preprocessing

The training and validation data are processed using the `train_val_generators` function. It utilizes the `ImageDataGenerator` class from Keras to perform data augmentation and normalization. Each image is resized to (150, 150) pixels and scaled by dividing the pixel values by 255 to bring them into the range [0, 1].

## Model Architecture

The model for cats and dogs image classification is implemented using Keras. It consists of three convolutional layers, each followed by a max-pooling layer to downsample the feature maps. After flattening the output, there is a fully connected (dense) layer with 512 units and a ReLU activation function. The final layer has one unit with a sigmoid activation function to produce binary classification predictions.

## Model Compilation

The model is compiled using the RMSprop optimizer with a learning rate of 0.001. The binary crossentropy loss function is used, as this is a binary classification task. Additionally, the accuracy metric is tracked during training.

## Training and Validation

The training and validation data generators are created using the `train_val_generators` function mentioned earlier. The batch size for both generators is set to 50. The model is then trained on the training data and evaluated on the validation data.


## Contribution

Contributions to this project are welcome. If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.


**NOTE**: This project is part of my course of convolutions neural networks in tensorflow from coursera and deeplearning.ai