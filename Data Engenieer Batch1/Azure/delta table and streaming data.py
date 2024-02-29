# Databricks notebook source
# MAGIC %sql 
# MAGIC create table delta.`/tmp/deltain-table1` USING DELTA AS SELECT col1 as id FROM VALUES 200,300,400,500,600;

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from delta.`/tmp/deltain-table1`;

# COMMAND ----------

# streaming data 
streamingDf = spark.readStream.format("rate").load()
stream = streamingDf.selectExpr("value as id").writeStream.format("delta").option("checkpointLocation", "/tmp/checkpoint").start("/tmp/delta-table1")

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC UPDATE delta.`/tmp/delta-table1` 
# MAGIC SET id = id + 100 
# MAGIC WHERE id % 2 == 0;

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC DELETE FROM delta.`/tmp/delta-table1` WHERE id % 2 == 0;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TEMP VIEW newData AS SELECT col1 AS id 
# MAGIC FROM VALUES 1,3,5,7,9,11,13,15,17,19;

# COMMAND ----------

# MAGIC %sql 
# MAGIC MERGE INTO delta.`/tmp/delta-table1` AS oldData
# MAGIC USING newData
# MAGIC ON oldData.id = newData.id
# MAGIC WHEN MATCHED
# MAGIC   THEN UPDATE SET id = newData.id
# MAGIC WHEN NOT MATCHED
# MAGIC   THEN INSERT (id) VALUES (newData.id);
# MAGIC
# MAGIC SELECT * FROM delta.`/tmp/delta-table1`;

# COMMAND ----------

stream2 = spark.readStream.format("delta").load("/tmp/delta-table1").writeStream.format("console").start()
