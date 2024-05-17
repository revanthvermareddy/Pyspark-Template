from pyspark.sql import DataFrame, SparkSession

def read_parquet(spark: SparkSession, path: str) -> DataFrame:
    return spark.read.parquet(path)
