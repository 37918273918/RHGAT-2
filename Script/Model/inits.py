import tensorflow as tf

import numpy as np
# import tensorflow.compat.v1 as tf.compat.v1

def weight_variable_glorot(input_dim, output_dim, name=""):
    """Create a weight variable with Glorot & Bengio (AISTATS 2010)
    initialization.
    """
    init_range = np.sqrt(6.0 / (input_dim + output_dim))
    initial = tf.compat.v1.random_uniform([input_dim, output_dim], minval=-init_range,
                                maxval=init_range, dtype=tf.compat.v1.float32)
    return tf.compat.v1.Variable(initial, name=name)


def zeros(input_dim, output_dim, name=None):
    """All zeros."""
    initial = tf.compat.v1.zeros((input_dim, output_dim), dtype=tf.compat.v1.float32)
    return tf.compat.v1.Variable(initial, name=name)


def ones(input_dim, output_dim, name=None):
    """All zeros."""
    initial = tf.compat.v1.ones((input_dim, output_dim), dtype=tf.compat.v1.float32)
    return tf.compat.v1.Variable(initial, name=name)