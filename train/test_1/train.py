import numpy as np
import pandas as pd
import csv
import DenQuat_1
import tensorflow as tf
# import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

data =pd.read_csv("D:/THI/Global_EPICs_5/data/train/Book1.csv")

X = (data.iloc[:,1:6].values)
Y = (data.iloc[:,9:10].values)
# print(Y)
# print(X)

model = tf.keras.models.Sequential()  
model.add(tf.keras.layers.Dense(15, input_shape = (5,), activation='sigmoid'))
model.add(tf.keras.layers.Dense(20, activation ='tanh')) 
model.add(tf.keras.layers.Dense(1, activation = "linear"))   
print(model.summary())

model.compile(loss='mse', optimizer='Nadam')

model = load_model("D:/THI/Global_EPICs_5/train/test_1/New_18")
model.fit(X, Y, epochs=1000, batch_size=16, )
model.save("D:/THI/YSC/source/module_train")



