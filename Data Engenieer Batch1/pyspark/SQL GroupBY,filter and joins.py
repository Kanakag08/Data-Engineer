# Databricks notebook source
# aggregate count fuction with group by

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Pratice").getOrCreate()
df=spark.read.option("header",True).csv("/FileStore/tables/Zipcode.csv")
df.printSchema()
df.show()
df.groupBy("State").count().show()

# COMMAND ----------

# aggregate Minimum fuction with group by
df.groupBy("Zipcode").min().show()

# COMMAND ----------

# aggregate Maximum fuction with group by
df.groupBy("Zipcode").max().show()

# COMMAND ----------

# filter 

df.select("country","city","zipcode","state") \
  .where("state == 'AZ'") \
  .show(5)

# COMMAND ----------

# Joins 
from pyspark.sql import SparkSession

emp = [(1,"Smith",-1,"2018","10","M",3000), \
    (2,"Rose",1,"2010","20","M",4000), \
    (3,"Williams",1,"2010","10","M",1000), \
    (4,"Jones",2,"2005","10","F",2000), \
    (5,"Brown",2,"2010","40","",-1), \
      (6,"Brown",2,"2010","50","",-1) \
  ]
empColumns = ["emp_id","name","superior_emp_id","year_joined", \
       "emp_dept_id","gender","salary"]

empDF = spark.createDataFrame(data=emp, schema = empColumns)
empDF.printSchema()
empDF.show(truncate=False)

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

# COMMAND ----------

# Inner Joins 

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"inner") \
     .show(truncate=False)

# COMMAND ----------

 # Full outer join
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"outer") \
    .show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"full") \
    .show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"fullouter") \
    .show(truncate=False)


# COMMAND ----------

# Left outer join
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"left").show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"leftouter").show(truncate=False)

# COMMAND ----------

# Right outer join
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"right").show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"rightouter").show(truncate=False)
