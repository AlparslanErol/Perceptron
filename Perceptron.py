import numpy as np

import pandas as pd


class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs)
        self.bias = 0

    def predict(self, inputs):
        sum = np.dot(inputs, self.weights) + self.bias  # dot product matrx multiplication bias add
        if sum > 0:
            activation = 1
        else:
            activation = 0
        return activation

    def train(self, train_data, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(train_data, labels):
                prediction = self.predict(inputs)
                self.bias += self.learning_rate * (label - prediction)
                self.weights += self.learning_rate * (label - prediction) * inputs
                

                #leru type of sigmoid function.
                #to predict either 1/0.



# read and  modify data
data = pd.read_csv(r'C:\Users\ALPARSLAN\Desktop\perceptron.csv')
data = data[:]
data[4] = np.where(data.iloc[:, -1] == 'Iris-setosa', 0, 1)
train_input = data.iloc[:, 0:4].values
labels = data.iloc[:, -1].values
# activate the perceptron
perceptron = Perceptron(4)
# train the perceptron
perceptron.train(train_input, labels)

# test the perceptron
test_data = pd.read_csv(r'C:\Users\ALPARSLAN\Desktop\perceptron.test.csv')

test_data = test_data[:]
test_data[4] = np.where(test_data.iloc[:, -1] == 'Iris-setosa', 0, 1)

test_data_input = test_data.iloc[:, 0:4].values

# count number of total missclassified
miss_classified = 0
miss_classified_list = []
test_data.iat[0, 5]
for i in range(0, test_data_input.shape[0]):
    test_prediction1 = perceptron.predict(test_data_input[i])
    miss_classified_list.append(test_prediction1)
    if test_prediction1 != test_data.iat[i, 5]:
        miss_classified = miss_classified + 1
accuracy = (1 - (miss_classified / test_data.shape[0])) * 100
print("Accuracy: ", accuracy)  # Accuracy is here giving 100%, with the test data as provided in Assignment.

# take a input from user (UI input of Data)
listFromUser = [0, 0, 0, 0]
for i in range(0, 4):
    userData = float(input('enter i th value :  '))
    listFromUser[i] = userData
print('the data you have Provided is\n=> ', listFromUser)

output_prediction = perceptron.predict(listFromUser)
if output_prediction == 0:
    print('According to the input you have given, : Iris-setosa')
elif output_prediction == 1:
    print('According to the input you have given : Iris-versicolor')
