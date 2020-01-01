from pyspark import SparkConf, SparkContext

sc = SparkContext(master="local",appName="Spark Demo")
print(sc.textFile("/opt/citizens-del.json").first())
print(sc.textFile("/opt/citizens-del.json").count())