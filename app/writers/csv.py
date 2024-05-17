from pyspark.sql import DataFrame


def write_csv(df: DataFrame, path: str) -> None:
    df.write.csv(path, mode="overwrite")
