import tensorflow as tf
import numpy as np
from tensorflow import keras

# Data
xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], dtype=float)
ys = np.array([],dtype=float)
print("Enter 10 numbers that have a pattern\n")
for i in range(10):
    number = float(input("Enter number " + str(i + 1) + ": "))
    ys = np.append(ys, number)


# Model
model = tf.keras.Sequential([keras.layers.Dense(units=4,input_shape=[1]),
                             keras.layers.Dense(units=1)])

# Build Model
model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.Adam(lr=0.01),
              metrics=["mae"])

# Train Model
model.fit(xs,ys,epochs=300)

print("Type a number you would like to predict from your pattern: ")
print('Type "end" to quit')
flag = True
while flag:
    user_number = input("Enter a number: ")
    if (user_number == "end"):
        print("Program terminated.")
        flag = False
    else:
        input_array = np.array([])
        input_array = np.insert(input_array, 0, user_number)
        print(model.predict(input_array))
