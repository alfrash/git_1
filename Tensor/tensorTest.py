import numpy as np
import tensorflow as tf
from tensorflow.python.client import session

opt = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.9)
var = tf.Variable(1.0)
val0 = var.value()
loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1
# First step is `- learning_rate * grad`
step_count = opt.minimize(loss, [var]).numpy()
val1 = var.value()
print((val0 - val1).numpy())

# On later steps, step-size increases because of momentum
step_count = opt.minimize(loss, [var]).numpy()
val2 = var.value()
print((val1 - val2).numpy())
