# For learning about tensorflow

import tensorflow as tf
print("TensorFlow version:", tf.__version__)

from tensorflow.python.keras.layers import Dense, Flatten, Conv2D
from tensorflow.python.keras import Model

# Load and prepare the MNIST dataset

mnist = tf.keras.datasets.mnist

# Splits loaded dataset into train and test set
(x_trian, y_train), (x_test, y_test) = mnist.load_data()

# Normalizes the pixel values of the images to be between 0 and 1
x_trian, x_test = x_trian / 255.0, x_test / 255.0

# Add a channels dimension
# Channels dimension in an image represents the number of color channels in the image
# Converting the shape from (28, 28) to (28, 28, 1)
# And then converts the data type of the images to "float32".
x_trian = x_trian[..., tf.newaxis].astype("float32")
x_test = x_test[..., tf.newaxis].astype("float32")