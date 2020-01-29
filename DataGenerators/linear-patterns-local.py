import numpy as np
from matplotlib import pyplot as plt

from sklearn import linear_model, datasets
from sklearn import svm
from sklearn.datasets import dump_svmlight_file

# Synthetic Data Generator producing datasets susceptible to Realistic Linear Regression
# Generates synthetic data in the standard LIBSVM data format specifically intended for Machine Learning

# Supports the following Data Science Workloads:
# LinearRegression.py (and ANY other prediction type of ML model)

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

Config = {}

f = open('classification-clust-patterns-local.cfg', 'r')
line = f.readline()
while (line != ""):
    line = line.rstrip()
    x = line.split('=')
    print(x[0])
    print(x[1])
    Config[x[0]] = x[1]
    line = f.readline()

n_samples = int(Config['number.samples'])
n_features = int(Config['number.features'])
n_informative = int(Config['number.informative'])
noise = int(Config['noise'])
coef = str2bool(Config['coef'])
random_state = int(Config['random.state'])
file=Config['file']

X, y, coef = datasets.make_regression(n_samples=n_samples, n_features=n_features,
                                      n_informative=n_informative, noise=noise,
                                      coef=coef, random_state=random_state)

print(X)
print(y)
print(coef)

dump_svmlight_file(X, y, file, zero_based=False)