# TensorFlowNumberRegression
Simple tensorflow program to learn patterns in numbers.

ex.
"Enter 10 numbers that have a pattern"
x  y
1) 4
2) 8
3) 12
4) 16
5) 20
6) 24
7) 28
8) 32
9) 36
10) 40

The program passes the numbers as a numpy array to the neural network which learns the pattern.
Once the model finishes training, the user can input any number he or she would like to predict from the pattern.
The pattern here is obviously y = 4x, so that is what the model attempts to learn. 

The user now can enter any number for x and the model will predict the y value from the provided pattern
