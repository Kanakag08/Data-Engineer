# Databricks notebook source
# dropping rows based on null value 

from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("pratice").getOrCreate()
df_pyspark=spark.read.csv("/FileStore/tables/test1.csv",header=True,inferSchema=True)
df_pyspark.show()
df_pyspark.na.drop().show()

# COMMAND ----------

# dropping rows based on parameter how 
df_pyspark.na.drop(how="all").show()

# COMMAND ----------

# dropping rows based on parameter thresh
df_pyspark.na.drop(how="any",thresh=2).show()

# COMMAND ----------

# dropping rows based on parameter subset
df_pyspark.na.drop(how="any",subset=["Salary"]).show()

# COMMAND ----------

# Fillinh Missing Value 
df_pyspark.na.fill('Missing Values').show()
inputdf_pyspark.na.fill(0).show()
