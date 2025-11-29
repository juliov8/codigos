# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists workspace.default.usuarios;
# MAGIC create table if not exists workspace.default.usuarios (codigo int, nombre string, dni string);

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType(
    [
        StructField("codigo", IntegerType(), True),
        StructField("nombre", StringType(), True),
        StructField("dni", StringType(), True),
    ]
)

df = (
    spark.readStream.format("cloudFiles")
    .option(
        "cloudFiles.schemaLocation",
        "/Volumes/workspace/default/volume_usuarios/usuarios/schema/",
    )
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .schema(schema)
    .load("sftp://<user>@<server>:22/<path>")
    .writeStream.format("delta")
    .option(
        "checkpointLocation",
        "/Volumes/workspace/default/volume_usuarios/usuarios/checkpoint/",
    )
    .trigger(once=True)
    .table("workspace.default.usuarios")
)
df.awaitTermination()

# COMMAND ----------

# echo -e "codigo,nombre,dni\n100,Javier,33562145\n101,Jaime,04142575" > usuarios1.csv

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.usuarios
