import os
os.environ['PYSPARK_PYTHON'] = '/path/to/python'
from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("PySpark Test") \
    .getOrCreate()

# Create a simple DataFrame
data = [("John", 28), ("Jane", 33), ("Sam", 41)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
