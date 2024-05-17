from pyspark.sql import DataFrame, SparkSession


def read_csv(spark: SparkSession, path: str, inferSchema: bool = True) -> DataFrame:
    return spark.read.csv(path=path, header=True, inferSchema=inferSchema)
