from pyspark.sql import DataFrame
from typing import List

def write_parquet(df: DataFrame, path: str, partition_cols: List[str] = None) -> None:
    if partition_cols:
        df.write.partitionBy(partition_cols).parquet(path, mode="overwrite")
    else:
        df.write.parquet(path, mode="overwrite")
