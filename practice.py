from pyspark.sql import SparkSession
# Initialize a Spark session
spark = SparkSession.builder \
    .appName("PySpark Test") \
    .getOrCreate()
# Stop the Spark session
spark.stop()
