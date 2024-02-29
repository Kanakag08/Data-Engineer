# Databricks notebook source
# sorting based on single column 

from pyspark.sql import SparkSession 
spark=SparkSession.builder.appName("Pratice").getOrCreate()
df_pyspark=spark.read.csv("/FileStore/tables/Department.csv",header=True,inferSchema=True)
df_pyspark.show()
df_pyspark.sort("salary").show()

# COMMAND ----------

# sorting based on descending order

df_pyspark.sort(df_pyspark["salary"].desc()).show()

# COMMAND ----------

# sorting based on ascending order

df_pyspark.sort(df_pyspark["salary"].asc()).show()

# COMMAND ----------

# sorting based on first column and then second columnns

df_pyspark.sort("salary","Name").show()

# COMMAND ----------

# order by 
df_pyspark.orderBy("salary").show()
