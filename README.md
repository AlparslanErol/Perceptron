# Perceptron

### Summer Term 2019/

## 1 Perceptron

```
∑ y
```
x 0 w (^0) θ
x 1 w 1
... ...
xn wn
Inputvalues Weights
net Activation(discrete)function
Figure 1: Perceptron with discreta activation function.
A perceptron consists of the following:

- Input vectorx=(x 0 x 1 ... xn)T,
- Weight vectorw=(w 0 w 1 ... wn)T,
- Biasθ,
- Activation functionf.

### 1.1 Calculating output value

Thenetvalue is the scalar product of the weight vector and input vector minus the bias:

net=wTx−θ=w 0 ·x 0 +w 1 ·x 1 +···+wn·xn−θ
The output value is:

```
y=f(net) =
```
#### {

```
1 ifnet≥ 0
0 otherwise
```

## 2 Perceptron - interpretacja geometryczna

A perceptron creates a hyperplane, which divides the decision space into two parts. The
weight vector is its normal vector. The output value is equal to 1 if the input is on the
same side of the hyperplane as the weight vector. Below is the hyperplane equation for a
perceptron with the weight vector (w 0 ,w 1 ,...,wn) and the biasθ:
w 0 x 0 +w 1 x 1 +···+wnxn−θ= 0

## 3 Delta rule

Weights and biases are modified according to the following rule:

w′=w+η(d−y)x
θ′=θ−η(d−y)
Where:

- w′is the new weight vector;
- wis the old weight vector;
- θ′is the new bias;
- θis the old bias;
- ηis the learning rate (usually between 0 and 1);
- dis the expected output;
- yis the output;
- xis the input vector.

## 4 Perceptron learning algorithm

The input is the training set consisting of input vectorsxiexpected outputsdi:
{(x 0 ,d 0 ),(x 1 ,d 1 ),...,(xn,dn)}

1. Pick learning rateηand pick random initial weights.
2. For each training set vectorxi:
    (a) Calculate outputy.
(b) Update weights and bias according to delta rule.
3. Calculate iteration error (number of erroneaus outputs):
    E=

```
∑n
i=
```
```
|di−yi|
```
4. Go back to step 2, or end training whenEis below a given threshold (E < Emax),
    or after a given number of iterations.


## Questions

Question 1.
Given the following perceptron with the weight vectorw= (2,− 1 , 4 ,1), biasθ= 3, and a
unipolar discrete activation function, calculate the output value for the following inputs.

- x= (7,− 2 ,− 5 ,4) • x= (2, 0 , 2 ,8)

(^23)
− 1
4
1
Question 2.
What is the hyperplane equation of the perceptron in Question 1.
Question 3.
Design a perceptron to implement the following logical functions: AND, OR, NAND,
NOR, XOR.
Question 4.
How will the weights and bias of the percptron from Q1 be modified by the delta rule
given the following inputs (η= 0.5).

- x= (7,− 2 ,− 5 ,4),d= 1 • x= (2, 0 , 2 ,8),d= 0
- x= (5, 8 ,− 1 ,−2),d= 1 • x= (3, 1 , 9 ,−3),d= 0
- x= (0, 1 , 2 ,1),d= 0


## Mini-project: Perceptron

The training set inperceptron.datacontains theIrisdataset limited toIris-setosa
andIris-versicolor. perceptron.test.datacontains the test set. Implement the
perceptron and train it to classify the two species. Test with the test set and output the
accuracy.
The program should have the following capabilities:

- Loading any dataset in csv format, where the last column is the class. The number
    of weight should be adjusted for the dataset.
- Picking the learning rate.
- Simple UI to manually input vectors to classify.
Submit by: 3.04.


