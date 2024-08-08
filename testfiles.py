import tensorflow as tf
print("TensorFlow version:", tf.__version__)

from tensorflow.python.keras.layers import Dense, Flatten, Conv2D
from tensorflow.python.keras import Model

# Load and prepare the MNIST dataset

mnist = tf.keras.datasets.mnist
print(mnist)