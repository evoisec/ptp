import numpy as np
from matplotlib import pyplot as plt

from sklearn import linear_model, datasets
from sklearn import svm
from sklearn.datasets import dump_svmlight_file

from sklearn.datasets import make_moons, make_circles, make_classification

# Synthetic Data Generator producing datasets susceptible to Realistic Linear Regression
# Generates synthetic data in the standard LIBSVM data format specifically intended for Machine Learning

# Supports the follwoing Data Science Workloads:
# LinearRegression.py

n_samples = 1000

X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1)

print(X)
print(y)

dump_svmlight_file(X, y, "/opt/data/classification.txt", zero_based=False)