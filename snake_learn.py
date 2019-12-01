import tensorflow as tf
import random
mnist = tf.keras.datasets.mnist

def lernen(l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9, l_10, l_12, l_13, l_14, l_15, l_16):
 steuerung = (-1,0), (1,0), (0,1), (0,-1)
 ki_steuerung = random.choice(steuerung)
 return ki_steuerung
