# TensorFlowNumberRegression
Simple tensorflow program to learn patterns in numbers.


Example run:

"Enter 10 numbers that have a pattern"
- 4
- 8
- 12
- 16
- 20
- 24
- 28
- 32
- 36
- 40

The program passes the numbers as a numpy array to the neural network which learns the pattern.
Once the model finishes training, the user can input any number he or she would like to predict from the pattern.
The pattern here is obviously y = 4x, so that is what the model attempts to learn. 

The user now can enter any number for x and the model will predict the y value from the provided pattern
