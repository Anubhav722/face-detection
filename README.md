# face-detection


## OPEN CV

### CASCADES

Series of filters that will be applied to detect the face.

### REFERENCES:

HAAR LIKE FEATURES AND VIOLA-JONES ALGORITHM (RESEARH PAPER CAN BE FOUND HERE)
https://www.superdatascience.com/computer-vision/

GITHUB REPO CONTAINING MORE HAAR LIKE FEATURES.
https://github.com/opencv/opencv/tree/master/data/haarcascades


## SSD: SINGLE SHOT MULTIBOX DETECTOR



### REFERENCES

RESEARCH PAPER: https://arxiv.org/pdf/1512.02325.pdf


GEOFFREY HINTON: FATHER OF DEEP LEARNING :)
EXPLAINS THE NEURAL NETWORKS https://www.youtube.com/watch?v=cbeTc-Urqak&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9


### ADDITIONAL READING RESOURCES

STANDARDIZATION AND NORMALIZATION
http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf

ACTIVATION FUNCTIONS:
http://proceedings.mlr.press/v15/glorot11a/glorot11a.pdf

medium article explaining activation functions: https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0
analytics vidhya link: https://www.analyticsvidhya.com/blog/2017/10/fundamentals-deep-learning-activation-functions-when-to-use-them/
wikipedia article: https://en.wikipedia.org/wiki/Activation_function

COST FUNCTIONS:
https://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications

GRADIENT DESCENT:
http://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html

STOCHASTIC GRADIENT DESCENT:
https://iamtrask.github.io/2015/07/27/python-network-part2/


GREAT ARTICLE TO UNDERSTAND THE NEURAL NETWORKS IN PYTHON:
https://iamtrask.github.io/2015/07/12/basic-python-network/

DIVING DEEPER INTO MATHEMATICS FOR DEEP LEARNING (also good to understand back propagation and grad descent)- A book by Michael Nielson
http://neuralnetworksanddeeplearning.com/chap2.html

### TRAINING THE ANN (ARTIFICIAL NEURAL NETWORK) WITH STOCHASTIC GRADIENT DESCENT)

Step 1: Randomly initialize the weights to small numbers close to 0 (but not 0).

Step 2: Input the first observation of your dataset in the input layer, eadch feature in one input node.

Step 3: Forward-Propagation: from left to right, the neurons are activated in a way that the impact of each neuron activation is limited by weights. Propagate the activations until getting the predicted result y.

Step 4: Compare the predicted result to the actual result. Measure the generated error.

Step 5: Back Propagation: from right to left, the error is back propagated. Update the weights acc. to how much they are responsible for the error. The learning rate decides by how much we update the weights.

Step 6: Repeat Steps 1 to 5 and update the weights after each observation (Reinforcement Learning). Or: Repeat Steps 1 to 5 but update the weights only after a batch of observations (Batch Learning).

Step 7: When the whole training set is passed through the ANN, that makes an epoch. Redo more epochs.


### CONVOLUTIONAL NEURAL NETWORKS

Understanding them: http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf

Introduction to convolutional neural network(for mathematics): https://cs.nju.edu.cn/wujx/paper/CNN.pdf

ReLU LAYER
Why is a non-linear activation function is essential at the filter output of all intermediate layers.
Understanding Convolutional Neural Networks with A Mathematical Model: https://arxiv.org/pdf/1609.04112v2.pdf

POOLING: https://www.ais.uni-bonn.de/papers/icann2010_maxpool.pdf

Visualization of Convolutional neural network: http://scs.ryerson.ca/~aharley/vis/conv/flat.html

STEPS INVOLVED IN CNN:
1. Convolution
1b. ReLu Layer (Removing Linearity)
2. Pooling
3. Flattening 
4. Full Connection

DEEP LEARNING BLOGS: https://adeshpande3.github.io/adeshpande3.github.io/The-9-Deep-Learning-Papers-You-Need-To-Know-About.html
