from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split  # Importing the necessary functions

# Initialize SparkSession
spark = SparkSession.builder.appName("WordCounter").getOrCreate()

# Read text file
df_text = spark.read.text('PySpark.txt')

# Split each line into words
df_words = df_text.select(explode(split(df_text.value, "\s+")).alias("word"))

# Filter out any empty words (optional)
df_words_filtered = df_words.filter(df_words.word != '')

# Group by words and count occurrences
word_count = df_words_filtered.groupBy("word").count().orderBy("count", ascending=False)

# Show the result
word_count.show(truncate=False)
