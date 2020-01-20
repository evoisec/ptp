from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression

Config = {}

f = open('LinearRegression.cfg', 'r')
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

spark = SparkSession.builder.appName("LinearRegression").getOrCreate()

# Load training data
#training = spark.read.format("libsvm").option("numFeatures", "3").load("file:/root/PycharmProjects/ptp/Data/regression-2.txt")
training = spark.read.format("libsvm").load(file)
# .load("file:/opt/data/sample_linear_regression_data.txt")

#training.show()
#exit(0)

lr = LinearRegression(maxIter=maxIter, regParam=0.3, elasticNetParam=0.8)

# Fit the model
lrModel = lr.fit(training)

# Print the coefficients and intercept for linear regression
print("Coefficients: %s" % str(lrModel.coefficients))
print("Intercept: %s" % str(lrModel.intercept))

# Summarize the model over the training set and print out some metrics
trainingSummary = lrModel.summary
print("numIterations: %d" % trainingSummary.totalIterations)
print("objectiveHistory: %s" % str(trainingSummary.objectiveHistory))
trainingSummary.residuals.show()
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)