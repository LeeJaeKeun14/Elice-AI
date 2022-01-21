# C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6\libnvvp
import tensorflow as tf
weights = tf.ones([3,3,1,1])
X = tf.ones([1,32,32,1])
Y = tf.nn.conv2d(X, weights, [1, 1, 1, 1], "VALID")
print(Y.shape)
print(tf.__version__)