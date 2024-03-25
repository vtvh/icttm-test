import os
from pyspark.sql import SparkSession

# You can use the following to set the environment variables in the notebook if you don't set manually access key, secret key and endpoint in minio
os.environ['OBJ_STORAGE_ACCESS_KEY'] = 'XpSkdzaL5NsSIe4YgHDg'
os.environ['OBJ_STORAGE_SECRET_KEY'] = 'jNiQdM05jn4cZIA6fBuWIjGD0UjfhsiKS3RpPL9W'
os.environ['OBJ_STORAGE_ENDPOINT'] = 'http://localhost:9000'

# Define S3 storage
obj_storage_access_key = os.getenv('OBJ_STORAGE_ACCESS_KEY')
obj_storage_secret_key = os.getenv('OBJ_STORAGE_SECRET_KEY')
obj_storage_endpoint = os.getenv('OBJ_STORAGE_ENDPOINT', 'http://localhost:9000')

path_1 = "s3a://data/data-raw/data.json"
path_2 = "s3a://data/data-raw/data2.json"
path_3 = "s3a://data/data-raw/data3.json"

# You need to more configuration if you want to use minio as object storage
# (hint: maybe you can using .config() method to set the configuration
# if you want using spark to read/write data from/to minio)

# Add the following configuration to read/write data from/to minio
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.hadoop.fs.s3a.endpoint", obj_storage_endpoint) \
    .config("spark.hadoop.fs.s3a.access.key", obj_storage_access_key) \
    .config("spark.hadoop.fs.s3a.secret.key", obj_storage_secret_key) \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", True) \
    .getOrCreate()

# Read the JSON files
df1 = spark.read.json(path_1)
df2 = spark.read.json(path_2)
df3 = spark.read.json(path_3)

# Merge the DataFrames
df = df1.union(df2).union(df3)

# Write the result to a single JSON file
df.coalesce(1).write.json('result.json')
