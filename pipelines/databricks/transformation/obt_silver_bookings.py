from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder.getOrCreate()

SRC_CATALOG = "claudecode_integration"
SRC_SCHEMA = "raw"
TGT_CATALOG = "claudecode_integration"
TGT_SCHEMA = "silver"
TGT_TABLE = "obt_bookings"

bookings = spark.table(f"{SRC_CATALOG}.{SRC_SCHEMA}.bookings")
passengers = spark.table(f"{SRC_CATALOG}.{SRC_SCHEMA}.passengers")
airports = spark.table(f"{SRC_CATALOG}.{SRC_SCHEMA}.airports")

obt = (
    bookings
    .join(passengers, on="passenger_id", how="left")
    .join(airports, on="airport_id", how="left")
    .select(
        col("booking_id"),
        col("flight_id"),
        col("booking_date"),
        col("amount"),
        col("passenger_id"),
        col("name").alias("passenger_name"),
        col("gender"),
        col("nationality"),
        col("airport_id"),
        col("airport_name"),
        col("city").alias("airport_city"),
        col("country").alias("airport_country"),
    )
    .withColumn("booking_date", to_date(col("booking_date")))
)

full_table = f"{TGT_CATALOG}.{TGT_SCHEMA}.{TGT_TABLE}"

(
    obt.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(full_table)
)

print(f"OBT written to {full_table} with {obt.count()} rows.")
