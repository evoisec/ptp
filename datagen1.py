import numpy as np
from matplotlib import pyplot as plt

from sklearn import linear_model, datasets
from sklearn import svm
from sklearn.datasets import dump_svmlight_file

# Synthetic Data Generator producing datasets susceptible to Realistic Linear Regression
# Generates synthetic data in the standard LIBSVM data format specifically intended for Machine Learning

n_samples = 1000
n_outliers = 50


X, y, coef = datasets.make_regression(n_samples=n_samples, n_features=3,
                                      n_informative=1, noise=10,
                                      coef=True, random_state=0)

print(X)
print(y)
print(coef)

dump_svmlight_file(X, y, "/opt/data/syntds.txt")