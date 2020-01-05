#from pyspark import SparkConf, SparkContext
import sys

#from pyspark.sql.functions import col, asc
from pyspark.sql import functions as F
from pyspark.sql.types import *

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
from pyspark.ml import Pipeline
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

############################################################################################
#
# uses synthetically enlarged Employee dataset (simulates Citizens welfare and income) from here
# http://archive.ics.uci.edu/ml/datasets/Adult - this is the original/staring dataset which is then enlarged further
# to stress and measure the performance of Data Science Workloads
#
############################################################################################

print(sys.version)
print(sys.version_info)
#sys.exit(0)

spark = SparkSession.builder.appName("LogisticRegression").getOrCreate()

schema = StructType([
    StructField("age", IntegerType(), True),
    StructField("workclass", StringType(), True),
    StructField("fnlwgt", IntegerType(), True),
    StructField("education", StringType(), True),
    StructField("education-num", IntegerType(), True),
    StructField("marital-status", StringType(), True),
    StructField("occupation", StringType(), True),
    StructField("relationship", StringType(), True),
    StructField("race", StringType(), True),
    StructField("sex", StringType(), True),
    StructField("capital-gain", IntegerType(), True),
    StructField("capital-loss", IntegerType(), True),
    StructField("hours-per-week", IntegerType(), True),
    StructField("native-country", StringType(), True),
    StructField("salary", StringType(), True)
])

train_df = spark.read.csv('train.csv', header=False, schema=schema)
test_df = spark.read.csv('test.csv', header=False, schema=schema)

categorical_variables = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
indexers = [StringIndexer(inputCol=column, outputCol=column+"-index") for column in categorical_variables]
encoder = OneHotEncoderEstimator(
    inputCols=[indexer.getOutputCol() for indexer in indexers],
    outputCols=["{0}-encoded".format(indexer.getOutputCol()) for indexer in indexers]
)
assembler = VectorAssembler(
    inputCols=encoder.getOutputCols(),
    outputCol="categorical-features"
)
pipeline = Pipeline(stages=indexers + [encoder, assembler])
train_df = pipeline.fit(train_df).transform(train_df)
test_df = pipeline.fit(test_df).transform(test_df)



spark.stop()