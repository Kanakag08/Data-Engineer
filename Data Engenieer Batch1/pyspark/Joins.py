# Databricks notebook source
# joins 

from pyspark.sql import SparkSession
spark= SparkSession.builder.appName("Pratice").getOrCreate()
df_pyspark=spark.read.csv("/FileStore/tables/empDF.csv",header=True,inferSchema=True)
df_pyspark.show()
df_spark1=spark.read.csv("/FileStore/tables/deptDF.csv",header=True,inferSchema=True)
df_spark1.show()

# COMMAND ----------

# inner Join 

df_pyspark.join(df_spark1,df_pyspark.emp_dept_id==df_spark1.dept_id,"inner").show()

# COMMAND ----------

# outer join 

df_pyspark.join(df_spark1,df_pyspark.emp_dept_id==df_spark1.dept_id,"outer").show()

# COMMAND ----------

# Left Join 

df_pyspark.join(df_spark1,df_pyspark.emp_dept_id==df_spark1.dept_id,"left").show()

# COMMAND ----------

# Right Join 

df_pyspark.join(df_spark1,df_pyspark.emp_dept_id==df_spark1.dept_id,"right").show()
