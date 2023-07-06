import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

mnist_data = tf.keras.datasets.mnist
(X_train, Y_train) , (X_test, Y_test) = mnist_data.load_data()

print(X_train.shape, Y_train.shape)

X_train = tf.keras.utils.normalize(X_train)
X_test = tf.keras.utils.normalize(X_test)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=256, activation='relu'))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=10, activation='sigmoid'))
model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs = 20)

loss, accuracy = model.evaluate(X_test, Y_test)
print('Loss: ', loss)
print('Accuracy: ', accuracy)

#Loss:  0.13855908811092377
#Accuracy:  0.9783999919891357

for i in range(1, 7):
  img = cv.imread(f'img_{i}.png')[:, :, 0]
  img = np.invert(np.array([img]))
  prediction = model.predict(img)
  print("Digit: ", np.argmax(prediction))
  plt.imshow(img[0], cmap=plt.cm.binary)
  plt.show()

