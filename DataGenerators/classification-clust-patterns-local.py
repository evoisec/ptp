import numpy as np
from matplotlib import pyplot as plt

from sklearn import linear_model, datasets
from sklearn import svm
from sklearn.datasets import dump_svmlight_file

from sklearn.datasets import make_moons, make_circles, make_classification

# Synthetic Data Generator producing datasets susceptible to Classification ML Models
# Generates synthetic data in the standard LIBSVM data format specifically intended for Machine Learning

# Supports the follwoing Data Science Workloads:
# LogisticRegression.py

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
random_state = int(Config['random.state'])
file=Config['file']


X, y = make_classification(n_samples=n_samples, n_features=n_features, n_redundant=0, n_informative=n_informative,
                           random_state=random_state, n_clusters_per_class=1)

print(X)
print(y)

dump_svmlight_file(X, y, file, zero_based=False)