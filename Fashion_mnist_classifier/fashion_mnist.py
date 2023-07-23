import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

fashion_data = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (val_images, val_labels) = fashion_data.load_data()

# Play with indexes
index = 0
np.set_printoptions(linewidth = 320)
print(f"Label:  {training_labels[index]} ")
print(f"\nImage Pixel (Array)\n {training_images[index]}")

plt.imshow(training_images[index])

"""### Normalize the data"""

training_images = training_images / 255.0
val_images = val_images / 255.0

"""## Callback Implementation for Early Stopping"""

DESIRED_ACCURACY = 0.995

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epochs, logs={}) :
        if(logs.get('acc') is not None and logs.get('acc') >= DESIRED_ACCURACY) :
            print('\nReached 99.9% accuracy so cancelling training!')
            self.model.stop_training = True

"""## Convolutional Model


"""

def convolutional_model():
  model = tf.keras.models.Sequential(
      [
          tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
          tf.keras.layers.MaxPooling2D(2, 2),
          tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
          tf.keras.layers.MaxPooling2D(2, 2),

          tf.keras.layers.Flatten(),
          tf.keras.layers.Dense(512, activation = 'relu'),
          tf.keras.layers.Dense(10, activation = 'softmax')
      ]
  )
  model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['Accuracy'])
  return model

model = convolutional_model()
model_params = model.count_params()

assert model_params < 1000000, (
    f'Your model has {model_params:,} params. For successful grading, please keep it '
    f'under 1,000,000 by reducing the number of units in your Conv2D and/or Dense layers.'
)

callbacks = myCallback()

history = model.fit(training_images, training_labels, epochs = 20, callbacks=[callbacks])

print(model.evaluate(val_images, val_labels))
predictions = model.predict(val_images)
print(predictions[0])
print(val_labels[0])

