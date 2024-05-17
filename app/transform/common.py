from pyspark.sql import DataFrame


def rename_cols(df: DataFrame, columns: dict):
    for column_old_name, column_new_name in columns.items():
        df = df.withColumnRenamed(column_old_name, column_new_name)
    return df
