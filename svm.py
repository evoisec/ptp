"""
Support Vector Machine.

Binary Classification

"""

from pyspark.sql import SparkSession
from pyspark.ml.classification import LinearSVC

Config = {}

f = open('svm.cfg', 'r')
line = f.readline()
while (line != ""):
    line = line.rstrip()
    x = line.split('=')
    print(x[0])
    print(x[1])
    Config[x[0]] = x[1]
    line = f.readline()

file = Config['file']
trainRatio = float(Config['train.ratio'])
testRatio = float(Config['test.ratio'])
maxIter = int(Config['max.iterations'])
partitions = int(Config['partitions'])

spark = SparkSession.builder.appName("SVM").getOrCreate()

if (partitions == 0):
    training = spark.read.format("libsvm").load(file)

if (partitions != 0):
    # Load training data
    training = spark.read.format("libsvm").load(file).repartition(3)

lsvc = LinearSVC(maxIter=maxIter, regParam=0.1)

# Fit the model
lsvcModel = lsvc.fit(training)

# Print the coefficients and intercept for linear SVC
print("Coefficients: " + str(lsvcModel.coefficients))
print("Intercept: " + str(lsvcModel.intercept))