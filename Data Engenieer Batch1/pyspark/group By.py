# Databricks notebook source
from pyspark.sql import SparkSession
spark =SparkSession.builder.appName("Practice").getOrCreate()
df_pyspark= spark.read.csv("/FileStore/tables/Department.csv",header=True,inferSchema=True)
df_pyspark.show()
# Group By function used 
df_pyspark.groupBy("Departments").sum("salary").show()


# COMMAND ----------

# group by with aggregate function minimum
df_pyspark.groupBy("Departments").min("salary").show()



# COMMAND ----------

# group by with aggregate maximum function 
df_pyspark.groupBy("Departments").max("salary").show()

# COMMAND ----------

# group by with aggregate Average function 
df_pyspark.groupBy("Departments").avg("salary").show()

# COMMAND ----------

# group by with aggregate mean function 
df_pyspark.groupBy("Departments").mean("salary").show()

# COMMAND ----------

# group by with aggregate count function 
df_pyspark.groupBy("Departments").count().show()

# COMMAND ----------

# group by with aggregate Sum function 
df_pyspark.groupBy("Departments").sum("salary").show()

# COMMAND ----------

# group by with aggregate Agg function 
df_pyspark.groupBy("Departments").agg({"salary": "sum"}).show()

# COMMAND ----------

# group by with aggregate pivot function 
df_pyspark.groupBy("Departments").pivot("Name").sum("salary").show()
