import os
from pyspark.sql import SparkSession

# Set the HADOOP_USER_NAME to bypass Hadoop's user authentication
os.environ['HADOOP_USER_NAME'] = 'hadoop'

# Start a Spark session
spark = SparkSession.builder.appName('Practice').getOrCreate()

# Set log level to ERROR to reduce verbosity
spark.sparkContext.setLogLevel("ERROR")

# Read dataset with Spark (with header and inferred schema)
df_pyspark = spark.read.csv('practice.csv', header=True, inferSchema=True)

df_pyspark.show()
