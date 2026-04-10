# /// script
# requires-python = ">=3.10,<3.12"
# dependencies = [
#     "pyspark",
#     "psutil"
# ]
# ///

from pyspark.sql import SparkSession, Row
# Force Spark to use uv's Python
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# Initialize Spark
spark = SparkSession.builder \
    .appName("RDD and SparkSQL Lab") \
    .master("local[*]") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

print("=== PART 1: RDD CREATION ===")

a = sc.parallelize(range(1, 100))
print("Partitions:", a.getNumPartitions())
print("Data:", a.take(10))  # safer than collect

b = a.repartition(11)
print("Repartitioned:", b.getNumPartitions())

c = b.coalesce(5)
print("Coalesced:", c.getNumPartitions())


print("\n=== PART 2: TEXT FILE PROCESSING ===")

text_rdd = sc.textFile("sample.txt")

words_rdd = text_rdd.flatMap(lambda line: line.split(" "))
filtered_words = words_rdd.filter(lambda x: x != "")
word_pairs = filtered_words.map(lambda word: (word, 1))
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

print("Word Counts:", word_counts.collect())


print("\n=== PART 3: SPARK SQL ===")

people_rdd = sc.parallelize([
    Row(name="Alice", age=25, city="Pune"),
    Row(name="Bob", age=30, city="Mumbai"),
    Row(name="Charlie", age=35, city="Pune"),
    Row(name="David", age=28, city="Delhi")
])

people_df = spark.createDataFrame(people_rdd)
people_df.createOrReplaceTempView("people")

print("All Data:")
spark.sql("SELECT * FROM people").show()

print("Age > 28:")
spark.sql("SELECT * FROM people WHERE age > 28").show()

print("Grouped by City:")
spark.sql("SELECT city, COUNT(*) AS total FROM people GROUP BY city").show()

print("Sorted by Age Desc:")
spark.sql("SELECT * FROM people ORDER BY age DESC").show()

spark.stop()