"""
Gaussian Mixture Model (GMM).

"""
from __future__ import print_function

# $example on$
from pyspark.ml.clustering import GaussianMixture
# $example off$
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("GaussianMixture")\
        .getOrCreate()

    # $example on$
    # loads data
    # dataset = spark.read.format("libsvm").load("file:/opt/data/gmm-data.txt/gmm-data.txt")
    # dataset = spark.read.format("libsvm").load("file:/opt/data/gmm-data.txt")
    # dataset = spark.read.format("libsvm").load("file:/opt/data/testfile.txt")
    dataset = spark.read.format("libsvm").load("file:/root/PycharmProjects/ptp/Data/gmm.txt")

    dataset.show(100)

    gmm = GaussianMixture().setK(2).setSeed(538009335)
    model = gmm.fit(dataset)

    print("Gaussians shown as a DataFrame: ")
    model.gaussiansDF.show(truncate=False)
    # $example off$

    spark.stop()