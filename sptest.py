#from pyspark import SparkConf, SparkContext
import sys

from pyspark.sql import SparkSession
#from pyspark.sql.functions import col, asc
from pyspark.sql import functions as F
from pyspark.sql.types import *

print(sys.version)
print(sys.version_info)
#sys.exit(0)

spark = SparkSession.builder.appName("CLIENT-ETL-Pipeline").getOrCreate()

df1 = spark.read.csv("file:/root/PycharmProjects/ptp/table1.csv", header=True, inferSchema=True)
#df2 = spark.read.csv("/opt/projects/1/table2.csv", header=True)

df1.show()
df1.printSchema()

df4 = df1.createOrReplaceTempView("Table1")
df5 = spark.sql("Select * from Table1 where c1=12")
df5.show()

df5.write.mode("overwrite").csv("file:/root/PycharmProjects/ptp/table1-deriv.csv", header=True)

spark.stop()