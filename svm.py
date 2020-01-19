"""
Support Vector Machine.

Binary Classification

"""

from pyspark.sql import SparkSession
from pyspark.ml.classification import LinearSVC

spark = SparkSession.builder.appName("SVM").getOrCreate()

# Load training data
training = spark.read.format("libsvm").load("file:/root/PycharmProjects/ptp/Data/classification-2.txt")

lsvc = LinearSVC(maxIter=10, regParam=0.1)

# Fit the model
lsvcModel = lsvc.fit(training)

# Print the coefficients and intercept for linear SVC
print("Coefficients: " + str(lsvcModel.coefficients))
print("Intercept: " + str(lsvcModel.intercept))