from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, count, sum as _sum, round as _round

spark = SparkSession.builder.getOrCreate()

SRC_TABLE = "claudecode_integration.silver.obt_bookings"
TGT_CATALOG = "claudecode_integration"
TGT_SCHEMA = "gold"

obt = spark.table(SRC_TABLE)

# 1. Number of bookings per city
bookings_per_city = (
    obt
    .groupBy("airport_city", "airport_country")
    .agg(count("booking_id").alias("num_bookings"))
    .orderBy(col("num_bookings").desc())
)

# 2. Number of bookings per year
bookings_per_year = (
    obt
    .withColumn("booking_year", year("booking_date"))
    .groupBy("booking_year")
    .agg(count("booking_id").alias("num_bookings"))
    .orderBy("booking_year")
)

# 3. Revenue per year and month
revenue_per_year_month = (
    obt
    .withColumn("booking_year", year("booking_date"))
    .withColumn("booking_month", month("booking_date"))
    .groupBy("booking_year", "booking_month")
    .agg(
        count("booking_id").alias("num_bookings"),
        _round(_sum("amount"), 2).alias("total_revenue"),
    )
    .orderBy("booking_year", "booking_month")
)

tables = {
    "bookings_per_city":     bookings_per_city,
    "bookings_per_year":     bookings_per_year,
    "revenue_per_year_month": revenue_per_year_month,
}

for table_name, df in tables.items():
    full_table = f"{TGT_CATALOG}.{TGT_SCHEMA}.{table_name}"
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(full_table)
    )
    print(f"Written to {full_table}")

print("All gold aggregated tables written successfully.")
