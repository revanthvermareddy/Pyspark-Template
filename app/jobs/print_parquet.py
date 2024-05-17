"""sample batch job"""

import click
import logging

from pyspark.sql import SparkSession, DataFrame

from app.readers.parquet import read_parquet
from app.utils.spark import get_spark_session


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@click.command()
@click.option(
    "--input_path",
    "-i",
    type=str,
    required=True,
    default="data/input/userIds_prod.csv",
    help="Path to input csv file",
)
def print_parquet(input_path: str) -> None:
    # Get spark session
    logging.info("Creating Spark session")
    spark: SparkSession = get_spark_session(app_name="PySpark Job")

    # Read data
    logging.info(f"Reading data from {input_path}")
    df: DataFrame = read_parquet(spark, input_path)

    # Printing the dataframe
    logging.info(f"Printing dataframe")
    df.show()
