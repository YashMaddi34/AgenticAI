import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

CATALOG = "claudecode_integration"
SCHEMA = "raw"

urls = {
    "airports":   "https://raw.githubusercontent.com/anshlambagit/Claude_X_Dtabricks/refs/heads/main/airports.csv",
    "bookings":   "https://raw.githubusercontent.com/anshlambagit/Claude_X_Dtabricks/refs/heads/main/bookings.csv",
    "passengers": "https://raw.githubusercontent.com/anshlambagit/Claude_X_Dtabricks/refs/heads/main/passengers.csv",
}

for table_name, url in urls.items():
    print(f"--- Ingesting {table_name} ---")

    pdf = pd.read_csv(url)
    print(f"Fetched {len(pdf)} rows, {len(pdf.columns)} columns: {list(pdf.columns)}")

    sdf = spark.createDataFrame(pdf)

    full_table = f"{CATALOG}.{SCHEMA}.{table_name}"
    (
        sdf.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(full_table)
    )
    print(f"Written to Delta table: {full_table}")

print("All tables ingested successfully.")
