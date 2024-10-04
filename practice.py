# Import the required module
from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Simple PySpark Test") \
    .master("local[*]") \
    .getOrCreate()

# Create a simple DataFrame
data = [("John", 28), ("Anna", 23), ("Mike", 35)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
