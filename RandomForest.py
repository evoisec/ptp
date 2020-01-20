"""
Random Forest Regression.
"""
from __future__ import print_function

from pyspark import SparkContext
# $example on$
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils
# $example off$

if __name__ == "__main__":

    Config = {}

    f = open('RandomForest.cfg', 'r')
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
    maxDepth = int(Config['max.depth'])
    numTrees = int(Config['number.trees'])

    sc = SparkContext(appName="RandomForestRegression")
    # $example on$
    # Load and parse the data file into an RDD of LabeledPoint.
    # data = MLUtils.loadLibSVMFile(sc, "file:/root/PycharmProjects/ptp/Data/classification.txt")
    data = MLUtils.loadLibSVMFile(sc, file)
    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([trainRatio, testRatio])

    # Train a RandomForest model.
    #  Empty categoricalFeaturesInfo indicates all features are continuous.
    #  Note: Use larger numTrees in practice.
    #  Setting featureSubsetStrategy="auto" lets the algorithm choose.
    model = RandomForest.trainRegressor(trainingData, categoricalFeaturesInfo={},
                                        numTrees=numTrees, featureSubsetStrategy="auto",
                                        impurity='variance', maxDepth=maxDepth, maxBins=32)

    # Evaluate model on test instances and compute test error
    predictions = model.predict(testData.map(lambda x: x.features))
    labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
    testMSE = labelsAndPredictions.map(lambda lp: (lp[0] - lp[1]) * (lp[0] - lp[1])).sum() /\
        float(testData.count())
    print('Test Mean Squared Error = ' + str(testMSE))
    print('Learned regression forest model:')
    print(model.toDebugString())

    # Save and load model
    #model.save(sc, "target/tmp/myRandomForestRegressionModel")
    #sameModel = RandomForestModel.load(sc, "target/tmp/myRandomForestRegressionModel")
    # $example off$