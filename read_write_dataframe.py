from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read write dataframe").getOrCreate()

spark.sparkContext.setLogLevel("OFF")

# lee dataframe
input_path = "./input/data.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True, sep=",")

# imprime dataframe
df.show()
df.printSchema()

# escribe dataframe
output_path = "./output/data.parquet"
df.write.mode("overwrite").parquet(output_path)

spark.stop()
