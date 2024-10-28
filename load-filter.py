from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unbase64

# initialize Spark session
spark = SparkSession.builder \
    .appName("Load Base64 Encoded File") \
    .getOrCreate()

# path to the Base64-encoded text file in HDFS
hdfs_path = "hdfs://///user/kroppl/bloom-filter/bloom_filter_encoded.txt" 

# load the Base64-encoded text file into a DataFrame
df = spark.read.text(hdfs_path)

# decode the Base64 content
decoded_df = df.select(unbase64(col("value")).cast("string").alias("decoded_value"))

# show the decoded content
decoded_df.show(truncate=False)

# stop the Spark session
spark.stop()
