"""
Decision Tree Regression.
"""
from __future__ import print_function

from pyspark import SparkContext
# $example on$
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
# $example off$

if __name__ == "__main__":

    sc = SparkContext(appName="PythonDecisionTreeRegression")

    # $example on$
    # Load and parse the data file into an RDD of LabeledPoint.
    data = MLUtils.loadLibSVMFile(sc, 'file:/root/PycharmProjects/ptp/Data/linear-regression.txt')
    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Train a DecisionTree model.
    #  Empty categoricalFeaturesInfo indicates all features are continuous.
    model = DecisionTree.trainRegressor(trainingData, categoricalFeaturesInfo={},
                                        impurity='variance', maxDepth=5, maxBins=32)

    # Evaluate model on test instances and compute test error
    predictions = model.predict(testData.map(lambda x: x.features))
    labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
    testMSE = labelsAndPredictions.map(lambda lp: (lp[0] - lp[1]) * (lp[0] - lp[1])).sum() /\
        float(testData.count())
    print('Test Mean Squared Error = ' + str(testMSE))
    print('Learned regression tree model:')
    print(model.toDebugString())

    # Save and load model
    #model.save(sc, "target/tmp/myDecisionTreeRegressionModel")
    #sameModel = DecisionTreeModel.load(sc, "target/tmp/myDecisionTreeRegressionModel")
    # $example off$