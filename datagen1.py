import numpy as np
from matplotlib import pyplot as plt

from sklearn import linear_model, datasets


n_samples = 1000
n_outliers = 50


X, y, coef = datasets.make_regression(n_samples=n_samples, n_features=3,
                                      n_informative=1, noise=10,
                                      coef=True, random_state=0)

print(X)
print(y)
print(coef)