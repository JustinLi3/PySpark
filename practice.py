from pyspark.sql import SparkSession

# Start a Spark session
spark = SparkSession.builder.appName('Practice').getOrCreate()

# Read dataset with Spark (with header and inferred schema)
df_pyspark = spark.read.csv('practice.csv', header=True, inferSchema=True)

df_pyspark.show()

spark.stop()

