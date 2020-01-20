"""
k-means clustering.
requires NumPy (http://www.numpy.org/).
"""
from __future__ import print_function

# $example on$
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
# $example off$

from pyspark.sql import SparkSession

Config = {}

f = open('kmeans.cfg', 'r')
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
clusters = int(Config['cluster.centers'])

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("KMeans")\
        .getOrCreate()

    # $example on$
    # Loads data.
    dataset = spark.read.format("libsvm").load(file)

    # Trains a k-means model.
    kmeans = KMeans().setK(clusters).setSeed(1)
    model = kmeans.fit(dataset)

    # Make predictions
    predictions = model.transform(dataset)

    # Evaluate clustering by computing Silhouette score
    evaluator = ClusteringEvaluator()

    silhouette = evaluator.evaluate(predictions)
    print("Silhouette with squared euclidean distance = " + str(silhouette))

    # Shows the result.
    centers = model.clusterCenters()
    print("Cluster Centers: ")
    for center in centers:
        print(center)
    # $example off$

    spark.stop()