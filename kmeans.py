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

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("KMeans")\
        .getOrCreate()

    # $example on$
    # Loads data.
    dataset = spark.read.format("libsvm").load("kmeans_data.txt")

    # Trains a k-means model.
    kmeans = KMeans().setK(2).setSeed(1)
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